#! /usr/bin/env python
# coding=utf-8
import json
import traceback

from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop

from configs.config_default import configs_default
from configs.config_error import config_error
from dal.dal_payment import Dal_Payment
from dal.dal_user import Dal_User
from logic.marker import Marker
from model.outgood import OutGood
from model.payment import Payment
from model.user import User
from tools.utils import Utils


class TCPConnection(object):
    def __init__(self, stream, address):
        self.mkid = ''
        self._stream = stream
        self._address = address
        self._stream.set_close_callback(self.on_close)
        self.read_message()
        print "A new user has connected.", address

    def read_message(self):
        self._stream.read_until('\n', self.broadcast_messages)

    def broadcast_messages(self, data):
        try:
            bJson = Utils().is_json(data)
            if bJson == False:
                self.read_message()
                return

            jsonData = json.loads(data)
            if 'msg' not in jsonData:
                self.read_message()
                return

            msg = jsonData['msg']
            if msg == 'init_mk':
                mkid = jsonData['mkid']
                self.on_init_mk(mkid)
            elif msg == 'beat_heart':
                self.on_beat_heart()
            elif msg == 'goods_update':
                self.on_goods_update(jsonData['newgoods'],jsonData['direction'])
            elif msg == 'auto_close_not_in':
                self.on_guester_door_state( configs_default['userstat']['out'])
            # elif msg == 'auto_close_not_out':
            #     self.on_guester_door_state( configs_default['userstat']['in'])

            self.read_message()
        except Exception, e:
            msg = traceback.format_exc()  # 方式1
            Utils().logMainDebug(msg)

    def send_message(self,data):
        self._stream.write(data)

    def on_close(self):
        MarketTcpServer.del_market(self.mkid)

##message handle
    def on_init_mk(self,mkid):
        self.mkid = mkid
        MarketTcpServer.add_market(mkid, self)
        msg = {'errorcode': config_error['success']}
        encodeMsg = json.dumps(msg)
        self.send_message(encodeMsg)

    def on_beat_heart(self):
        msg = {'errorcode': config_error['success']}
        encodeMsg = json.dumps(msg)
        self.send_message(encodeMsg)

    def on_goods_update(self,newgoods,action):
        MarketTcpServer.on_goodsUpdate(self.mkid, newgoods,action)

        msg = {'errorcode': config_error['success']}
        encodeMsg = json.dumps(msg)
        self.send_message(encodeMsg)


    def on_guester_door_state(self, state):
        MarketTcpServer.on_setUserState(None, state)

        msg = {'errorcode': config_error['success']}
        encodeMsg = json.dumps(msg)
        self.send_message(encodeMsg)


class MarketTcpServer(TCPServer):
    markets = dict()
    lastOpenDoorUser = None

    def handle_stream(self, stream, address):
        print "New connection :", address, stream
        TCPConnection(stream, address)
       # print "connection num is:", len(TCPConnection.clients)


#辅助函数
    @classmethod
    def init_free_markets(cls):
        for k,v in configs_default['free_markets'].iteritems():
            cls.add_market(k,None)

    @classmethod
    def is_free_markets(cls,id):
        return (id in  configs_default['free_markets'])

    @classmethod
    def add_market(cls,id,conn):
        if cls.markets.has_key(id) == False:
            newMt = Marker(id,conn)
            cls.markets[id] = newMt
        else:
            mk = cls.get_market(id)
            mk.m_conn = conn

    @classmethod
    def del_market(cls,id):
        if cls.markets.has_key(id) == True:
            mk = cls.get_market(id)
            mk.m_conn = None

    @classmethod
    def get_market(cls,id):
        return cls.markets.get(id)

    @classmethod
    def send_message(cls, mkid,data):
       try:
            mk = cls.get_market(mkid)
            if mk:
                if mk.m_conn:
                    mk.m_conn.send_message(data)
       except Exception, e:
           msg = traceback.format_exc()  # 方式1
           Utils().logMainDebug(msg)


    @classmethod
    def open_door_inner(cls, mkid,uid = None):
        try:
            userstate = configs_default['userstat']['out']
            Dal_User().updateUserState(uid,userstate)
            mk = cls.get_market(mkid)
            if mk == None:
                msg = {'errorcode': config_error['mkinvaild']}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            if mk.m_conn == None:
                msg = {'errorcode':config_error['mkdisconnect']}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            cls.lastOpenDoorUser = uid
            mk.del_guest(uid)

            msg = {'msg':'open_door_inner'}
            encodeMsg = json.dumps(msg)
            cls.send_message(mkid,encodeMsg)
            msg = {'errorcode': config_error['success'],'state':userstate}
            encodeMsg = json.dumps(msg)
            return encodeMsg

        except Exception, e:
            msg = traceback.format_exc()  # 方式1
            Utils().logMainDebug(msg)

    @classmethod
    def open_door(cls, mkid,uid = None):
        try:
            if uid:
                cls.check_user(uid)

            user = Dal_User().getUser(uid)
            if user== None:
                msg = {'errorcode': config_error['userinvaild']}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            if user.state != configs_default['userstat']['out']:#已经在室内了
                msg = {'errorcode': config_error['user_state_invaild'], 'state': user.state}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            lastOpenDoorUser = uid
            Dal_User().start_state_timeout(uid)

            mk = cls.get_market(mkid)
            if mk == None:
                msg = {'errorcode': config_error['mkinvaild']}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            if mk.m_conn == None:
                msg = {'errorcode':config_error['mkdisconnect']}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            if mk.m_disDoor:  # 结算期间不能开门
                msg = {'errorcode': config_error['mk_paying_state']}
                encodeMsg = json.dumps(msg)
                return encodeMsg


            guester = mk.get_guest(uid)
            if guester == None:
               mk.add_guest(uid)


            Dal_User().updateUserState(uid,mkid)

            msg = {'msg':'open_door'}
            encodeMsg = json.dumps(msg)
            cls.send_message(mkid,encodeMsg)
            msg = {'errorcode': config_error['success'],'state':user.state}
            encodeMsg = json.dumps(msg)
            return encodeMsg

        except Exception, e:
            msg = traceback.format_exc()  # 方式1
            Utils().logMainDebug(msg)

    # 添加主动扫描商品
    @classmethod
    def on_zdAddGood(cls, mkid, uid, gid):
        try:
            mkid = str(mkid)
            mk = cls.get_market(mkid)
            if mk == None:
                msg = {'errorcode': config_error['mkinvaild']}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            if mk.m_conn == None:
                msg = {'errorcode':config_error['mkdisconnect']}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            user = Dal_User().getUser(uid)
            if user.state == configs_default['userstat']['out']:#已经在室外了
                msg = {'errorcode': config_error['user_state_invaild'], 'state': user.state}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            guester = mk.get_guest(uid)
            if guester == None:
                mk.add_guest(uid)
                guester = mk.get_guest(uid)
            count = guester.add_good(gid)

            msg = {'errorcode': config_error['success'], 'good': gid,'count':count,'state':user.state}
            encodeMsg = json.dumps(msg)
            return encodeMsg

        except Exception, e:
            msg = traceback.format_exc()  # 方式1
            Utils().logMainDebug(msg)

    # 删除主动扫描商品
    @classmethod
    def on_zdDelGood(cls, mkid, uid, gid):
        try:
            mkid = str(mkid)
            mk = cls.get_market(mkid)
            if mk == None:
                msg = {'errorcode': config_error['mkinvaild']}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            if mk.m_conn == None:
                msg = {'errorcode':config_error['mkdisconnect']}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            user = Dal_User().getUser(uid)
            if user.state == configs_default['userstat']['out']:#已经在室外了
                msg = {'errorcode': config_error['user_state_invaild'], 'state': user.state}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            guester = mk.get_guest(uid)
            if guester == None:
                mk.add_guest(uid)
                guester = mk.get_guest(uid)

            count = guester.del_good(gid)

            msg = {'errorcode': config_error['success'], 'good': gid,'count':count,'state':user.state}

            encodeMsg = json.dumps(msg)
            return encodeMsg

        except Exception, e:
            msg = traceback.format_exc()  # 方式1
            Utils().logMainDebug(msg)

    # 用户请求付款(主动)
    @classmethod
    def on_payZDReq(cls, mkid,uid):
        try:
            mkid = str(mkid)
            uid = str(uid)
            goods = ''
            mk = cls.get_market(mkid)
            if mk == None:
                msg = {'errorcode': config_error['mkinvaild']}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            if mk.m_conn == None:
                msg = {'errorcode':config_error['mkdisconnect']}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            user = Dal_User().getUser(uid)
            if user.state == configs_default['userstat']['out']:#已经在室外了
                msg = {'errorcode': config_error['user_state_invaild'], 'state': user.state}
                encodeMsg = json.dumps(msg)
                return encodeMsg
            if mk:
                guester = mk.get_guest(uid)
                if guester:
                    gCount = guester.check_goods()
                    if gCount == 0:
                        cls.open_door_inner(mkid,uid)
                        mk.m_disDoor = False
                    else:
                        mk.m_disDoor = True
                        mk.start_pay_timeout()
                        goods = guester.format_goods()
                else:
                    cls.open_door_inner(mkid, uid)
                    mk.m_disDoor = False

                paymsg = {'errorcode': config_error['success'], 'id': uid, 'goods':goods,'state':user.state}
                return paymsg


            paymsg = {'errorcode':  config_error['mkinvaild']}
            return paymsg
        except Exception, e:
            msg = traceback.format_exc()  # 方式1
            Utils().logMainDebug(msg)

    # 用户请求付款(被动)
    @classmethod
    def on_payBDReq(cls, mkid, uid):
        try:
            user = Dal_User().getUser(uid)
            if user.state == configs_default['userstat']['out']:  # 已经在室外了
                msg = {'errorcode': config_error['user_state_invaild'], 'state': user.state}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            mkid = str(mkid)
            uid = str(uid)

            mk = cls.get_market(mkid)
            if mk == None:
                msg = {'errorcode': config_error['mkinvaild']}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            if mk.m_conn == None:
                msg = {'errorcode':config_error['mkdisconnect']}
                encodeMsg = json.dumps(msg)
                return encodeMsg

            if mk:
                mk.m_paymsg = mk.format_goods()
                if mk.m_paymsg == '':
                    cls.open_door_inner(mkid, uid)
                    mk.m_disDoor = False
                else:
                    mk.m_disDoor = True
                    mk.start_pay_timeout()

                paymsg = {'errorcode': config_error['success'], 'id': uid, 'goods':  mk.m_paymsg}

                encodeMsg = json.dumps(paymsg)
                return encodeMsg

            paymsg = {'errorcode': config_error['mkinvaild']}
            encodeMsg = json.dumps(paymsg)
            return encodeMsg
        except Exception, e:
            msg = traceback.format_exc()  # 方式1
            Utils().logMainDebug(msg)

            # 处理支付结果，开门，数据存储

    @classmethod
    def handlePayResult(cls, mkid, uid, goods, price,payway = configs_default['payway']['wx']):
        try:
            mkid = str(mkid)
            uid = str(uid)
            goods = str(goods)

            mk = cls.get_market(mkid)
            if mk:
                    # update database
                    newPayment = Payment()
                    newPayment.mkid = mkid
                    newPayment.userid = uid
                    newPayment.goods = goods
                    newPayment.price = int(price)
                    newPayment.time = Utils().dbTimeCreate()
                    newPayment.payway = payway
                    Dal_Payment().addPayment(newPayment)

                     #失效处理
                    goodsArray = goods.split(';')
                    for k, v in enumerate(goodsArray):
                        goodArray = v.split(':')
                        gID = goodArray[0]
                        gCount = goodArray[1]
                        mk.outDate_goods(uid,gID,gCount)
                    mk.clear_goods()  # 清空当前

                    mk.m_disDoor = False  # 放开限制
                    mk.stop_pay_timeout()
                    cls.open_door_inner(mkid,uid)

        except Exception, e:
            msg = traceback.format_exc()  # 方式1
            Utils().logMainDebug(msg)

    @classmethod
    def check_user(cls, uid):
        user = Dal_User().getUser(uid)
        if user == None:#第一次自动创建用户
            user = User()
            user.id = uid
            user.state = configs_default['userstat']['out']
            Dal_User().addUser(user)
        return user

    # 商品增量更新
    @classmethod
    def on_goodsUpdate(cls, mkid, newgoods,action):
        mkid = str(mkid)
        mk = cls.get_market(mkid)
        if mk:
            if action == "none":
                mk.clear_goods()
            elif action == "+":
                mk.add_goods(newgoods)
            elif action == "-":
                mk.remove_goods(newgoods)

    #
    @classmethod
    def on_getUserState(cls, uid):
        try:
            if uid:
                cls.check_user(uid)

            user = Dal_User().getUser(uid)
            msg = {'errorcode': config_error['success'],'state': user.state}
            encodeMsg = json.dumps(msg)
            return encodeMsg

        except Exception, e:
            msg = traceback.format_exc()  # 方式1
            Utils().logMainDebug(msg)

#如果uid为空，则默认是最后一个人
    @classmethod
    def on_setUserState(cls, uid = None,state = configs_default['userstat']['out']):
        try:
            user = None
            if uid == None:
                uid = MarketTcpServer.lastOpenDoorUser

            user = Dal_User().getUser(uid)
            if user:
               user.state = state
               Dal_User().updateUserState(uid, state)

        except Exception, e:
            msg = traceback.format_exc()  # 方式1
            Utils().logMainDebug(msg)
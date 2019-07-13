#-*-coding:utf-8-*-
'''
逻辑玩家类
'''
from dal.dal_outgood import Dal_OutGood
from logic.guester import Guester
from model.outgood import OutGood
from tools.mainTimerManager import MainTimerManager
## 定义超市类
from tools.utils import Utils


class Marker:
    def __init__(self,id,conn):##链接，id
       self.m_id = id#玩家userid
       self.m_conn = conn
       self.m_userPool = dict()
       self.m_goodsPool = dict()#被动扫码使用
       self.m_disDoor = False#结算期间不能开门
       self.m_timerMgr = MainTimerManager()  ##超时处理队列
       self.m_paymsg = ''

    def add_guest(self, id, conn = None):
    #   self.del_guest(id)
       if self.m_userPool.has_key(id) == False:
           newG = Guester(id, conn)
           self.m_userPool[id] = newG
           return newG

    def del_guest(self, id):
        if self.m_userPool.has_key(id) == True:
           self.m_userPool.pop(id)
           return True
        return False

    def get_guest(self, id):
       return self.m_userPool.get(id)

    def start_pay_timeout(self):
        self.stop_pay_timeout()
        self.m_timerMgr.addTimer(self.m_id, self.on_pay_timeout, 20000,{})

    def stop_pay_timeout(self):
        self.m_timerMgr.delTimer(self.m_id)

    def on_pay_timeout(self,arg):  ##支付超时处理
        self.m_disDoor = False

    def add_goods(self,gid):
        if Dal_OutGood().getOutGood(gid):
             return
        real_gid = gid[4:8]
        if self.m_goodsPool.has_key(real_gid) == False:
           self.m_goodsPool[real_gid] = list()
           self.m_goodsPool[real_gid].append(gid)
        else:
           self.m_goodsPool[real_gid].append(gid)

    def remove_goods(self,gid):
        real_gid = gid[4:8]
        if self.m_goodsPool.has_key(real_gid):
            self.m_goodsPool[real_gid].remove(gid)
            if len(self.m_goodsPool[real_gid]) == 0:
               self.m_goodsPool.pop(real_gid)

#过期处理
    def outDate_goods(self,uID,gID,gCount):
        gCount = int(gCount)
        if  self.m_goodsPool.has_key(gID):
            gList = self.m_goodsPool[gID]
            count = 0
            for real_gid in gList:
                if count >= gCount:return
                count = count  +  1
                outgood = OutGood()
                outgood.mkid = self.m_id
                outgood.uid = uID
                outgood.id = real_gid
                outgood.time = Utils().dbTimeCreate()
                Dal_OutGood().addOutGood(outgood)


    def clear_goods(self):
        self.m_goodsPool.clear()
        self.m_paymsg = ""

    def check_goods(self):
         return  len(self.m_goodsPool)

    def format_goods(self):
         sGoods = ''
         for k,v in self.m_goodsPool.iteritems():
             sGoods = sGoods + k + ':' + str(len(v)) +';'
         self.m_paymsg = sGoods[:-1]
         return  self.m_paymsg


#-*-coding:utf-8-*-
'''
逻辑玩家类
'''

## 定义顾客类
class Guester:
    def __init__(self,id,conn):##链接，id
       self.m_id = id#玩家userid
       self.m_conn = conn
       self.m_goodsPool = dict()

    def add_good(self, gid):
        if self.m_goodsPool.has_key(gid) == False:
           self.m_goodsPool[gid] = 1
        else:
           self.m_goodsPool[gid] =  self.m_goodsPool[gid]  + 1
        return self.m_goodsPool[gid]

    def del_good(self, gid):
        if self.m_goodsPool.has_key(gid):
            self.m_goodsPool[gid] = self.m_goodsPool[gid] - 1
            if self.m_goodsPool[gid] == 0:
               self.m_goodsPool.pop(gid)
               return 0
            return  self.m_goodsPool[gid]
        return 0

    def clear_good(self):
       self.m_goodsPool.clear()

    def format_goods(self):
        sGoods = ''
        for k, v in self.m_goodsPool.iteritems():
            sGoods = sGoods + k + ':' + str(v) + ';'
        return  sGoods[:-1]

    def check_goods(self):
         return  len(self.m_goodsPool)

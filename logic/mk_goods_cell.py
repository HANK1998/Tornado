#-*-coding:utf-8-*-
'''
逻辑玩家类
'''

## 定义顾客类
class MKGoodsCell:
    def __init__(self,id,gCount):##dbid，商品count
       self.m_id = id#数据库mk_goods主键id
       self.m_gCount = gCount#对应记录的商品数量


# -*-coding:utf-8-*-
from orm.orm import Model, IntegerField, StringField


##库存信息模型
class Warehouse(Model):
    __table__ = "warehouse"
    __primary_key__ = "id"

    # 库存编号
    id = IntegerField('id', False)
    # 商品名
    p_name = StringField('p_name', True)
    # 批次ID
    p_id = IntegerField('p_id',True)
    # 入库时间
    inTime = StringField('inTime', True)
    # 仓库时间
    outTime = StringField('outTime', True)
    # 仓库ID
    w_id = IntegerField('w_id', True)
    # 入库公司ID
    in_c_id = IntegerField('in_c_id', True)
    # 批次ID
    out_c_id = IntegerField('p_id', True)
    # 存量
    stock = IntegerField('stock', True)
# -*-coding:utf-8-*-
from orm.orm import Model, IntegerField, StringField


##批次信息模型
class Batch(Model):
    __table__ = "batch"
    __primary_key__ = "id"

    # 批次编号
    id = IntegerField('id', False)
    # 商品时间
    prodtime = StringField('prodtime', True)
    # 生产公司id
    pc_id = IntegerField('pc_id', True)
    # 商品名
    p_name = StringField('p_name', True)
    # 原料商品批次id组合
    mat_list = StringField('mat_list', True)
    # 过期时间
    exptime = StringField('exptime', True)
    # 该批商品简介
    intro = StringField('intro', True)
    # 订单ID
    man_id = IntegerField('man_id',True)
    # 物流id
    log_id = IntegerField('log_id',True)
    # 批次含量
    amount = IntegerField('amount', True)
    # 商品图片
    pro_img = StringField('pro_img',True)
    # 二维码图片
    qr_img = StringField('qr_img', True)
    # 条形码图片
    br_img = StringField('br_img', True)
    # 批次产生时间
    time = StringField('time', True)
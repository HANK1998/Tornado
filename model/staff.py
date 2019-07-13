# -*-coding:utf-8-*-
from orm.orm import Model, IntegerField, StringField


##职员信息模型
class Staff(Model):
    __table__ = "staff"
    __primary_key__ = "id"

    # 职员编号
    id = IntegerField('id', False)
    # 职员名
    name = StringField('name', True)
    # 联系方式
    tel=StringField('tel',True)
    # 工作类型
    type = StringField('type', True)
    #照片地址
    photoPath=StringField('photoPath',True)
    # 公司编号
    companyId = StringField('companyId', True)
    # 入职时间
    entryTime = StringField('entryTime', True)
    # 离职时间
    leaveTime = StringField('leaveTime', True)

# -*-coding:utf-8-*-
from orm.orm import Model, IntegerField, StringField


##公司信息模型
class Company(Model):
    __table__ = "company"
    __primary_key__ = "id"

    # 公司编号
    id = IntegerField('id', False)
    # 密码
    password = StringField('password', True)
    # 公司地址
    name = StringField('name', True)
    # 公司地址
    address = StringField('address', True)
    # 公司简介
    profile = StringField('profile', True)
    # 营业执照图片路径
    blPath = StringField('blPath', True)
    # 生产许可证图片路径
    pcPath = StringField('pcPath', True)
    # 安全认证图片路径
    scPath = StringField('scPath', True)
    # 联系方式
    tel = StringField('tel', True)
    # 注册时间
    rTime = StringField('rTime', True)
    # 公司类型
    type =StringField('type',True)

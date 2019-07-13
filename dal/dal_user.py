# -*- coding:utf-8 -*-
#普通用户数据处理
import math

from dal.dal_base import Dal_base
from model.user import User


class Dal_user(Dal_base):
    ##数据库信息进缓存
    def initCache(self):
        self.initDB("User", User)
    #添加用户
    def addUser(self,newUser):
        newUser.id=newUser.save()
        self._m_cache[newUser.id]=newUser
        return newUser.id
    #删除用户
    def deleteUser(self,pk):
        pk=int(pk)
        return self.delete(pk,User)
    #修改信息
    def updateUser(self,pk,**kwargs):
        pk=int(pk)
        return self.update(pk,User,**kwargs)
    #查找所有用户,并分页
    def selectAllUser(self,pageId):
        page = {}
        if pageId == None:
            return page
        pageNum = 3
        page_start = (int(pageId) - 1) * pageNum
        page_end = page_start + pageNum
        num = 0
        temp = self._m_cache.keys()[page_start:page_end]
        count = 0.0
        for k in self._m_cache.iteritems():
            count += 1
        page["count"] = math.ceil(count / pageNum)
        for value in temp:
            page[num] = self._m_cache[value]
            num += 1
        return page
    #查找指定用户
    def selectUser(self,pk):
        pk=int(pk)
        return self.get(pk, User)
    #通过名字和密码查找用户
    def selectUserByNP(self, name, password):
        for k, v in self._m_cache.iteritems():
            if v['name'] == name:
                if v['password'] == password:
                    return True
        return None
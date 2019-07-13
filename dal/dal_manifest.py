# -*- coding:utf-8 -*-
#普通用户数据处理
import math

from dal.dal_base import Dal_base
from model.manifest import Manifest
from dal.dal_staff import Dal_Staff
from dal.dal_company import Dal_Company


class Dal_Manifest(Dal_base):
    ##数据库信息进缓存
    def initCache(self):
        self.initDB("Manifest", Manifest)
    #添加订单
    def addManifest(self,newManifest):
        newManifest.id=newManifest.save()
        self._m_cache[newManifest.id]=newManifest
        return newManifest.id
    #删除订单
    def deleteManifest(self,pk):
        pk=int(pk)
        return self.delete(pk,Manifest)
    #修改订单
    def updateManifest(self,pk,**kwargs):
        pk=int(pk)
        return self.update(pk,Manifest,**kwargs)
    #查找所有订单,并分页
    def selectAllManifest(self,pageId):
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
    #查找指定订单
    def selectManifest(self,pk):
        pk=int(pk)
        return self.get(pk, Manifest)
    #通过名字和密码查找用户
    def selectManifestByNP(self, name, password):
        for k, v in self._m_cache.iteritems():
            if v['name'] == name:
                if v['password'] == password:
                    return True
        return None

        # 通过职员id查找订单
    def selectManifestBySID(self,sid):
        res = {}
        i = 0
        for k, v in self._m_cache.iteritems():
            v_id = int(v['originatorId'])
            if  v_id == sid:
                v_res = Dal_Staff().selectStaff(v_id)
                v['Sname'] = v_res['name']
                res[i] = v
                i += 1
        return res

        # 通过公司id查找订单
    def selectManifestByCId(self,cid):
        res = {}
        i = 0
        for k, v in self._m_cache.iteritems():
            v_id = int(v['place'])#获取目标公司id
            if  v_id == cid:
                v_res = Dal_Staff().selectStaff(int(v['originatorId']))#获取发起人信息
                c_id = v_res['companyId']#获取发起人公司id
                c_res = Dal_Company().selectCompany(c_id)#查询公司信息
                v['c_name'] = c_res['name']#放入订单字典
                res[i] = v
                i += 1
        return res
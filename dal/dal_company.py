# -*- coding:utf-8 -*-
# 公司信息数据处理
import math
import os
import shutil

from dal.dal_base import Dal_base
from model.company import Company


class Dal_Company(Dal_base):
    ##数据库信息进缓存
    def initCache(self):
        self.initDB("Company", Company)

    # 添加公司信息
    def addCompany(self, newCompany):
        newCompany.id = newCompany.save()
        self._m_cache[newCompany.id] = newCompany
        return newCompany.id

    # 删除公司信息
    def deleteCompany(self, pk):
        pk = int(pk)
        company = Dal_Company().selectCompany(pk)
        if (company == None):
            return False
        shutil.rmtree(r'./static/img/company/' + str(pk))
        return self.delete(pk, Company)

    # 修改公司信息
    def updateCompany(self, pk, **kwargs):
        pk = int(pk)
        return self.update(pk, Company, **kwargs)

    # 查找所有公司信息,并分页
    def selectAllCompany(self, pageId):
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
#        page["count"] = math.ceil(count / pageNum)
        for value in temp:
            page[num] = self._m_cache[value]
            num += 1
        return page

    # 查找指定公司信息
    def selectCompany(self, pk):
        pk = int(pk)
        return self.get(pk, Company)

    # 查找ID和密码公司信息
    def selectCompanyByIP(self, id,password):
        id=int(id)
        for k, v in self._m_cache.iteritems():
            if v['id'] == id and v['password']==password:
                return v
        return None

    # 通过名字查找公司信息
    def selectCompanyByN(self, companyName):
        for k, v in self._m_cache.iteritems():
            if v['name'] == companyName:
                return v
        return None

    def selectCompanyByNID(self, companyName):
        for k, v in self._m_cache.iteritems():
            if v['name'] == companyName:
                return v['id']
        return None

    # 上传图片处理
    def addPhoto(self, photo, type):
        id=1
        for k in self._m_cache.iteritems():
            id+=1
        id=str(id)
        filepath = r'./static/img/company/' + id + ''
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        for temp in photo:
            photoname = id + '_' + type + '.jpg'
            photopath = os.path.join(filepath + '/', photoname)
            with open(photopath, 'wb') as up:
                up.write(temp['body'])
        return photopath

    # 修改图片
    def updatePhoto(self, id, photo, type):
        id=str(id)
        filepath = r'./static/img/company/' + id + ''
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        for temp in photo:
            photoname = id + '_' + type + '.jpg'
            photopath = os.path.join(filepath + '/', photoname)
            with open(photopath, 'wb') as up:
                up.write(temp['body'])

    def getCompanyNameByType(self,type):
        res = {}
        i = 0
        for k,v in self._m_cache.iteritems():
            if v['type'] == type:
                res[i] = v['name']
                i += 1
        return res

    def getCompanyNameByDType(self,type):
        res = {}
        i = 0
        for k,v in self._m_cache.iteritems():
            a = str(v['type'])
            if a == 'productionA' or a == 'productionB':
                res[i] = v['name']
                i += 1
        return res

    def selectC_nameByID(self, id):
        for k, v in self._m_cache.iteritems():
            if v['id'] == id:
                return v['name']
        return None
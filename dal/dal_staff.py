# -*- coding:utf-8 -*-
# 职员信息数据处理
import os
from dal.dal_base import Dal_base
from model.staff import Staff


class Dal_Staff(Dal_base):
    ##数据库信息进缓存
    def initCache(self):
        self.initDB("Staff", Staff)

    # 添加职员信息
    def addStaff(self, newStaff):
        newStaff.id = newStaff.save()
        self._m_cache[newStaff.id] = newStaff
        return newStaff.id

    # 删除职员信息
    def deleteStaff(self, pk):
        pk = int(pk)
        staff = Dal_Staff().selectStaff(pk)
        if (staff == None):
            return False
        os.remove(staff["photoPath"])
        return self.delete(pk, Staff)

    # 修改职员信息
    def updateStaff(self, pk, **kwargs):
        pk = int(pk)
        return self.update(pk, Staff, **kwargs)

    # 查找所有职员信息,并分页
    def selectAllStaff(self, pageId):
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

    # 查找指定职员信息
    def selectStaff(self, pk):
        pk = int(pk)
        return self.get(pk, Staff)

        # 通过名字，密码，类型查找职员信息

    def selectStaffByCid(self,companyId):
        staff={}
        res = {}
        i = 0
        companyId = int(companyId)
        for k, v in self._m_cache.iteritems():
            if v['companyId'] == companyId:
                staff[i]=v
                # staff[i][0]
                i += 1
        return staff

    # 通过名字，密码，类型查找职员信息
    def selectStaffByNPT(self,name,type):
        for k, v in self._m_cache.iteritems():
            if v['name'] == name and v['type'] == type:
                return True
        return None

    # 上传图片处理
    def addPhoto(self, photo):
        id = 1
        for k, v in self._m_cache.iteritems():
            id += 1
        for temp in photo:
            photoname = str(id) + '.jpg'
            photopath = os.path.join(r'./static/img/staff/', photoname)
            with open(photopath, 'wb') as up:
                up.write(temp['body'])
        return photoname

    # 修改图片
    def updatePhoto(self, id, photo):
        for temp in photo:
            photoname = str(id) + '.jpg'
            photopath = os.path.join(r'./static/img/staff/', photoname)
            with open(photopath, 'wb') as up:
                up.write(temp['body'])

    def selectStaffByCT(self,companyId,type):
        staff={}
        res = {}
        i = 0
        companyId = int(companyId)
        for k, v in self._m_cache.iteritems():
            stype = v['type'].encode("utf-8")
            if v['companyId'] == companyId and stype == type:
                staff[i]=v['name']
                i += 1
        return staff

    def selectStaffByName(self,name):
        for k, v in self._m_cache.iteritems():
            # vt = str(v['type'])
            vt = v['type'].encode('utf-8')
            if v['name'] == name and vt == "司机":
                return v
        return None

    def selectStaffByCName(self,name,cid):
        for k, v in self._m_cache.iteritems():
            if v['name'] == name and v['companyId'] == int(cid):
                return v
        return None
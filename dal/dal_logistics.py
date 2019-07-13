# -*- coding:utf-8 -*-
# 物流信息数据处理
import copy
import math

from dal.dal_base import Dal_base
from model.logistics import Logistics


class Dal_Logistics(Dal_base):
    ##数据库信息进缓存
    def initCache(self):
        self.initDB("Logistics", Logistics)

    # 添加物流信息
    def addLogistics(self, newLogistics):
        newLogistics.id = newLogistics.save()
        self._m_cache[newLogistics.id] = newLogistics
        return newLogistics.id

    # 删除物流信息
    def deleteLogistics(self, pk):
        pk = int(pk)
        logistics = Dal_Logistics().selectLogistics(pk)
        if (logistics == None):
            return False
        return self.delete(pk, logistics)

    # 修改物流信息
    def updateLogistics(self, pk, **kwargs):
        pk = int(pk)
        return self.update(pk, Logistics, **kwargs)

    # 查找所有物流信息,并分页
    def selectAllLogistics(self, pageId,type, companyId):
        logistic = {}
        page = {}
        if pageId == None:
            return page
        pageNum = 3
        num = 0
        k = 0
        for key, v in self._m_cache.iteritems():
            if (type == 'p' and companyId == int(v['startPlace'])):
                logistic[k] = copy.deepcopy(v)
                k += 1
            elif (type == 'g' and companyId == int(v['endPlace'])):
                logistic[k] =copy.deepcopy(v)
                k += 1
            # if (companyId == int(v['startPlace'])):
            #     logistic[k] = v
            #     k += 1
        count = 0.0

        for k in logistic.iteritems():
            count += 1
        if (pageId > math.ceil(count / pageNum)):
            page_start = count - pageNum
        else:
            page_start = (int(pageId) - 1) * pageNum
        page_end = page_start + pageNum
        if page_start < 0:
            page_start = 0
        temp = logistic.keys()[page_start:int(page_end)]

        #        page["count"] = math.ceil(count / pageNum)
        for k in temp:
            for key, value in logistic.items():
                if k == key:
                    page[num] = value
                    num += 1
        page["total"] = int(math.ceil(count / pageNum))
        return page

    # 查找指定物流信息
    def selectLogistics(self, pk):
        pk = int(pk)
        return self.get(pk, Logistics)
    # 通过溯源码、始发地查找物流信息
    def selectShelvesByNCW(self, number, companyId,place):
        for k, v in self._m_cache.iteritems():
            if v['number'] == number and v['companyId'] == companyId and v['place'] == place:
                return v
        return None

 # 加密
    def decrypt(srcStr, password='193876245'):
        # 数字替换还原
        tempStr = ""
        for index in range(len(srcStr)):
            tempStr += str(password.find(srcStr[index]))
        # 去掉长度位，还原成字典
        index = 0
        strList = []
        while True:
            # 取长度位
            length = int(tempStr[index])
            # 取数字字符串
            s = tempStr[index + 1:index + 1 + length]
            # 加入到列表中
            strList.append(s)
            # 增加偏移量
            index += 1 + length
            # 退出条件
            if index >= len(tempStr):
                break
        data = bytearray(len(strList))
        for i in range(len(data)):
            data[i] = int(strList[i])
        return data.decode('utf-8')

    def selectMyLogG(self,pk):
        res = {}
        i=0
        for k, v in self._m_cache.iteritems():
            if v['endPlace'] == pk:
                res[i] = v
                i+=1
        return res

    def selectMyLogP(self,pk):
        res = {}
        i=0
        for k, v in self._m_cache.iteritems():
            if v['startPlace'] == pk:
                res[i] = v
                i+=1
        return res

# -*- coding:utf-8 -*-
# 仓储信息数据处理

from dal.dal_base import Dal_base
from model.warehouse import Warehouse
from dal.dal_company import Dal_Company
from dal.dal_batch import Dal_Batch

class Dal_Warehouse(Dal_base):
    ##数据库信息进缓存
    def initCache(self):
        self.initDB("Warehouse", Warehouse)

    # 添加仓储信息
    def addWarehouse(self, newWarehouse):
        newWarehouse.id = newWarehouse.save()
        self._m_cache[newWarehouse.id] = newWarehouse
        return newWarehouse.id

    # 删除仓储信息
    def deleteWarehouse(self, pk):
        pk = int(pk)
        warehouse = Dal_Warehouse().selectWarehouse(pk)
        if (warehouse == None):
            return False
        return self.delete(pk, warehouse)

    # 修改仓储信息
    def updateWarehouse(self, pk, **kwargs):
        pk = int(pk)
        return self.update(pk, Warehouse, **kwargs)

    # 查找所有仓储信息,并分页
    def selectAllWarehouse(self, pageId):
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

    # 查找指定仓储信息
    def selectWarehouse(self, pk):
        pk = int(pk)
        return self.get(pk, Warehouse)

    # 通过溯源码查找仓储信息
    def selectWarehouseByCS(self,code,shelvesId):
        for k, v in self._m_cache.iteritems():
            if v['code'] == code and v['shelvesId']==int(shelvesId):
                return v
        return None

    def getAllProd(self,id):
        id = int(id)
        list = {}
        i = 0
        for k,v in self._m_cache.iteritems():
            if v['w_id'] == id:
                list[i] = v
                i += 1
        res = {}
        i = 0
        for key,value in list.items():
            res[i] = {'outTime':value.outTime,
                      'in_company':Dal_Company().selectC_nameByID(value.in_c_id),
                      'p_name':value.p_name,
                      'p_id':value.p_id,
                      'inTime':value.inTime,
                      'stock':value.stock,
                      'out_company':''
                      }
            if value.out_c_id != '':
                res[i]['out_company'] = Dal_Company().selectC_nameByID(value.out_c_id)
            else:
                res[i]['out_company'] = value.out_c_id
            i += 1
        return res

    def getProdBN(self,id,name):
        id = int(id)
        list = {}
        i = 0
        for k, v in self._m_cache.iteritems():
            if v['w_id'] == id and v['p_name'] == name:
                list[i] = v
                i += 1
        res = {}
        i = 0
        for key, value in list.items():
            res[i] = {'outTime': value.outTime,
                      'in_company': Dal_Company().selectC_nameByID(value.in_c_id),
                      'p_name': value.p_name,
                      'p_id': value.p_id,
                      'inTime': value.inTime,
                      'stock': value.stock,
                      'out_company': ''
                      }

            if value.out_c_id != '':
                res[i]['out_company'] = Dal_Company().selectC_nameByID(value.out_c_id)
            else:
                res[i]['out_company'] = value.out_c_id
            i += 1
        return res

    #仓库公司查询
    def getAllProdWa(self,id):
        res = {}
        i = 0
        id = int(id)
        for k, v in self._m_cache.iteritems():
            p_id = v['p_id']
            if v['w_id'] == id:
                batch = Dal_Batch().selectBatch(p_id)
                res[i] = {
                    "p_name" : batch['p_name'],
                    "prodtime" : batch['prodtime'],
                    "exptime" : batch['exptime'],
                    "man_id" : batch['man_id'],
                    "amount" : batch['amount']
                }
                i+=1
        return res
    #零售公司查询
    def getAllProdMa(self,id):
        res = {}
        i = 0
        id = int(id)
        for k, v in self._m_cache.iteritems():
            p_id = v['p_id']
            if v['out_c_id'] == id:
                batch = Dal_Batch().selectBatch(p_id)
                res[i] = {
                    "p_name": batch['p_name'],
                    "prodtime": batch['prodtime'],
                    "exptime": batch['exptime'],
                    "man_id": batch['man_id'],
                    "amount": batch['amount']
                }
                i += 1
        return res
    #生产公司查询
    def getAllProdPd(self,id):
        res = {}
        i = 0
        id = int(id)
        for k, v in self._m_cache.iteritems():
            p_id = v['p_id']
            if v['in_c_id'] == id:
                batch = Dal_Batch().selectBatch(p_id)
                res[i] = {
                    "p_name": batch['p_name'],
                    "prodtime": batch['prodtime'],
                    "exptime": batch['exptime'],
                    "man_id": batch['man_id'],
                    "amount": batch['amount']
                }
                i += 1
        return res
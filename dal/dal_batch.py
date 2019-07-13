# -*- coding:utf-8 -*-
# 批次信息数据处理
import qrcode
import os

from dal.dal_base import Dal_base
from dal.dal_company import Dal_Company
from model.batch import Batch


class Dal_Batch(Dal_base):
    ##数据库信息进缓存
    def initCache(self):
        self.initDB("Batch", Batch)

    # 添加批次信息
    def addBatch(self, newBatch):
        newBatch.id = newBatch.save()
        self._m_cache[newBatch.id] = newBatch
        return newBatch.id

    # 删除批次信息
    def deleteBatch(self, pk):
        pk = int(pk)
        batch = Dal_Batch().selectBatch(pk)
        if (batch == None):
            return False
        return self.delete(pk, batch)

    # 修改批次信息
    def updateBatch(self, pk, **kwargs):
        pk = int(pk)
        return self.update(pk, Batch, **kwargs)

    # 查找所有批次信息,并分页
    def selectAllShelves(self, pageId):
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

    # 查找指定批次信息
    def selectBatch(self, pk):
        pk = int(pk)
        return self.get(pk, Batch)

    def createQrCode(self, code):
        img = qrcode.make('code')
        img.save('test1.png')

        # 上传图片处理
    def addPhoto(self, photo):
        id = 1
        for k, v in self._m_cache.iteritems():
            id += 1
        for temp in photo:
            photoname = str(id) + '.jpg'
            photopath = os.path.join(r'./static/img/production/', photoname)
            with open(photopath, 'wb') as up:
                up.write(temp['body'])
        return photoname

    def selectBatchBCid(self,companyId):
        batch={}
        i = 0
        companyId = int(companyId)
        for k, v in self._m_cache.iteritems():
            if v['pc_id'] == companyId:
                batch[i]=v
                i += 1
        res = {}
        i = 0
        for key, value in batch.items():
            res[i] = {'id': value.id,
                      'prodtime': value.prodtime,
                      'pc_name': Dal_Company().selectC_nameByID(value.pc_id),
                      'p_name': value.p_name,
                      'mat_name': None,
                      'exptime': value.exptime,
                      'intro': value.intro,
                      'man_id':value.man_id,
                      'log_id':value.log_id,
                      'pro_img':value.pro_img,
                      'qr_img':value.qr_img,
                      'br_img':value.br_img,
                      'time':value.time,
                      'amount':value.amount
                      }
            i += 1
        return res
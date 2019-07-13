# -*-coding:utf-8-*-

import json

from handlers.BaseHandler import BaseHandler
from dal.dal_company import Dal_Company
from dal.dal_batch import Dal_Batch
from dal.dal_logistics import Dal_Logistics
from dal.dal_staff import Dal_Staff
from dal.dal_manifest import Dal_Manifest

class SelectByCodeHandlers(BaseHandler):
    def get(self):
        self.render("page/selectApp.html")

    def post(self):
        post_data = {}
        for key in self.request.arguments:
            post_data[key] = self.get_argument(key)

        encode = post_data['code']
        # 解密
        # code = decrypt(encode, '1938762450')
        c_code = int(encode[3:7])#截取公司id
        b_code = int(encode[7:])#截取批次id

        c_res = Dal_Company().selectCompany(c_code)#获取公司信息
        b_res = Dal_Batch().selectBatch(b_code)#获取批次信息

        prod = {
            'prodtime':b_res['prodtime'],
            'p_name': b_res['p_name'],
            'exptime': b_res['exptime'],
            'intro': b_res['intro'],
            'pro_img': b_res['pro_img'],
            'br_img': b_res['br_img'],
        }
        #获取订单信息
        man_id = b_res['man_id']
        m_res = Dal_Manifest().selectManifest(man_id)
        s_res = Dal_Staff().selectStaff(m_res['originatorId'])
        maniefest = {
            'staff':s_res['name']
        }
        #获取物流信息
        log_id = b_res['log_id']
        l_res = Dal_Logistics().selectLogistics(log_id)
        d_name = Dal_Staff().selectStaff(l_res['driverId'])
        logistic = {
            'd_name':d_name['name'],
            'plateNum':l_res['plateNum'],
            'start_p':Dal_Company().selectC_nameByID(l_res['startPlace']),
            'end_p':Dal_Company().selectC_nameByID(l_res['endPlace']),
            'time':l_res['time']
        }
        #获取公司信息
        company = {
            'name':c_res['name'],
            'address':c_res['address'],
            'profile': c_res['profile'],
            'tel': c_res['tel'],
            'pcPath': c_res['pcPath'],
            'blPath': c_res['blPath'],
            'scPath': c_res['scPath'],
        }

        data = {'errorcode':0,'prod':prod,"maniefest":maniefest,"logistic":logistic,"company":company}
        self.write(json.dumps(data))

#解密
def decrypt(srcStr,password='193876245'):
    #数字替换还原
    tempStr=""
    for index in range(len(srcStr)):
        tempStr+=str(password.find(srcStr[index]))
    #去掉长度位，还原成字典
    index=0
    strList=[]
    while True:
        #取长度位
        length=int(tempStr[index])
        #取数字字符串
        s=tempStr[index+1:index+1+length]
        #加入到列表中
        strList.append(s)
        #增加偏移量
        index+=1+length
        #退出条件
        if index>=len(tempStr):
            break
    data=bytearray(len(strList))
    for i in range(len(data)):
        data[i]=int(strList[i])
    return data.decode('utf-8')









#coding:utf-8
import json
import os

from tools.singleton import Singleton
import time
import datetime
import logging
from datetime import date
from datetime import datetime
#工具类
class Utils:
    __metaclass__ = Singleton
    ##工具中包含有 截取字符串的    编码的 解码的  是否为空的  获取文件路径的
#prama: ,,,;,,, return dict
    def decodeMutilFormat(self,inputstring,char1,char2):## 输入的字符串"1:30;2:20;3:90;4;90"
        outResult = {}
        outlist = inputstring.split(char1);

        for substr in outlist:
            arrStr = substr.split(char2)
            outResult[arrStr[0]] = arrStr[1]
        return outResult

    def encodeMutilFormat(self,inputDict,char1,char2):
        outResult = '' ##{‘name’:"blx","age":20,"sex":"nan"}
        i = 0
        dlen = len(inputDict)
        for k, v in inputDict.iteritems():
            outResult = outResult + k + char2 + v
            i = i + 1
            if i < dlen:
                outResult = outResult + char1

        return outResult

#prama: ;;;; [] return str
    def encodeIDFormat(self,inputList,char = ';'):  ## 列表转化为字符串
        outResult = ''
        index = 0
        listlen = len(inputList)
        for substr in inputList:
            index = index + 1
            if index < listlen:
                outResult = outResult +substr+ char
            else:
                outResult = outResult +substr
        return outResult
    ## decodeIDFromat() 解码 就是分割字符串 分隔符 传入一个字符串和分隔符 输出一个列表
    def decodeIDFormat(self,inputstring,char = ';'):  ## 字符串转化为列表"1;2;3;4;5" ==> [1,2,3,4]
        outResult = []
        outlist = inputstring.split(char)
        for substr in outlist:
            outResult.append(substr)
        return outResult
    ## 判断某个元素是否在一个字符串（可以分割成列表）中
    def isValueInIDFormat(self,v,inputstring):
        if self.isNull(inputstring):
            return False
        outlist = self.decodeIDFormat(inputstring)
        return (str(v) in outlist)   ##返回的值是False  和 True
    ## 判断是否为空
    def isNull(self,v):
        return (v == None or v == '');

    def getFileCountInPath(self,path):
        count = 0
        for root, dirs, files in os.walk(path):
        #print files
            fileLength = len(files)
            if fileLength != 0:
               count = count + fileLength
        return count

    def dbTime2Client(self,timeDB):
        timeArre = time.strptime(timeDB, "%Y-%m-%d %H:%M:%S")
        timestrap = int(time.mktime(timeArre))
        v1 = datetime.datetime.utcfromtimestamp(timestrap)
        return v1

    def dbTimeCreate(self):
        return time.strftime('%Y-%m-%d %H:%M:%S')

    def logMainDebug(self, msg):
        loger = logging.getLogger("ingenia")
        loger.info(msg)

    def is_json(self,myjson):
        try:
            json_object = json.loads(myjson)
        except ValueError, e:
             return False
        return True

    def tupleToDict(self, data):
        n=0
        data_dict = {}
        for i in data:
            data_dict[n]=i
            n+=1

        return data_dict

class JsonExtendEncoder(json.JSONEncoder):
    """  
        This class provide an extension to json serialization for datetime/date.  
    """

    def default(self, o):
        """  
            provide a interface for datetime/date  
        """
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o,date):
            return o.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, o)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
import json
import requests
import time
import threading

#查询数据库
def Slelect_Park():
   # 打开数据库连接
   db = pymysql.connect("localhost", "root", "123456", "centerServer", charset='utf8' )

   # 使用cursor()方法获取操作游标
   cursor = db.cursor()

   # SQL 查询语句

   #f_name = 'apple'
   sql = "SELECT * FROM Area WHERE AreaName = 'B1' or AreaName = 'B2' #INCOME > %s" % (1000)
   try:
      # 执行SQL语句
      cursor.execute(sql)
      # 获取所有记录列表
      results = cursor.fetchall()
      # print(''results[0][5])

      B1 = results[0][5];
      B2 = results[1][5];
      print("B1剩余车辆=%s,B2剩余车辆%s" % (B1, B2))

      Park_Lout ={}
      Park_Lout["B1"] = B1
      Park_Lout["B2"] = B2
      jsonStr = json.dumps(Park_Lout)



      return jsonStr
      #return Park_Lout
      #print(jsonStr)

   except:
      print("Error: unable to fecth data")
   # 关闭数据库连接
   db.close()



def Send(jsonStrs):

   #url = ""
   #requests.post(url='', data=json.dumps({'key1': 'value1', 'key2': 'value2'}),headers={'Content-Type': 'application/json'})
   try:
      url = 'http://192.168.1.51'
      headers={'Content-Type': 'application/json'}
      requests.post(url=url, data=jsonStrs,headers=headers, timeout=5)
   except Exception as e:
      print("服务器断开")

def While_():
   # 数据库查询
   jsonStrs = Slelect_Park()
   print(jsonStrs)
   # 发送数据给服务器
   Send(jsonStrs)

if __name__ == '__main__':
   while(1):
      While_()
      time.sleep(30)
      #timer = threading.Timer(10, While_)
      #timer.start()
   #t = time(10.0, While_)
   #t.start()




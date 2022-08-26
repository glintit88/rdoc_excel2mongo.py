#coding=utf-8
  
import xlrd
import sys
import json
import pymongo
import datetime
from pymongo import MongoClient
'''
def xldate_to_datetime(xldate):
    temp = datetime.datetime(1900, 1, 1)
    delta = datetime.timedelta(days=xldate)
    return temp+delta

def overdue(duedate):
    td=datetime.datetime.now()
    xx=td-duedate
    return xx.days
'''  
#连接数据库
client=MongoClient('localhost',27017)
db_name='rdoc01'
db=client[db_name]
#mycol=db["employee2"]
#mydoc=mycol.find().sort("Customer Code")
ss=0

'''
for x in mydoc:
    
    cc=x['Customer Code']
    print(cc,'\n')
    dd=x['Due date']
    idate=x['Inv Date']
    if(idate):
        ddate=int(dd)
        duedate=xldate_to_datetime(ddate-2)
        print('Due Date: ', duedate.strftime("%d-%m-%Y"))
        oday=overdue(duedate)
        if(oday>0):
            print('===>>> OVERDUE ---> ', oday, ' DAYS')
        ss=int(idate)
        aa=xldate_to_datetime(ss-2)
        print(aa.strftime("%Y/%m/%d"))
    #dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + idate - 2)
    #tt = dt.timetuple()
    #print(dt, tt)
    print(x,'\n')
'''
collection = db['budget2022']
#collection_set01 = db['set01']
account=db.rdoc01
  
data=xlrd.open_workbook('budget2022.xls')
table=data.sheets()[0]
#读取excel第一行数据作为存入mongodb的字段名
rowstag=table.row_values(0)
nrows=table.nrows
#ncols=table.ncols
#print rows

returnData={}
for i in range(1,nrows-1):
  #将字段名和excel数据存储为字典形式，并转换为json格式
  returnData[i]=json.dumps(dict(zip(rowstag,table.row_values(i+1))))
  #通过编解码还原数据
  returnData[i]=json.loads(returnData[i])
  #print returnData[i]
  print('\n', i,returnData[i])
  collection.insert_one(returnData[i])
  #account.insert(returnData[i])
  


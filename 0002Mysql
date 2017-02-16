#!/usr/bin/env python
# -*-coding:utf-8-*-
#Q:第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

#A:
import MySQLdb
import string,random


wordLength = 20     #length
wordAllNeed = 200   #count
saveResult = [] #init for save relustNumber
i = 0       #init for add data indexNumber

def basisWord():
    return string.letters + string.digits   #26word(upper && lower) with all number

def everyOneWord():
    saveList = []
    for i in range(wordLength):         #range=20,get key's length
        result = random.choice(basisWord())     #random.choice( ) within one'e list to random on word
        saveList.append(result)
    return "".join(saveList)            #return all word piece one word

for x in range(wordAllNeed):        #range 200 get all result And save in saveResult[]
    saveResult.append(everyOneWord())


#connect MySQL
#i advance create a database name:DebugOne ,And has a table name:adwardTable

connect = MySQLdb.connect('localhost', 'root', '123456', 'DebugOne')    #连接数据库
cursor = connect.cursor()
cursor.execute('use DebugOne;')
try:
    for _ in range(200):
        if _ < 200:
            sql = 'insert into adwardTable value( \'' + str(i+1) + '\','  + '\'' + saveResult[i] + '\' );'
            i += 1
            cursor.execute(sql)
    connect.autocommit(on=connect)
except:
    connect.rollback()      #rollback

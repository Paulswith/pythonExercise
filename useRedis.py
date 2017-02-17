#!/usr/bin/env python
# -*-coding:utf-8-*-
#第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

import redis
import string,random


wordLength = 20      #length
wordAllNeed = 200      #count
saveResult = []     #init for save relustNumber

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

def initRedis():
    connectRedis = redis.Redis(host='localhost',port=6379,db=0)
    return connectRedis

# initRedis().flushdb()   # it can cleanup this list
# try:
# for _ in range(200):
#     x = 0
#     if _ < 200:
#         # initRedis().hset('users:jerry','has200KeyNumber', saveResult[i])
#         initRedis().set(i, saveResult[x])
#             # initRedis().lpush('number'+str(i), _+'s')
#         i += 1
#         x += 1
# except:
#     raise
for _ in saveResult:
    initRedis().lpush('saveKeys', _)  #use lpush one by one save in listName:saveKeys

hasAll = initRedis().lrange('saveKeys',0,-1)
for _ in hasAll:    #枚举检测是否成功
    print _


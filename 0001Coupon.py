#/usr/bin/env python
# -*-coding:utf-8-*-
#Q:第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
#A：

import string,random

wordLength = 20
wordAllNeed = 200

def basisWord():
    return string.letters + string.digits   #26word(upper && lower) with all number

def everyOneWord():
    saveList = []
    for i in range(wordLength):         #range=20,get key's length
        result = random.choice(basisWord())     #random.choice( ) within one'e list to random on word
        saveList.append(result)
    return "".join(saveList)            #return all word piece one word

# def rangeGetWord(count,list=None):
#     if list is None:
#         list = []
#     for x in range(count):
#         everyWord = everyOneWord()
#         list.append(everyWord)
#     return list
#
# rangeGetWord(wordAllNeed)             when use this mothod , it can't work shangxin
if list is None:
    list = []
for x in range(wordAllNeed):
    print everyOneWord()

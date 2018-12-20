#!/usr/bin/python
# -*- coding: UTF-8 -*-
#变量类型
number = 1
floatx = 1.000000001
string = "xxxxxxx"
dictionaty = {"x":1,"y":"x"}
list = [1,0]

print number + 0.11111111
print floatx + 1
print string + 'y'
print dictionaty['x']
print list[1]


#字符串操作
print string
print string[0] #感觉就是字符串数组
print string[0:3]

#牛逼的操作
listnew = ["print me ！",0]
concatList = list + listnew
print concatList[2]

#元数组（不可被修改的数组）
tuple1 = ("hello","world")
print tuple1
print tuple1[0:1][0] #分割之后还是元数组类型吗

#是的！
''' 
tuple2 = tuple1[0:1]
tuple2[0] = "new ~"
print tuple2
'''

#字典操作
dictionaty2 = {0:["hello","world"],"1":{"hello":"world"}}

print dictionaty2[0][0]
print dictionaty2["1"]['hello']
print dictionaty2.keys()
print dictionaty2.values()
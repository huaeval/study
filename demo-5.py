#!/usr/bin/python

#数学函数
import math
import string

print dir(math)

#字符串

#1.字符串截取 split?

h = "hello,world!"

print h[:6] + "nihao!" + h #原字符串标改变

#2.字符串格式化

fix = 'nihao %s ,im %s ,h ASCII is : %c' % ("tony",'eval',"h")

print fix #h ... 不知道为什么

uincodex = u'Hello\u0020World !'
print uincodex

#3.字符串方法

#首字母大写
print string.capitalize("hello world !")

#center 
s1 = "你是头小乳猪？"
scenter = s1.center(100,"b")
print scenter
#count
s2 = "上海自来水来自海上"
print s2.count("海",4) #utf-8字符串天坑。

#endswith 检查结尾
str3 = "wuma.jpg"
print str3.endswith(".jpg")

#find 查找

s4 = "你是我的小苹果"
print s4.find("我的")

#join 

s5 = "hello,world"
print s5.join("*")




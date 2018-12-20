#!/usr/bin/python
# -*- coding: UTF-8 -*-

#类型转换

print int('12',10)

#为什么二机制回出错呢？
#print int('12',2)

print int(1.0000)
#print int ("10px") 并没有js的特效
#print int ("m10") 也不认识这种乱七巴扎的东西

#18位长度 支持文本整数1 不支持文本小数1.1
print long(1)
print long("1")
#print long("1.1") error! 不知道为什么。
print long(1.000001)
print long(1234567890123456789.00000111111111111111)

#8位小数
print float(1)
print float("1")
print float(1.000001)
print float(11.00000111111111111111)

print str(10086) + ' over!'
#print 10086 + ' over!' error!数字和文本不能相加，这是要智能呢，还是要只能呢？
number = 10010
print str(number) + ' add str!'

# print eval("printx = 1")
#!/usr/bin/python
def printme( str ):
   "打印传入的字符串到标准显示设备上"
   print str
   return

printme("print function")

def funcaguments(arg1, *vartuple ):
   "函数_文档字符串"
   print list(vartuple)
   return arg1

print funcaguments("show",1,2,3)

sum = lambda arg1,arg2:arg1 + arg2

print sum(1,2)

'''
sumList = lambda list :
    _sum = 0
    for item in list:
        _sum += item

    return _sum
'''

print globals()

print locals()
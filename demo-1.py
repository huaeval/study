#!/usr/bin/python
# -*- coding: UTF-8 -*-

if True:
    print "TRUE"
else:
    print "FALSE"

#测试错误
'''
    if True:
        print "TRUE"
    else:
    print "FALSE"
'''

#多行输入

print "h" + \
      "e" + \
      "l" + \
      "l" + \
      "o"

#python 引号

word = 'word'
sentence = "这是一个句子"
paragraph = '''这他么就很厉害了

很牛逼的代码'''

print word + \
      sentence + \
      paragraph

#处理输入，这个就很牛逼了
input = raw_input("按下 enter 键退出，其他任意键显示...\n")
print input

#导入系统包
import sys; 
sys.stdout.write(input + '\n .......<')

#if elseif 就不要学了吧
caseNum = "1"
if caseNum == "0":
    sys.stdout.writelines("if?" + caseNum)
elif caseNum == "1":
    print "elif?" + caseNum
else:
    print "else"

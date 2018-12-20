#!/usr/bin/python

#list

hello = "hello"
nihao = "nihao"
list = ["hello","world",0,1]
if(hello in list):
    print "list 包含 hello"
if(nihao not in list):
    print "list 不包含 nihao"
else:
    print "list 包含 nihao"

#is 关键字
a = 100000001000000
b = 100000001000000

#b = "10" #文本比较

#列表比较
'''
a = [1,2]
b = [1,2]
'''

if(a is b):
    print "a is b return True"
else:
    print "a is b return False"

#循环
# 1. while 

list = [1,2,3,4,5,6,7,8,9]
odd = []
even = []
while len(list) > 0:#学习新关键字len
    num = list.pop()
    if num % 2 ==0:
        even.append(num)
    else:
        odd.append(num)
print odd
print even

## 测试len
print len("这个很长？") #utf 占3字节位 输入15.讲道理我需要输出4。后面继续

#continue and break
i = 0
while  i<10:
    i+=1
    if i % 2 > 0:
        continue
    print "continue:"+str(i)

j = 1
while  j>0:
    j+=1
    if j  > 9:
        print "break:"+str(j)
        break
    else:
        print "break-else:"+str(j)

'''
var = 1
while var == 1 :  # 该条件永远为true，循环将无限执行下去
   num = raw_input("Enter a number  :")
   print "You entered: ", num
 
print "Good bye!"
'''

#raw_input 输入？ sys.?

#while else
k = 0
while k < 10 :
    k+=1
else :
    print "while else is :" + str(k) 

# 2. for

for item in "hello":
    if item == "l":
        continue
    elif item == "o":
        break
    print item
    dis = {"key":"value"}
    for key in dis:
        if item == "h":
            break 
        print key +" : "+ dis[key]

fruits = ['banana', 'apple',  'mango']

# .需要下标
for index in range(len(fruits)):
    print "index :" + str(index) + " (:value :" + fruits[index]

#range 是啥？
#print range(100)

# . for ...else (@_@)

for item in ["hello","world"]:
    '''
    if item == "world": 
        break #break 结束的循环，else不执行
    '''
    print item
else :
    print "for end?"

# 3. 循环嵌套

cloumn = 0
while cloumn < 9 :
    cloumn += 1
    for row in range(9):
        print str(cloumn) + "*" + str(row+1) + "=" + str(cloumn * (row+1))
else :
    print "-----------end-----------"
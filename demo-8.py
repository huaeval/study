#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Myodule
from dirmodule import MyModule2
#from 'dirmodule/MyModule.py' import MyModule

if __name__ == '__main__':
    print '作为主程序运行'
else:
    print '初始化'


Myodule.printstr("打印吧。。。。")
MyModule2.printstr("包打印。。。")

Myodule.printstr(str(Myodule.sum(10,30)))

print dir(Myodule)
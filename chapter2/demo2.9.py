# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:CY
@file: demo2.9.py
@time: 2019/06/02
"""
import random

import array

'''
2.9  当列表不是首选时
'''
# 2.9.1  数组
print('\n------------------------------------------------------')
print('示例2-20  一个浮点数组的创建、存入文件和从文件读取的过程')
print('------------------------------------------------------\n')

floats = array.array('d', (random.random() for i in range(10**7)))
# 此处调用要注意是  模块名.函数名 （直接调用方法名是不可以的）  ps:调用类里的方法:  模块名.类名.函数名
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array.array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats[-1] == floats2[-1])

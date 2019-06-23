'''
声称其表达式
'''

#示例2-5  用生成器表达式初始化元组和数组

symbols = '$¢£¥€¤'
t = tuple(ord(symbol) for symbol in symbols)
print(t)


import array
a = array.array('I', (ord(symbol) for symbol in symbols))
print(a)


#示例2-6  使用生成器表达式计算笛卡儿积

colors = ['black', 'white']
sizes = ['L', 'M', 'S']
for tshirts in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirts)
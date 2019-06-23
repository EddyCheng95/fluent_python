'''
2.4.1   为什么切片和区间会忽略最后一个元素
'''


'''
2.4.2   对对象进行切片
'''
invoice = '''
0.....6.................................40..........52...55........
1909  Pimoroni Pibrella                 $17.50      3    $52.50
1489  6mm Tactile Switch x20            $4.95       2    $9.90
1510  Panavise Tr. - PV-201             $28.00      1    $28.00
1601  PiTFT Mini Kit 320x240            $34.95      1    $34.95   
'''
SKU = slice(0,6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40,52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55,None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])


'''
2.4.3   多维切片和省略
'''

'''
2.4.4   给切片赋值
'''

l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
# l[2:5] = 100赋值的对象是一个切片，那么赋值的右侧必须是一个可迭代对象
l[2:5] = [100]
print(l)


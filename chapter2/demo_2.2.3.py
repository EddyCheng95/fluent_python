'''
笛卡儿积
'''

#示例2-4  使用列表推导计算笛卡儿积

colors = ['black', 'white']
sizes = ['L', 'M', 'S']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))


tshirts = [(color, size) for size in sizes
                         for color in colors]

print(tshirts)
for size in sizes:
    for color in colors:
        print(color, size)
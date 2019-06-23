'''
2.3元组不仅仅是不可变的列表

2.3.1元组和记录
'''
#示例2-7  把元组用作记录
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)


'''
2.3.2   元组拆包
'''
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates # 元组拆包
print(latitude)
print(longitude)

#j交换两个变量的值
a = 1
b = 2
b, a = a, b #优雅的一批
print(a,b)

d = divmod(20, 8)
print(d)
t = (20, 8)
t1 = divmod(*t)
print(t1)
quotient, remainder = divmod(*t)
print(quotient, remainder)


import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)

a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)


a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)



'''
2.3.3   嵌套元组拆包
'''
#示例2-8  用嵌套元组拆包来获取经度

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
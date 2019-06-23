'''
具名元组
'''
#示例2-9  定义和使用具名元组
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

#示例2-10 具名元组的属性和方法
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi)
for key, value in delhi._asdict().items():
    print(key + ':',value)
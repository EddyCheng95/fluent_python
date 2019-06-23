'''
2.7 list.sort方法和内置函数sorted
'''
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(fruits)
l = sorted(fruits, reverse=True)
print(l)
l = sorted(fruits, key=len)
print(l)
l = sorted(fruits, key=len, reverse=True)
print(l)
print(fruits)
fruits.sort()
print(fruits)
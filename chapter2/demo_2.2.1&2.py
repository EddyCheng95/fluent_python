'''
2.2.1列表推导和可读性
'''

#示例2-1把一个字符串变成Unicode码位的列表
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

#示例2-2把字符串变成Unicode编码的另一种写法
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)

'''
2.2.2列表推导同filter和map比较
'''

#示例2-3 用列表推导和map/filter组合来创建同样的表单

symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)
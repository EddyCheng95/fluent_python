'''
2.6 序列的增量赋值
'''
l = [1, 2, 3]
print(id(l))
l *= 2
print(l)
print(id(l))
t = (1, 2, 3)
print(id(t))
t *= 2
print(t)
print(id(t))


'''
一个关于+=的谜题
'''
#示例2-14 一个谜题

t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]
except TypeError:
    print("'tuple' object does not support item assignment")
print(t)

#示例2-16 s[a] += b 背后的字节码
import dis
dis.dis('s[a] += b')

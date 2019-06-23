
'''
2.8 用bisect来管理已排序的序列
'''


# 2.8.1  用bisect来搜索
import bisect
import random
import sys

print('\n------------------------------------------------------')
print('示例2-17  在有序序列中用bisect查找某个元素的插入位置')
print('------------------------------------------------------\n')

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

print('DEMO:', bisect_fn.__name__)
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_fn)

print('\n------------------------------------------------------')
print('示例2-18  根据一个分数，找到它对应的成绩')
print('------------------------------------------------------\n')


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


l = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]];
print(l)

# 2.8.2  用bisect.insort插入新元素
print('\n------------------------------------------------------')
print('示例2-19  根据一个分数，找到它对应的成绩')
print('------------------------------------------------------\n')

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

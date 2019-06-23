'''
2.5 对序列使用+和*
'''
l = [1, 2, 3]
print(l*5)
print(l + [4, 5, 6])
print(5 * 'abcd')

'''
建立又列表组成的列表
'''

#示例 2-12
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

#示例 2-13
weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = 'O'
print(weird_board  )
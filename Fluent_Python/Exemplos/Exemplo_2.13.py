# Uma lista com três referências à mesma lista é inutil

weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = '0'
print(weird_board)

row = ['_'] * 3
board =[]
for i in range(3):
    board.append(row)
board[2][0] = 'X'
print(board)
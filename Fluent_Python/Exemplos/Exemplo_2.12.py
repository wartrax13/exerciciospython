#Uma lista com três listas de tamanho 3 pode representar um tabuleiro de jogo da velha
board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)

board = ['  ',' ',' ',' ',' ',' ',' ',' ',' ']
choices = []
def print_board(board):
    print(board[0],'|',board[1],'|',board[2],'\n','-----------\n',board[3],'|',board[4],'|',board[5],'\n','-----------\n',board[6],'|',board[7],'|',board[8],'\n','-----------\n')

playerone = True
winner = False

print("Welcome to Intergalactic Tic Tac Toe!")
# blank board
print_board(board)
print(playerone + 1)

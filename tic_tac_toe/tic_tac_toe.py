from __future__ import print_function
import sys

squares = []

for board in range (0, 9):
    squares.append(str(board))

playerOneTurn = True
winner = False
def print_w_board() :    
    print('  ' + '|' + '  ' + '|' + '  ')
    print( '-----------')
    print('  ' + '|' + '  ' + '|' + '  ')
    print( '-----------')
    print('  ' + '|' + '  ' + '|' + '  ')
    print( '-----------')

def print_board_parameters() :
    print( board[0] + '|' + board[1] + '|' + board[2])
    print( '-----------')
    print( board[3] + '|' + board[4] + '|' + board[5])
    print( '-----------')
    print( board[6] + '|' + board[7] + '|' + board[8])
    print( '-----------')

    print_w_board()
    while not winner :
    print("Welcome to Intergalactic Tic Tac Toe!")
    print_board_parameters()

    if playerOneTurn :
        print( "Player 1:, it's your turn. Which square?")
        print_board_parameter()
    else :
        print( "Player 2:")
    choice = int(input())
    if playerOneTurn :
        board[choice] = 'X'
        print_board_parameter()
        print("Interesting choice, Player 1.")
    else :
        board[choice] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (board[y] == board[(y + 1)] and board[y] == board[(y + 2)]) :
            winner = True
            print_board_parameter()
        if (board[x] == board[(x + 3)] and board[x] == board[(x + 6)]) :
            winner = True
            print_board_parameter()
        if((board[0] == board[4] and board[0] == board[8]) or
            (board[2] == board[4] and board[4] == board[6])) :
            winner = True
            print_board_parameter()

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")

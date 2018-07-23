import sys

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

board_num = ['0','1','2','3','4','5','6','7','8','9']
def print_board(board):
    print(board[0],'|',board[1],'|',board[2],'\n','-----------\n',board[3],'|',board[4],'|',board[5],'\n','-----------\n',board[6],'|',board[7],'|',board[8],'\n','-----------\n')

def print_num_board(board_num):     
    print_board(board_num)

def main(args):
    playerone = True
    winner = False
    print("Welcome to Intergalactic Tic Tac Toe!")
    print_board(board)
    
    while not winner:
        if playerone:
            print("Player 1, it's your turn. Which square?")
            print_num_board(board_num)
        else: 
            print("Player 2, it's your turn. Which square?")
            print_num_board(board_num)
        choice = int(input())
        if  playerone:
            board[choice] = 'X'
            board_num[choice] = 'X'
            print("Interesting choice, Player 1.") 
            print_board(board)
        else:
            board[choice] = 'O'
            board_num[choice] = 'O'
            print("Interesting choice, Player 2.")
            print_board(board)
        playerone = not playerone
        
        for x in range (0, 2):
            y = x * 3
            if (board_num[y] == board_num[(y + 1)] and board_num[y] == board_num[(y + 2)]):
                winner = True
                print_board(board_num)
            if (board_num[x] == board_num[(x + 3)] and board_num[x] == board_num[(x + 6)]):
                winner = True
                print_board(board_num)
            if((board_num[0] == board_num[4] and board_num[0] == board_num[8]) or 
                (board_num[2] == board_num[4] and board_num[4] == board_num[6])) :
                winner = True
                print_board(board_num)
    print ("Player " + str(int(playerone + 1)) + " wins!\n")

if __name__ == "__main__":
    main(sys.argv)

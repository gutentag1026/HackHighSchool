choices = []
ch = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
num = []
checkturns = []
for x in range(0, 9):
    choices.append(str(x))
for x in range(0,9):
    num.append(str(x))

playerOneTurn = True
winner = False

def print_w_Board():
    print(ch[0] + '|' + ch[1] + '|' + ch[2])
    print('------')
    print(ch[3] + '|' + ch[4] + '|' + ch[5])
    print('------')
    print(ch[6] + '|' + ch[7] + '|' + ch[8])

def printBoard():
    print(choices[0] + '|' + choices[1] + '|' + choices[2])
    print('------')
    print(choices[3] + '|' + choices[4] + '|' + choices[5])
    print('------')
    print(choices[6] + '|' + choices[7] + '|' + choices[8])

def print_num_Board():
    print(num[0] + '|' + num[1] + '|' + num[2])
    print('------')
    print(num[3] + '|' + num[4] + '|' + num[5])
    print('------')
    print(num[6] + '|' + num[7] + '|' + num[8])

print("Welcome to Intergalactic Tic Tac Toe!")
print_w_Board()
print('\n')
while not winner:
    if (len(checkturns) == 9 and winner == False):
        print("Both lost")
        break

    if playerOneTurn:
        print("Player 1, it's your turn. Which square?")
        print_num_Board()
        print("\n")
    else:
        print("Player 2: it's your turn. Which square?")
        print_num_Board()
        print('\n')
    try:
        choice = int(input())
        checkturns.append(choice)
    except:
        print("please enter a valid field")
        continue
    if choices[choice] == 'X' or choices[choice] == 'O':
        print("illegal move, plase try again")
        continue

    if playerOneTurn:
        choices[choice] = 'X'
        print("Interesting choice, Player 1.")
        ch[choice] = 'X'
        print_w_Board()
        print('\n')
    else:
        choices[choice] = 'O'
        print("Interesting choice, Player 2.")
        ch[choice] = 'O'
        print_w_Board()
        print('\n')
    playerOneTurn = not playerOneTurn

    for x in range(0, 3):
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]):
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]):
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or
    (choices[2] == choices[4] and choices[4] == choices[6])):
        winner = True
        printBoard()
    if winner == True:
        print("Player " + str(int(playerOneTurn + 1)) + " wins!\n")

import random
import sys

def guess_func(n,word,five):
    guess = input()
    print("GUESS:",guess)
    if(guess == ""):
        print("You wasted a guess!")
    elif(len(guess) != len(word)):
        print("0, 1, 2, 3, 4 that’s how we count to five!")
    elif(guess[0] != word[0] and (len(guess) == len(word))):
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    elif(guess[0] == word[0] and (len(guess) == len(word)) and (guess != word)):
        print("You have", (n - 1) ,"guesses left!")
    elif(guess == word):
        print("Good Job! You are one with the Source.")
        exit()

def main(args): 
    five = ["champ", "charm", "clean", "clear", "danny", "dream", "drive", "eager", "enjoy","extra"]
    word = random.choice(five)
    print("The secret word begins with a", word[0],".")
    for n in range(10):
        guess_func((10 - n), word, five)

if __name__ == "__main__":
    main(sys.argv)

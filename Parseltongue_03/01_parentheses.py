#!/usr/bin/env python3

# IDK
# By yhuang

import sys

def CaP(text):
    i = True
    string = ""
    for char in text:
        if i:
            string += char.upper()
        else:
            string += char.lower()
#       if (char != '"' and char != '(' and char != ')' and char != '?' and char != ' '):
        if (char.isalpha()):
            i = not i
    return string

def ReplaceVowel(test):
    for letter in test:
        if letter in ['a','e','i','o','u','A','E','I','O','U']:
           test = test.replace(letter, '*')
    print(test)

def check_parentheses(s):
    j = 0
    for c in s:
        if c == ')':
            j -= 1
            if j < 0:
                return False
        elif c == '(':
            j += 1
    return j == 0

def main(args):
    print(CaP(args[1]))
    a = CaP(args[1])
    ReplaceVowel(a)
    Result = check_parentheses(args[1])
    if(Result == False):
        print("Balanced? False")
    else:
        print("Balanced? True")
if __name__ == "__main__":
    main(sys.argv)

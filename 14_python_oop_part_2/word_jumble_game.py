# Design a word jumble game


'''
The user will be shown some jumbled word such as -> PPELAS
The user is supposed to guess that word and enter it
If the guess is correct the user will be awarded point
Otherwise, no points.

PPELSA
INPUT <- APPLES 
-> one point awarded

ITEKS
INPUT <- KSTIES
-> No points awarded
-> Correct answer KITES

Finally give the score

'''
import random

def jumble(s):
    temp = list(word)
    random.shuffle(temp)
    return ''.join(temp)

# List of words
L = ["apples", "laptop", "airplane", "india", "elephant", "mobile", "pencil", "computer", "banana"]
random.shuffle(L)

points = 0

# Repeat the following for entire list
for word in L:

    # Choose a word randomly
    # Shuffle the characters in the word
    jword = jumble(word)

    # Show it to the user and take the input
    print("Can you guess this word -> ", jword)
    uinput = input("-> ")

    # Check if the input is correct or not
    # Based on that award point
    if(uinput == word):
        points += 1
        print("Correct")
    else:
        print("Incorrect")

    print('-' * 60)

# Show the report to the user

print("Your score ", points, '/', len(L))

# [July 4th, 2022]
# Improvement #1
# Offer a second chance if the first guess in incorrect
#      -> first attempt 2 points
#      -> second attent 1 point
# How to keep the words and their clues?

# Improvement #2
# You need to pick up the words and clues from a file

# How can we make this game multi player?

# []

# Improvement #3
# Add more difficulty levels

# Improvement #4
# Add GUI to this game


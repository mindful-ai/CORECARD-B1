'''

    -> PLEPAS
    Guess this word ? APPLES
    -> THYPNO
    Guess this word ? PYTHON

    ---------------------------

    RESULT: Excellent Playing

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
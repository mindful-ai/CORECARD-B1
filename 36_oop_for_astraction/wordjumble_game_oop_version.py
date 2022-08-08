import random
from unicodedata import name
# core dev
class game:

    def __init__(self, name, age, level=1):
        self.name = name
        self.age = age
        self.L = ["apples", "laptop", "airplane", "india", "elephant", "mobile", "pencil", "computer", "banana"]
        self.points = 0

    def jumble(self, word):
        temp = list(word)
        random.shuffle(temp)
        return ''.join(temp)

    def run(self):
        print("Player --> ", self.name)
        random.shuffle(self.L)
        # Repeat the following for entire list
        for word in self.L:

            # Choose a word randomly
            # Shuffle the characters in the word
            jword = self.jumble(word)

            # Show it to the user and take the input
            print("Can you guess this word -> ", jword)
            uinput = input("-> ")

            # Check if the input is correct or not
            # Based on that award point
            if(uinput == word):
                self.points += 1
                print("Correct")
            else:
                print("Incorrect")

            print('-' * 60)

    def result(self):
        print("Your score ", self.points, '/', len(self.L))

# ----------------------------------------
# app developer
p1 = game('Avkash', 25)
p2 = game('Bharti', 25)

p1.run()
p2.run()

p1.result()
p2.result()
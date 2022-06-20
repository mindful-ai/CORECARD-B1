'''
INPUT: This is a test to Test the test
OUTPUT: {"test":3, "is":1, "a":1, "to":1, "the":1, "this":1}

'''

# Write a program to build a word histogram

# input

text = input("Enter the text: ")


# process

# 1 convert the text to lower case
text = text.lower()

# 2 split the text into words
words = text.split()
print(words)

# 3 find the unique set of words
uwords = set(words)
print(uwords)

# 4 build a dictionary
whist = {}
for word in uwords:
    whist[word] = words.count(word)


# output
print(whist)

template = "| {0:15} | {1:5} |"
line = '-'*27

print(line)
print(template.format("WORD", "COUNT"))
print(line)
for key in whist.keys():
    print(template.format(key, str(whist[key])))
print(line)

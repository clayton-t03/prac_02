"""
Word Occurences
Estimate: 30
Actual: 45
"""

word_to_count = {}  # initialise empty dictionary
user_string = input("Enter a string: ")
words = user_string.split()  # convert string to list

for word in words:
    occurrence = word_to_count.get(word, 0) #adding words to dictionary as a key
    word_to_count[word] = occurrence + 1  # adds occurence to each word as a value in dictionary

words = list(word_to_count.keys()) #puts words so they are only displayed once
words.sort() #sorts words by alphabetical order

max_length = max(len(word) for word in words)

for word in words:
    print(f"{word:{max_length}} = {word_to_count[word]}")

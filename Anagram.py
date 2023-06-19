
word = input("Enter original: ")
key = input("Enter word to compare: ")

num = 0

for digit in key:
    if digit in word:
        num += 1

if num == len(word):
    print("is anagram")
else:
    print("not an anagram")







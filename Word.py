# cook your dish here
word = input()
countU = sum(1 for i in word if i.isupper())
countL = sum(1 for i in word if i.islower())
if countU > countL:
    print(word.upper())
else:
    print(word.lower())

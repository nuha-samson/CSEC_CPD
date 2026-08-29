# cook your dish here
word = input().strip()
word = word.lower()

for i in word:
    if i in 'aeiouy':
        word= word.replace(i, "")
new = '.' + '.'.join(word)
print(new)

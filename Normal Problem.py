# cook your dish here
n = int(input())
for i in range(n):
    word = input()
    reverser = word[::-1]
    if 'p' not in reverser:
        print(reverser.replace('q','p'))
    elif 'q' not in reverser:
        print(reverser.replace('p','q'))
    elif 'p' and 'q' in reverser:
        change = reverser.maketrans({"p": "q", "q": "p"})
        result  = reverser.translate(change)
        print(result)

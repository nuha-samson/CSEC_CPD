# cook your dish here
n = input()
current = 0
count = 0
for i in n:
    change = ord(i) - ord('a')
    CW = abs(change - current)
    ACw = 26-CW
    if CW < ACw:
        count += CW
    else:
        count += ACw
    current = change
print(count)

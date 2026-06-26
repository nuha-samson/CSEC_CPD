n = int(input())
lst = list(map(int,input().split()))
zero = lst.count(0)
five = lst.count(5)
if zero == 0:
    print(-1)
else:
    five = five - (five % 9)
    if five == 0:
        print(0)
    else:
        print("5"*five + "0"*zero)

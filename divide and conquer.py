t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if x % y == 0:
        print("yes")
    else:
        print("no")

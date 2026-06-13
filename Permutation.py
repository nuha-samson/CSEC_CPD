# cook your dish here
n = int(input())
 
if n % 2 == 1:
    print(-1)
else:
    p = list(range(1, n + 1))
 
    for i in range(0, n, 2):
        p[i], p[i + 1] = p[i + 1], p[i]
 
    print(*p)

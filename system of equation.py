n, m = map(int,input().split())
count = 0
for a in range(n + 1):
    b = n - a * a
    if b >= 0 and a + b * b == m:
        count += 1
print(count)

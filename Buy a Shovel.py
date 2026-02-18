a, b = map(int, input().split())
n = 1
while True:
    total = n * a
    if total % 10 == 0 or total % 10 == b:
        break
    n += 1
print(n)

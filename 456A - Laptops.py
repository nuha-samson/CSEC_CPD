n = int(input())
found = False

for _ in range(n):
    a, b = map(int, input().split())
    if a != b:
        found = True

if found:
    print("Happy Alex")
else:
    print("Poor Alex")

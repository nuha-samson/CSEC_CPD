# cook your dish here
n = int(input())
stops = [tuple(map(int, input().split())) for _ in range(n)]

max_capacity = 0
for i in range(n):
    current = 0
    for j in range(i + 1):
        current = current - stops[j][0] + stops[j][1]
    max_capacity = max(max_capacity, current)

print(max_capacity)

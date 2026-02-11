# cook your dish here
a, b = map(int, input().split())
lst = list(map(int, input().split()))
count = 0
for i in range(a):
    if lst[i]<= b:
        count += 1
    else:
        count += 2
print(count)

# cook your dish here
n = int(input())
lst = list(map(int, input().split()))
count = 0
add = 0
lst.sort(reverse = True)
for i in lst:
    add += i
    if sum(lst) < n:
        print(-1)
        break
    if n == 0:
        count = 0
        print(count)
        break
    elif n > add:
        count += 1
    elif n <= add:
        count += 1
        print(count)
        break

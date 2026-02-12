# cook your dish here
n = int(input())
count = 0
for i in range(n):
    lst = list(map(int, input().split()))
    count1 = sum(1 for i in lst if  i == 1)
    if count1 >= 2:
        count += 1
print(count)

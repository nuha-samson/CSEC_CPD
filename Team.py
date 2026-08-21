# cook your dish here
n = int(input())
count = 0
for i in range(n):
    lst = list(map(int,input().split()))
    add = sum(lst)
    if add >= 2:
        count += 1
print(count)
    
    
    

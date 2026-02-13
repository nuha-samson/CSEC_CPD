# cook your dish here
n = int(input())
lst = list(map(int,input().split()))
police = 0
untreated = 0
for i in range(n):
    if lst[i] > 0:
        police += lst[i]
    elif lst[i] < 0 and police == 0:
        untreated += abs(lst[i])
    elif police > 0 and lst[i] < 0:
        add = police + lst[i]
        if add >= 0:
            police += lst[i]
            continue
        else:
            untreated += abs(add)
    
        
print(untreated)

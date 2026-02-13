# cook your dish here
n = int(input())
lst = list(map(int, input().split()))
s = 0
d = 0
for i in range(n):
    if len(lst) == 1 and i%2 == 0:
        s += lst[0]
    elif len(lst) == 1 and i%2 != 0:
        d += lst[0]
    elif lst[0] > lst[-1] and i%2 == 0:
        s+= lst.pop(0)
    elif lst[0] < lst[-1] and i%2 == 0:
        s += lst.pop()
    elif lst[0] < lst[-1] and i%2 != 0:
        d += lst.pop()
    elif lst[0] > lst[-1] and i%2 != 0:
        d += lst.pop(0)
print(s,d)
        
        
        

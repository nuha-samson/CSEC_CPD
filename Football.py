# cook your dish here
n = int(input())
lst = {}
for i in range(n):
    t = input()
    if t not in lst:
        lst[t] = 1
    else:
        lst[t] += 1
 
print(max(lst, key=lst.get))

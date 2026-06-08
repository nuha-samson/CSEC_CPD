n = int(input())
lst = list(map(int, input().split()))
 
big_index = lst.index(max(lst))
 
bucket = []
mn = min(lst)
 
for i in range(n):
    if lst[i] == mn:
        bucket.append(i)
 
small_index = bucket[-1] 
 
ans = big_index + (n - 1 - small_index)
 
if big_index > small_index:
    ans -= 1
 
print(ans)

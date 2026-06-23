n = int(input())
lst = list(map(int, input().split()))
min_diff = float('inf')
ans = (0, 1)
    
for i in range(n):
  j = (i + 1) % n
  diff = abs(lst[i] - lst[j])
  if diff < min_diff:
    min_diff = diff
    ans = (i, j)
print(ans[0]+1, ans[1]+1)

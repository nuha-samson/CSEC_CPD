# cook your dish here
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
max_diff = 0
count = 0
for i in range(n):
    for j in range(m):
        diff = b[j] / a[i]
        if diff == int(diff): 
            if diff > max_diff:
                max_diff = diff
                count = 1
            elif diff == max_diff:
                count += 1
print(count)

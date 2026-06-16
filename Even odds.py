# cook your dish here
n, m = map(int, input().split())
odd = (n + 1) // 2
if m <= odd:
    print(2*m - 1)
else:
    m -= odd
    print(2*m)

n = int(input())
v = list(map(int, input().split()))

# prefix for original array
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + v[i]

# sorted array
v.sort()

# prefix for sorted array
sorted_prefix = [0] * (n + 1)

for i in range(n):
    sorted_prefix[i + 1] = sorted_prefix[i] + v[i]


m = int(input())

for _ in range(m):
    t, l, r = map(int, input().split())

    if t == 1:
        # original order
        print(prefix[r] - prefix[l - 1])
    else:
        # sorted order
        print(sorted_prefix[r] - sorted_prefix[l - 1])

import math
n = int(input())
lst = list(map(int, input().split()))
c1 = lst.count(1)
c2 = lst.count(2)
c3 = lst.count(3)
c4 = lst.count(4)
taxis = c4
taxis += c3
c1 = max(0, c1 - c3)
taxis += c2 // 2
if c2 % 2 != 0:
    taxis += 1
    c1 = max(0, c1 - 2)
if c1 > 0:
    taxis += math.ceil(c1 / 4)
print(taxis)

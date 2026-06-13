# cook your dish here
n = int(input())
r = []
l = []
for i in range(n):
    m = list(map(str,input().split()))
    l.append(m[0])
    r.append(m[1])
countR0 = r.count('0')
countR1 = r.count('1')
countL0 = l.count('0')
countL1 = l.count('1')
add = min(countL1,countL0)
addR = min(countR1,countR0)
print(add+addR)

# cook your dish here
n = int(input())
home = []
guest = []
same = 0
for i in range(n):
    a, b = map(int, input().split())
    home.append(a)
    guest.append(b)
for i in range(len(home)):
    if home[i] in guest:
        count = sum(1 for j in guest if j == home[i])
        same += count
print(same)
        

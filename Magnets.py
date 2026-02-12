# cook your dish here
n = int(input())
magnet = []
for i in range(n):
    mag = input()
    magnet.append(mag)
group = 1

for j in range(len(magnet)-1):
    if magnet[j] == magnet[j+1]:
        continue
    else:
        group += 1
if len(magnet)==1:
    group = 1
print(group)

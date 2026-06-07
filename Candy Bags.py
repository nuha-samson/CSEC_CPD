# cook your dish here
n = int(input())
lt = 1
rt = n * n
for i in range(n):
    bags = []
    for j in range(n // 2):
        bags.append(str(lt))
        bags.append(str(rt))
        lt += 1
        rt -= 1
    print(" ".join(bags))
 

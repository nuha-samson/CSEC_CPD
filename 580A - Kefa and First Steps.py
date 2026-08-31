# cook your dish here
n = int(input())
days = list(map(int,input().split()))
if len(days) == 1:
    print(1)
else:
    count = 1
    max_count = 1
    for i in range(1,len(days)):
        if days[i] >= days [i-1]:
            count += 1
            max_count = max(max_count,count)
        else:
            count = 1
    print(max_count)

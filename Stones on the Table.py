# cook your dish here
n = int(input())
lst = input()
count = 0
if n == 1:
    print(0)
else:
    for i in range(n-1):
        if lst[i] != lst[i+1]:
            continue
        else:
            count+=1
    print(count)        
        

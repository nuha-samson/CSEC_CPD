# cook your dish here
a, b = map(int, input().split())
die = [1, 2, 3, 4, 5, 6]
count = 0
max_value = max(a, b)
for i in die:
    if i >= max_value:
        count += 1
        
if count == 0:
    print('0/1')
elif count == 1:
    print('1/6')
elif count == 2:
    print('1/3')
elif count == 3:
    print('1/2')
elif count == 4:
    print('2/3')
elif count == 5:
    print('5/6')
elif count == 6:
    print('1/1')

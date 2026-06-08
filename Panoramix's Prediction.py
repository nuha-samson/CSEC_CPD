# cook your dish here
n,m = map(int,input().split())
lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
if n in lst and m in lst:
    if lst.index(n) == lst.index(m)-1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

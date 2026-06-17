# cook your dish here
n = int(input())
for i in range(2*n+1):
    if i < (2*n+1)//2:
        spaces = n - i
        print("  " * spaces, end="")
        for j in range(i+1):
            print(j, end=" ")
        for j in range(i-1, -1, -1):
            print(j, end="")
            
    elif i == (2*n+1)//2:
        for j in range(n+1):
            print(j, end=" ")
        for j in range(n-1, -1, -1):
            print(j, end="")

    else:
        spaces = i - n
        print("  " * spaces, end="")
        count = 2*n - i
        for j in range(count+1):
            print(j, end=" ")
        for j in range(count-1, -1, -1):
            print(j, end="")

    print()

# cook your dish here
grid = [list(map(int, input().split())) for i in range(3)]
 
for i in range(3):
    row = ""
    for j in range(3):
        presses = grid[i][j]
 
        if i > 0:
            presses += grid[i - 1][j]
        if i < 2:
            presses += grid[i + 1][j]
        if j > 0:
            presses += grid[i][j - 1]
        if j < 2:
            presses += grid[i][j + 1]
 
        row += "1" if presses % 2 == 0 else "0"
 
    print(row)
    

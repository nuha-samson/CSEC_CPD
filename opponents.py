n, d = map(int, input().split())
max_win = 0
current_win = 0
for i in range(d):
    s = input().strip()
    if '0' in s:  
        current_win += 1
        if current_win > max_win:
            max_win = current_win
    else:  
        current_win = 0
print(max_win)

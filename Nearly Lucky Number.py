n = input()
c = n.count('4') + n.count('7')
print('YES' if set(str(c)) <= {'4', '7'} else 'NO')

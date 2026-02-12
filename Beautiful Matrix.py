# cook your dish here
matrix = []
move = 0
for i in range(5):
    lst = list(map(int, input().split()))
    if 1 in lst:
        column = abs(2-lst.index(1))
        lst[lst.index(1)] = 0
        lst[2] = 1
        move += column
    matrix.append(lst)

for j in range(len(matrix)):
    if matrix[j] == [0, 0, 1, 0, 0]:
        row = abs(2 - matrix.index(matrix[j]))
        move += row
print(move)

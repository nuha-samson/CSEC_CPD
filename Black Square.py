# cook your dish here
a, b, c, d = map(int, input().split())
strips = input()
count1 = sum(1 for i in strips if i == '1')
count2 = sum(1 for i in strips if i == '2')
count3 = sum(1 for i in strips if i == '3')
count4 = sum(1 for i in strips if i == '4')
print(count1*a + count2*b + count3*c + count4 * d)

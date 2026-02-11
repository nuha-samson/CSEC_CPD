# cook your dish here
n = int(input())
played = input()
countD = sum(1 for i in played if i == 'D')
countA = sum(1 for i in played if i == 'A')
if countA > countD:
    print('Anton')
elif countD > countA:
    print('Danik')
else:
    print('Friendship')

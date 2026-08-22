# cook your dish here
n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
add = sum(coins)
sume = 0
count = 0
for i in coins:
    sume += i
    count += 1
    if sume > add - sume:
        break
print(count)

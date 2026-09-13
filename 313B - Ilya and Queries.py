# cook your dish here
s = input()
m = int(input())
pref = [0] * (len(s)+1)
for i in range(1,len(s)):
    pref[i+1] = pref[i] + (1 if s[i-1] == s[i] else 0)
for i in range(m):
    l,r = map(int,input().split())
    print(pref[r]-pref[l])

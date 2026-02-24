# cook your dish here
s =input()
t = input()
count = 0
for i in t:
    if s[count] == i:
        count += 1
print(count+1)

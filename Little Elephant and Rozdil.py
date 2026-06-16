# cook your dish here
n = int(input())
lst = list(map(int, input().split()))
s = min(lst)
print(lst.index(s)+1 if lst.count(s) == 1 else "Still Rozdil")

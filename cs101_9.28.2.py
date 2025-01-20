s = input()
s += s[-1]
list_s = [0 for _ in range(len(s))]
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        list_s[i+1] = list_s[i] + 1
    else:
        list_s[i+1] = list_s[i]
m = int(input())
for i in range(m):
    l,r = map(int,input().split())
    k = list_s[r-1] - list_s[l-1]
    print(k)

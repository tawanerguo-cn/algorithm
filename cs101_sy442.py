n, m = map(int,input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
s.sort()
t.sort()
pair = 0
l = 0
for i in range(n):
    for j in range(l, m):
        if t[j] >= s[i]:
            pair += 1
            l = j + 1
            break
print(pair)
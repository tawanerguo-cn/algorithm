n = int(input())
a = list(map(int,input().split()))
k = int(input())
m = 0
for i in range(n):
    if k - a[i] in a[i+1:]:
        m += 1
print(m)
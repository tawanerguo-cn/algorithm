n = int(input())
v = list(map(int,input().split()))
v1 = sorted(v)
sum_v = [0 for _ in range(n+1)]
sum_v1 = [0 for _ in range(n+1)]
for i in range(n):
    sum_v[i] = sum_v[i-1] + v[i]
    sum_v1[i] = sum_v1[i-1] + v1[i]
m = int(input())
for _ in range(m):
    type,l,r = map(int,input().split())
    if type == 1:
        print(sum_v[r-1] - sum_v[l-2])
    if type == 2:
        print(sum_v1[r-1] - sum_v1[l-2])
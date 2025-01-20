n,m = map(int,input().split())
r = list(map(int,input().split()))
r.sort()
rm = [r[i+1] - r[i] for i in range(n - 1)]
rm.sort()
print(sum(rm[:n-m]))
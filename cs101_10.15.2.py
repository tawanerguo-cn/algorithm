import bisect
n = int(input())
x = list(map(int, input().split()))
q = int(input())
m = []
for i in range(q):
    mi = int(input())
    m.append(mi)
x.sort()
for i in m:
    a = bisect.bisect(x, i)
    print(a)
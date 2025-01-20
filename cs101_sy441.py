n, w0 = map(int, input().split())
w = list(map(int,input().split()))
w.sort()
w1 = 0
m = 0
for i in range(n):
    if w1 + w[i] <= w0:
        w1 += w[i]
    else:
        m = i
        break
print(m, w1)
n = int(input())
tree = []
for _ in range(n):
    xi, hi = map(int, input().split())
    tree.append([xi, hi])
if n == 1:
    print(1)
    exit()
m = 2
p = tree[0][0]
for i in range(1, n - 1):
    x, h = tree[i]
    if x - h > p:
        m += 1
        p = x
    elif x + h < tree[i+1][0]:
        m += 1
        p = x + h
    else:
        p = x
print(m)

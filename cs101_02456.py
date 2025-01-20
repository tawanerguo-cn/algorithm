n, c = map(int, input().split())
x = []
for _ in range(n):
    xi = int(input())
    x.append(xi)
x.sort()
def is_feasible(x, n, c, d):
    count = 1
    last_pos = x[0]
    for i in range(1, n):
        if x[i] - last_pos >= d:
            count += 1
            last_pos = x[i]
            if count == c:
                return True
    return False
l, r = 1, x[-1] - x[0]
result = 0
while l <= r:
    mid = (l + r) // 2
    if is_feasible(x, n, c, mid):
        result = mid
        l = mid + 1
    else:
        r = mid - 1
print(result)
l, n, m = map(int, input().split())
d = [0]
for _ in range(n):
    di = int(input())
    d.append(di)
d.append(l)
def is_feasible(d, m, n, length):
    last_pos = d[0]
    count_pass = 0
    for i in range(1, n + 2):
        if d[i] - last_pos < length:
            count_pass += 1
            if count_pass > m:
                return False
        else:
            last_pos = d[i]
    return True
left = 0
right = l
result = 0
while left <= right:
    mid = (left + right) // 2
    if is_feasible(d, m, n, mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)
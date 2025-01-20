n, a, b = map(int,input().split())
w = list(map(int,input().split()))
wa = a; wb = b
count = 0
if n % 2 == 0:
    for i in range(n // 2):
        if wa >= w[i]:
            wa -= w[i]
        else:
            count += 1
            wa = a - w[i]
    for j in range(n - 1, n // 2 - 1, -1):
        if wb >= w[j]:
            wb -= w[j]
        else:
            count += 1
            wb = b - w[j]
else:
    for i in range((n - 1) // 2):
        if wa >= w[i]:
            wa -= w[i]
        else:
            count += 1
            wa = a - w[i]
    for j in range(n - 1, (n - 1) // 2, -1):
        if wb >= w[j]:
            wb -= w[j]
        else:
            count += 1
            wb = b - w[j]
    if w[(n - 1) // 2] > max(wa, wb):
        count += 1
print(count)
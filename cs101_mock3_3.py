n, k = map(int, input().split())
t = list(map(int, input().split()))
t.sort()
while True:
    if t[-1] > sum(t) / k:
        t.pop()
        k -= 1
    else:
        print(f'{sum(t) / k :.3f}')
        break
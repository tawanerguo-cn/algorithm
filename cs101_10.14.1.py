while True:
    r,n = map(int,input().split())
    if r == -1:
        break
    x = list(set(list(map(int,input().split()))))
    x.sort()
    i = 0
    t = 0
    while i < len(x):
        start = x[i]
        i += 1
        while i < len(x) and x[i] <= start + r:
            i += 1
        tp = x[i-1]
        t += 1
        while i < len(x) and x[i] <= tp + r:
            i += 1
    print(t)
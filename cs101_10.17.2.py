q = int(input())
for _ in range(q):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort(reverse = True)
    b = False
    for i in range(n):
        sum_s = 0
        a = False
        for j in range(i, n):
            sum_s += s[j]
            if sum_s == 2048:
                print('YES')
                a = True
                b = True
                break
        if a:
            break
    if not b:
        print('NO')
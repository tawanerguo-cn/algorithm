k = int(input())
for _ in range(k):
    n = int(input())
    p = []
    for _ in range(n):
        si, di = map(int, input().split())
        p.append([si, di])
    p.sort(key=lambda x: (x[1], x[0]))
    test_count = 0
    last_test_time = -1
    for start, end in p:
        if start > last_test_time:
            last_test_time = end
            test_count += 1
    print(test_count)

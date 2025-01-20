n = int(input())
for _ in range(n):
    s = int(input())
    a0 = int(input())
    a = list(map(int,input().split())).sort()
    b0 = int(input())
    b = list(map(int,input().split())).sort()
    pair = 0
    for i in range(a0):
        for j in range(b0):
            if a[i] + b[j] == s:
                pair += 1
    print(pair)
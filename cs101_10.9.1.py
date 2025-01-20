count = 1
while True:
    p,e,i,d = map(int,input().split())
    if [p,e,i,d] == [-1,-1,-1,-1]:
        break
    p = p % 23;e = e % 28;i = i % 33
    m = 21252
    for k in range(d + 1,d + m + 1):
        if (k-p) % 23 == 0 and (k - e) % 28 == 0 and (k - i) % 33 == 0:
            print(f'Case {count}: the next triple peak occurs in {k - d} days.')
            break
    count += 1
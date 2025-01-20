while True:
    o = list(map(int,input().split()))
    if o.count(0) == 6:
        break
    t = 0
    t += o[5]
    t += o[4]
    o[0] = max(0,o[0] - 11 * o[4])
    t += o[3]
    mid1 = o[1]
    o[1] = max(0,o[1] - 5 * o[3])
    if o[1] == 0:
        o[0] = max(0,o[0] - (20 * o[3] - 4 * mid1))
    t += o[2] // 4
    if o[2] % 4 != 0:
        o[1] = max(0,o[1] - (7 - 2 * (o[2] % 4)))
        o[0] = max(0,o[0] - (8 - o[2] % 4))
        t += 1
    t += o[1] // 9
    if o[1] % 9 != 0:
        o[0] = max(0,o[0] - (36 - 4 * (o[1] % 9)))
        t += 1
    t += o[0] // 36
    if o[0] % 36 != 0:
        t += 1
    print(t)
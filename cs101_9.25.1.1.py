while True:
    try:
        o = list(map(int,input().split()))
        if o.count(0) != len(o):
            n = o[5] + o[4]
            o[0] = max(0,o[0] - 11 * o[4])
            n += o[3]
            if 5 * o[3] >= o[1]:
                o[1] = 0
                o[0] = max(0,o[0] - 20 * o[3] + 4 * o[1])
            else:
                o[1] -= 5 * o[3]
            n += o[2] // 4 + o[1] // 9 + o[0] // 36
            o[2] = o[2] % 4
            o[1] = o[1] % 9
            o[0] = o[0] % 36
            if o[2] == 0:
                n += -(-((4*o[1] + o[0])/36) // 1)
            else:
                n += 1
                o[1] = max(0,o[1] - 7 - 2 * o[2])
                o[0] = max(0,o[1] - 8 - o[2])
                n += -(-((4*o[1] + o[0])/36) // 1)
            print(int(n))
    except EOFError:
        break
#贪心就要一步一步来，按次序依次加上去，不能乱来
while True:
    n,p,m = map(int,input().split())
    if n == 0:
        break
    kid = [(i + p - 1)%n + 1 for i in range(n)]
    kill = []
#自然的顺序处理思路：从头开始报数，如果不是mI就放到最后，如果是就删掉
    i = 1
    while len(kid) > 0:
        if i != m:
            kid.append(kid[0])
            kid.pop(0)
            i += 1
        else:
            kill.append(kid[0])
            kid.pop(0)
            i = 1
    print(','.join(str(i) for i in kill))
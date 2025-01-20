n,w = map(int,input().split())
candy = []
for _ in range(n):
    v1,w1 = map(int,input().split())
    v_w = v1 / w1
    candy.append([v1,w1,v_w])
candy.sort(key = lambda x:x[2],reverse = True)
jiazhi = 0
for i in range(n):
    if candy[i][1] <= w:
        jiazhi += candy[i][0]
        w -= candy[i][1]
    else:
        jiazhi += candy[i][2] * w
        break
print(f'{jiazhi:.1f}')
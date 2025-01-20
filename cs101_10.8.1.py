n = int(input())
print((3 * n) // 5 * 5)
#不能直接这么写的原因：对每个a都有限制，所以就是得暴力
m=0
for i in range(n, -1, -1):
    for j in range(n, -1, -1):
        for k in range(n, -1, -1):
            if (i + j) % 2 == 0 and (j + k) % 3 == 0 and (i + j + k) % 5 == 0:
                m=max(m,i+j+k)#递推，避免多写一轮
print(m)
from itertools import permutations
n = int(input())
m = 8
def m_queen(m):
    list_m = list(permutations(range(m)))#这天然只用检查对角线
    output = []
    for perm in list_m:
        a = True
        for i in range(m):
            for j in range(i + 1,m):
                if abs(i-j) == abs(perm[i] - perm[j]):#检查任意两个是否在同一条对角线上
                    a = False
                    break
            if not a:
                break
        if a:
            output.append(perm)
    return output
output = m_queen(m)
for _ in range(n):
    k1 = int(input())
    print(''.join(str(output[k1 - 1][j] + 1) for j in range(8)))
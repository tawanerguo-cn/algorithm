p = int(input())
p1 = list(map(int,input().split()))
p1.sort()
m = 0
i = 0
j = len(p1) - 1
while i != j:
    if p >= p1[i]:
        m += 1
        p -= p1[i]
        i += 1
    elif p < p1[i]:
        m -= 1
        if m == -1:
            print(0)
            exit()
        p += p1[j]
        j -= 1
if p >= p1[i]:
    m += 1
print(m)
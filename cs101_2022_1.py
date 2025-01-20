#25538, 25580, 25572, 25573, 25566, 25570
n = int(input())
bi_n = []
while n != 0:
    a = n % 2
    bi_n.append(a)
    n = n // 2
n0 = len(bi_n)
a = True
if n0 % 2 == 0:
    for i in range(n0 // 2):
        if bi_n[i] != bi_n[n0 - 1 - i]:
            a = False
            break
elif n0 % 2 == 1:
    for i in range((n0 - 1) // 2):
        if bi_n[i] != bi_n[n0 - 1 - i]:
            a = False
            break
if a:
    print('Yes')
else:
    print('No')
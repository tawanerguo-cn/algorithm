n = int(input())
def pell():
    pell = []
    pell.append(1)
    pell.append(2)
    for i in range(2,1000000+1):
        pell.append((2 * pell[i-1] + pell[i-2]) % 32767)
    return pell
pell_list = pell()
for _ in range(n):
    m = int(input())
    print(pell_list[m-1])

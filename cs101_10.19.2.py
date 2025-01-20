letter  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['1','2','3','4','5','6','7','8','9','0']
def aaa_to_rc(m):
    col = []
    row = []
    for i in m:
        if i in letter:
            col.append(letter.index(i) + 1)
        elif i in number:
            row.append(i)
    row1 = int(''.join(i for i in row))
    col1 = 0
    l1 = len(col)
    for i in range(l1):
        col1 += 26 ** (l1 - 1 - i) * col[i]
    ans = ['R', str(row1), 'C', str(col1)]
    ans1 = ''.join(i for i in ans)
    return ans1
def rc_to_aaa(m):
    div = m.index('C')
    row = m[1: div]
    col = int(m[div + 1:])
    col1 = []
    while col != 0:
        b = col % 26
        col1.append(letter[b - 1])
        if b != 0:
            col = col // 26
        elif b == 0:
            col = col // 26 - 1
    col1.reverse()
    ans = [''.join(i for i in col1), row]
    ans1 = ''.join(i for i in ans)
    return ans1
n = int(input())
for i in range(n):
    m = input()
    l = len(m)
    a = True
    for i in range(l - 1):
        if m[i] in number and m[i + 1] in letter:
            print(rc_to_aaa(m))
            a = False
            break
    if a:
        print(aaa_to_rc(m))
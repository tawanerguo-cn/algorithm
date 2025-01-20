import math
s = input()
n = len(s)
m = math.floor(math.log2(n))
code_l = [s[2 ** (i) - 1] for i in range(m + 1)]
code = []
for i in range(m + 1):
    if i % 2 == 0:
        code.append(code_l[i // 2])
    else:
        code.append(code_l[m - i // 2])
print(''.join(i for i in code))
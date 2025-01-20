k = int(input())
k = k % 26
code = [i for i in input()]
for i in range(len(code)):
    if (ord(code[i]) >= 65 + k and ord(code[i]) <= 90) or ord(code[i]) >= 97 + k:
        code[i] = chr(ord(code[i]) - k)
    else:
        code[i] = chr(ord(code[i]) + 26 - k)
print(''.join(i for i in code))
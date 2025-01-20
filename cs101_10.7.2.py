n = int(input())
string_list = []
for _ in range(n):
    string_list.append(input())
len_list = [len(i) for i in string_list]
output = []
b = True
for j in range(min(len_list)):
    a = True
    for i in range(n-1):
        if string_list[i][j] != string_list[i+1][j]:
            a = False
            b = False
            break
    if a:
        output.append(string_list[0][j])
    if not b:
        break
print(''.join(i for i in output))
a,b = map(int,input().split())
ab = True
list_output = []
for i in range(a,b + 1):
    list_number = [int(j) for j in str(i)]
    m = 0
    for j in list_number:
        m += j ** 3
    if m == i:
        list_output.append(i)
if len(list_output) == 0:
    print('NO')
else:
    print(' '.join(str(i) for i in list_output))
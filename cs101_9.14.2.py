n = int(input())
list_cood = [[] for _ in range(3)]
for _ in range(n):
    list_input = list(map(int,input().split()))
    for i in range(3):
        list_cood[i].append(list_input[i])
if sum(list_cood[0]) == 0 and sum(list_cood[1]) == 0 and sum(list_cood[2]) == 0:
    print('YES')
else:
    print('NO')
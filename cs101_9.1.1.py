t = int(input())
for i in range(t):
    list_test = list(map(int,input().split()))
    list_sorted = sorted(list_test)
    if list_sorted[2] == list_sorted[0] + list_sorted[1]:
        print('YES')
    else:
        print('NO')

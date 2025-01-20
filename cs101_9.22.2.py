n = int(input())
array = list(map(int,input().split()))
a = True
for i in range(n - 1):
    if array[i] > array[i + 1]:
        print('NO')
        a = False
        break
if a:
    print('YES')
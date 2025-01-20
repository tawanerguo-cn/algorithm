n = int(input())
list_number = list(map(int,input().split()))
list_evenness = [0 for _ in range(n)]
for i in range(n):
    if list_number[i] % 2 == 0:
        list_evenness[i] = 1
    else:
        list_evenness[i] = -1
if list_evenness.count(1) == 1:
    print(list_evenness.index(1)+1)
else:
    print(list_evenness.index(-1)+1)
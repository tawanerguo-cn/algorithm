n = int(input())
list_a = list(map(int,input().split()))
list_a.append(-1)
list_increase = []
a = 1
for i in range(n):
    if list_a[i] <= list_a[i+1]:
        a += 1
    else:
        list_increase.append(a)
        a = 1
print(max(list_increase))
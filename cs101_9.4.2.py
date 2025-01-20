n = int(input())
list_values = list(map(int,input().split()))
list_sorted = sorted(list_values,reverse=True)
values = sum(list_sorted)
sum_values = 0
for i in range(n):
    sum_values += list_sorted[i]
    if 2*sum_values > values:
        print(i+1)
        break

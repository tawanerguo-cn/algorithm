n,m = map(int,input().split())
list_ai = list(map(int,input().split()))
list_sorted = sorted(list_ai)
negative_number = 0
if list_sorted[n-1] < 0:
    negative_number = n
for i in range(n-1):
    if list_sorted[i+1] >= 0 and list_sorted[i] < 0:
        negative_number = i+1
        break
print(abs(sum(list_sorted[0:min(negative_number,m)])))
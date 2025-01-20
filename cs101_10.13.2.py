n,k = map(int,input().split())
a = list(map(int,input().split()))
m = 0
i = 0
j = n - 1
while i < j:
    if a[i] + a[j] > k:
        j -= 1
    elif a[i] + a[j] == k:
        m += 1
        i += 1
    elif a[i] + a[j] < k:
        i += 1
print(m)
a = list(map(int,input().split()))
n = len(a)
raise1 = [[0,a[0]]]
for i in range(1, n):
    if a[i] >= raise1[-1][1]:
        if a[i]- raise1[-1][1] > raise1[-1][0]:
            raise1[-1][0]  = a[i]- raise1[-1][1]
    else:
        raise1.append([0,a[i]])
raise1.sort(key = lambda x:x[0], reverse = True)
print(raise1[0][0])
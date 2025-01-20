n,m,k = map(int,input().split())
a = [[0 for i in range(m + 2)] for j in range(n + 2)]
b = True
for _ in range(k):
    n1,m1 = map(int,input().split())
    a[n1][m1] = 1
    if a[n1-1][m1-1] == 1 and a[n1][m1-1] == 1 and a[n1-1][m1] == 1:
        print(_ + 1)
        b = False
        break
    elif a[n1+1][m1-1] == 1 and a[n1][m1-1] == 1 and a[n1+1][m1] == 1:
        print(_ + 1)
        b = False
        break
    elif a[n1+1][m1+1] == 1 and a[n1][m1+1] == 1 and a[n1+1][m1] == 1:
        print(_ + 1)
        b = False
        break
    elif a[n1-1][m1+1] == 1 and a[n1][m1+1] == 1 and a[n1-1][m1] == 1:
        print(_ + 1)
        b = False
        break
if b:
    print(0)
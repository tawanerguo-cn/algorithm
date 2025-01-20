t=int(input())
for i in range(t):
    n=int(input())
    if n%2==0:
        print(n//2-1)
    if n%2!=0:
        print((n-1)//2)
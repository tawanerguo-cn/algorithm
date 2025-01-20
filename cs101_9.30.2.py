n = int(input())
boy = sorted(list(map(int,input().split())))
m = int(input())
girl = sorted(list(map(int,input().split())))
if n > m:
    boy,girl = girl,boy
    n,m = m,n
pair = 0
for i in range(n):
    a = False
    for j in range(len(girl)):
        if abs(boy[0] - girl[j]) <= 1:
            pair += 1
            boy.pop(0)
            girl.pop(j)
            a = True
            break
    if not a:
        boy.pop(0)
print(pair)
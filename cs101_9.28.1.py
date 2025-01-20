#看答案……
#思路：通过n-1递推到n个人时应该杀掉哪个人
#f(n,m) = (f(n-1,m) + m) % n
#已知n个人时的胜利者下标，则n-1个人时的胜利者下标向前移动m即可
#理解：每次杀了之后重新分配，下一个人变成了新的0号，则被杀的是m-1，则下一个是m号，在下一轮又变成0号，反推即可
while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    p = 0
    for i in range(2,n + 1):
        p = (p + m) % i
    print(p+1)
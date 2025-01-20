t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    cost_1 = min(a)*n + sum(b)
    cost_2 = min(b)*n +sum(a)
    print(min(cost_1,cost_2))
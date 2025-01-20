t = int(input())
for i in range(t):
    a,k = map(int,input().split())
    forecast = list(map(int,input().split()))
    exact = list(map(int,input().split()))
    for j in range(a):
        forecast[j] = [forecast[j],j]
    forecast.sort(key = lambda x: x[0])
    exact.sort()
    for j in range(a):
        forecast[j] = [forecast[j][0],forecast[j][1],exact[j]]
    forecast.sort(key = lambda x:x[1])
    print(' '.join(str(forecast[k][2]) for k in range(a)))
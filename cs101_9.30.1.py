t = int(input())
for i in range(t):
    l,n = map(int,input().split())
    location = list(map(int,input().split()))
    l_dis = [location[i] for i in range(n)]
    r_dis = [l - location[i] for i in range(n)]
    print(max(min(l_dis[i],r_dis[i]) for i in range(n)),max(max(l_dis),max(r_dis)))
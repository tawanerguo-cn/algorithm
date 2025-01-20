t=int(input())
ab_list=[]
for i in range(t):
    ab_list.append(list(map(int,input().split())))
    if ab_list[i][0]%ab_list[i][1]!=0:
        print(ab_list[i][1]-ab_list[i][0]%ab_list[i][1])
    else:
        print(0)
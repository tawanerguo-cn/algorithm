case = int(input())
for _ in range(case):
    n,m,b = map(int,input().split())
    skill = []
    time = []
    for _ in range(n):
        ti,xi = map(int,input().split())
        time.append(ti)
        skill.append([ti,xi])
    skill.sort(key = lambda x:(x[0],-x[1]))#获得的技能按照时间从小到大排序，对于同一个时间，按照技能值从大到小排序
    skill1 = [skill[0][1]]
    time = sorted(list(set(time)))
    k = 1
    for i in range(1,n):
        if skill[i][0] != skill[i-1][0]:
            k = 1
            skill1.append(skill[i][1])
        elif skill[i][0] == skill[i-1][0] and k < m:
            skill1[-1] += skill[i][1]
            k += 1
    skill1 = [[time[i],skill1[i]] for i in range(len(skill1))]
    a = True
    for i in range(len(skill1)):
        b -= skill1[i][1]
        if b <= 0:
            print(skill1[i][0])
            a = False
            break
    if a:
        print('alive')
n = int(input())
#pop:去除序号
l_list = []
for _ in range(4):
    l_list.append(input())
possible_way1 = [(0)]
possible_way2 = [(0,1),(1,0)]
possible_way3 = [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,1,0),(2,0,1)]
possible_way4 = [(0,1,2,3),(0,1,3,2),(0,2,1,3),(0,2,3,1),(0,3,1,2),(0,3,2,1),
                (1,0,2,3),(1,0,3,2),(1,3,0,2),(1,3,2,0),(1,2,0,3),(1,2,3,0),
                (2,0,1,3),(2,0,3,1),(2,1,3,0),(2,1,0,3),(2,3,1,0),(2,3,0,1),
                (3,0,1,2),(3,0,2,1),(3,1,0,2),(3,1,2,0),(3,2,1,0),(3,2,0,1)]
for _ in range(n):
    l = input()
    n_l = len(l)
    a = False
    if n_l == 1:
        for i in range(4):
            if l[0] in l_list[i]:
                a = True
                break
    elif n_l == 2:
        for i, j in possible_way2:
            if (l[i] in l_list[0] and l[j] in l_list[1]) or (l[i] in l_list[0] and l[j] in l_list[2]) or (l[i] in l_list[0] and l[j] in l_list[3]) or (l[i] in l_list[1] and l[j] in l_list[2]) or (l[i] in l_list[1] and l[j] in l_list[3]) or (l[i] in l_list[2] and l[j] in l_list[3]):
                a = True
                break
    elif n_l == 3:
        for i, j, k in possible_way3:
            if (l[i] in l_list[0] and l[j] in l_list[1] and l[k] in l_list[2]) or (l[i] in l_list[0] and l[j] in l_list[1] and l[k] in l_list[3]) or (l[i] in l_list[0] and l[j] in l_list[2] and l[k] in l_list[3]) or (l[i] in l_list[1] and l[j] in l_list[2] and l[k] in l_list[3]):
                a = True
                break
    elif n_l == 4:
        for i1, i2, i3, i4 in possible_way4:
            if l[i1] in l_list[0] and l[i2] in l_list[1] and l[i3] in l_list[2] and l[i4] in l_list[3]:
                a = True
                break
    if a:
        print('YES')
    else:
        print('NO')
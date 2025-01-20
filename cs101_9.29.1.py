# while True:
#     n = int(input())
#     if n == 0:
#         break
#     hotel = []
#     for _ in range(n):
#         d,c = map(int,input().split())
#         hotel.append([d,c])
#     m = 0
#     for i in range(n):
#         hotel_closer_cost = [hotel[j][1] for j in range(n) if hotel[j][0] < hotel[i][0]]
#         hotel_closer_cost.append(10001)
#         hotel_cheaper_distance = [hotel[j][0] for j in range(n) if hotel[j][1] < hotel[i][1]]
#         hotel_cheaper_distance.append(10001)
#         if min(hotel_cheaper_distance) > hotel[i][0] and min(hotel_closer_cost) > hotel[i][1]:
#             m += 1
#     print(m)
#超时了
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     hotel = []
#     d = []
#     c = []
#     for i in range(n):
#         d1,c1 = map(int,input().split())
#         d.append(d1)
#         c.append(c1)
#         hotel.append([d1,c1])
#     mind = min(d)
#     minc = min(c)
#     hotel_mind = [hotel[i][1] for i in range(n) if hotel[i][0] == min(d)]
#     mind_cost = min(hotel_mind)
#     hotel_minc = [hotel[i][0] for i in range(n) if hotel [i][1] == min(c)]
#     minc_dis = min(hotel_minc)
#     m = 0
#     for i in range(n):
#         if hotel[i][0] <= mind_cost and hotel[i][1] <= minc_dis:
#             m += 1
#     print(m)
# 思路有问题
while True:
    n = int(input())
    if n == 0:
        break
    hotel = [list(map(int,input().split())) for _ in range(n)]
    hotel.sort(key = lambda x:[x[0],x[1]])
    min_cost = hotel[0][1]
    m = 1
    for i in range(n):
        if hotel[i][1] < min_cost:
            m += 1
            min_cost = hotel[i][1]
    print(m)
#最关键的是学会了用lambda排序
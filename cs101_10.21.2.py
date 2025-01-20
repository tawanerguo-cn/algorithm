n, m = map(int, input().split())
a = [0]
a.extend(list(map(int, input().split())))
a.append(m)
sign = 1
on = 0
point_off = []
for i in range(1, n + 2):
    if sign == 1:
        on += a[i] - a[i - 1]
        point_off.append([a[i], on])
    sign *= -1
for i in point_off:
    i[1] = i[1] + (m - i[0] - (on - i[1])) - 1
point_off.sort(key = lambda x:-x[1])
print(max(point_off[0][1], on))

#重要的是某个点后面关灯时间与开灯时间的差值，按照这个排序，找到关-开时间最长的那个
#若在本来亮的时间插入，则应该尽量靠近关灯点
#若在本来暗的时间插入，则也应该尽量靠近关灯点（远离开灯点）
#已知某个关灯点前亮的时间和后面暗的时间，则在这个关灯点前或者后插入没差别
#一定是在关灯点的位置改
#在可以插入时，关灯点插入后新的亮的时间是关灯点前亮的时间+关灯点后暗的时间-1
#已知总开灯时间，某点前的开灯时间，某点后的关灯时间，按照开灯+关灯时间排序即可
#最终结果是开灯时间+关灯时间-1的最大值
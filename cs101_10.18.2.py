t = int(input())
results = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 将 a[i] 和 b[i] 按 a[i] 降序排序
    dishes = sorted(zip(a, b), key=lambda x: x[0], reverse=True)

    # 初始化累计自取时间和最大快递时间
    total_pickup_time = 0
    max_delivery_time = max(a)
    min_time = max_delivery_time

    for i in range(n):
        # 当前菜品切换为自取
        total_pickup_time += dishes[i][1]

        # 更新最大快递时间
        if i + 1 < n:
            max_delivery_time = dishes[i + 1][0]
        else:
            max_delivery_time = 0

        # 当前策略的最小时间
        current_time = max(total_pickup_time, max_delivery_time)
        min_time = min(min_time, current_time)

    results.append(min_time)

# 输出结果
print("\n".join(map(str, results)))

#理清楚为什么这么写判断：对于排序后的第i+1个，
#若决定自提花费的总时间大于等于这个送的时间，则剩下的都靠送，花的时间是自提与送的最大值
#若自提花费的总时间依然小于送这个的时间，那不如继续送
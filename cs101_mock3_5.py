import itertools

def calculate_total_price(combination, price, sale, n, m):
    # 计算每家店铺的总花费
    shop_totals = [0 for _ in range(m)]
    for item_idx, shop_idx in enumerate(combination):
        shop_totals[shop_idx] += price[item_idx][shop_idx]

    # 应用每家店铺的优惠券
    for shop_idx in range(m):
        if shop_totals[shop_idx] > 0:  # 有消费才计算优惠
            max_discount = 0
            for q, x in sale[shop_idx]:
                if shop_totals[shop_idx] >= q:
                    max_discount = max(max_discount, x)
            shop_totals[shop_idx] -= max_discount

    # 计算跨店满减
    total = sum(shop_totals)
    if total > 0:  # 只有正值时计算满减
        discount = (total // 300) * 50
        total -= discount
    return total

# 输入处理
n, m = map(int, input().split())
price = [[float('inf') for _ in range(m)] for _ in range(n)]  # 初始化价格为无穷大
for j in range(n):
    price_i = list(map(str, input().split()))
    for price_i_s in price_i:
        price_i_s1, price_i_s2 = map(int, price_i_s.split(':'))
        price[j][price_i_s1 - 1] = price_i_s2  # 填入对应店铺的价格

sale = [[] for _ in range(m)]  # 初始化优惠券列表
for i in range(m):
    sale_i = list(map(str, input().split()))
    for j in sale_i:
        q, x = map(int, j.split('-'))
        sale[i].append((q, x))  # 添加优惠券 (满减条件, 减免金额)

# 遍历所有商品购买方案，计算最低价格
min_price = float('inf')
for combination in itertools.product(range(m), repeat=n):
    # 检查是否所有商品的选择都有有效报价
    if all(price[item_idx][shop_idx] < float('inf') for item_idx, shop_idx in enumerate(combination)):
        total_price = calculate_total_price(combination, price, sale, n, m)
        min_price = min(min_price, total_price)

print(min_price)

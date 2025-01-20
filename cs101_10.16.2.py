t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    total_sum = sum(a)
    
    # 如果整个数组的和不能被 x 整除，直接返回 n
    if total_sum % x != 0:
        print(n)
        continue
    
    # 从左边找到第一个不能被 x 整除的位置
    left = -1
    for i in range(n):
        if a[i] % x != 0:
            left = i
            break
    
    # 从右边找到第一个不能被 x 整除的位置
    right = -1
    for i in range(n - 1, -1, -1):
        if a[i] % x != 0:
            right = i
            break
    
    # 如果所有元素都能被 x 整除，返回 -1
    if left == -1 and right == -1:
        print(-1)
    else:
        # 计算去掉左边或右边后的最大长度
        max_length = max(n - left - 1, right)
        print(max_length)

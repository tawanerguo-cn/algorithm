t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pre_sum = 0
    pre_set = set()
    count = 0
    for i in range(n):
        pre_sum += a[i]
        if pre_sum == 0 or pre_sum in pre_set:
            count += 1
            pre_sum = 0
            pre_set.clear()
        else:
            pre_set.add(pre_sum)
        print(i, pre_sum, pre_set, count)
    print(count)
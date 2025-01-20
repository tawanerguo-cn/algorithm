n = int(input())
rows = []
len_row = 0
while True:
    row = list(map(int, input().split()))
    n1 = len(row)
    if not row:
        continue
    rows.extend(row)
    len_row += n1
    if len_row == n ** 2:
        break
mat = [rows[n * i : n * (i + 1)] for i in range(n)]
#抄kadane算法，原始的问题是一维最大子数组
#原始问题可以用动态规划，遍历一遍o(n)解决
#current_sum = max(value, current_sum + value)
#best_sum = max(best_sum, current_sum)
#本质上就是在考虑动态规划加入一个新的数后带这个的最大和与原来的最大和哪个大
#但带这个数的最大和本身也需要动态规划，求到底是单独这个数还是跟前面的接上
max_sum = float('-inf')
for top in range(n):
    temp = [0 for _ in range(n)]
    for bottom in range(top, n):
        for col in range(n):
            temp[col] += mat[bottom][col]
        current_sum = float('-inf')
        best_sum = float('-inf')
        for value in temp:
            current_sum = max(value, current_sum + value)
            best_sum = max(best_sum, current_sum)
        max_sum = max(max_sum, best_sum)
print(max_sum)
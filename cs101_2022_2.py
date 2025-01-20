h, l, n = map(int, input().split())
v = list(map(float, input().split()))
t_arrive = [l / v[i] for i in range(n)]
t_arrive.sort(reverse = True)
t = t_arrive[n // 2]
print(f'{(h - 5 * t ** 2):.2f}')
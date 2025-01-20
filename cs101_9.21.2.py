t = int(input())
list_polygon = [180 - 360 // i for i in range(3,361) if 360 % i == 0]
for _ in range(t):
    a = int(input())
    if a in list_polygon:
        print('YES')
    else:
        print('NO')
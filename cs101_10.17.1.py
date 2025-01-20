a, b, k = map(int, input().split())
bomb = []
for _ in range(k):
    r1, s1, p1, t1 = map(int, input().split())
    bomb.append([r1 - 1, s1 - 1, p1, t1])
mat = [[0 for _ in range(b)] for _ in range(a)]
bomb_count = 0
for i in range(k):
    if bomb[i][3] == 1:
        bomb_count += 1
for i in range(k):
    if bomb[i][3] == 1:
        for j in range(-(bomb[i][2] - 1) // 2, (bomb[i][2] - 1) // 2 + 1):
            for k in range(-(bomb[i][2] - 1) // 2, (bomb[i][2] - 1) // 2 + 1):
                cx, cy = bomb[i][0] + j, bomb[i][1] + k
                if 0 <= cx < a and 0 <= cy < b and mat[cx][cy] != -1:
                    mat[cx][cy] += 1
    elif bomb[i][3] == 0:
        for j in range(-(bomb[i][2] - 1) // 2, (bomb[i][2] - 1) // 2 + 1):
            for k in range(-(bomb[i][2] - 1) // 2, (bomb[i][2] - 1) // 2 + 1):
                cx, cy = bomb[i][0] + j, bomb[i][1] + k
                if 0 <= cx < a and 0 <= cy < b:
                    mat[cx][cy] = -1
field_count = 0
for i in range(a):
    for j in range(b):
        if mat[i][j] == bomb_count:
            field_count += 1
print(field_count)
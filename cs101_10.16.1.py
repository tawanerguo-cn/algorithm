n, m = map(int, input().split())
mat = [[0 for _ in range(m + 2)]]
for _ in range(n):
    row = [0]
    row.extend(list(map(int, input().split())))
    row.append(0)
    mat.append(row)
mat.append([0 for _ in range(m + 2)])
new_mat = [[0 for _ in range(m)] for _ in range(n)]
nei = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if mat[i][j] == 1:
            alive = 0
            for dx, dy in nei:
                cx, cy = i + dx, j + dy
                if mat[cx][cy] == 1:
                    alive += 1
            if alive == 2 or alive == 3:
                new_mat[i - 1][j - 1] = 1
        elif mat[i][j] == 0:
            alive = 0
            for dx, dy in nei:
                cx, cy = i + dx, j + dy
                if mat[cx][cy] == 1:
                    alive += 1
            if alive == 3:
                new_mat[i - 1][j - 1] = 1
for i in new_mat:
    print(' '.join(str(j) for j in i))
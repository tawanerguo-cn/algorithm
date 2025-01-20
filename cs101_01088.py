r, c = map(int, input().split())
height = []
for _ in range(r):
    row = tuple(map(int, input().split()))
    height.append(row)
dp = [[1 for _ in range(c)] for _ in range(r)]
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for i in range(r):
    for j in range(c):
        for dx, dy in dir:
            cx, cy = i + dx, j + dy
            if 0 <= cx < r and 0 <= cy < c and height[cx][cy] < height[i][j]:
                dp[i][j] = max(dp[i][j], dp[cx][cy] + 1)
print(max(max(row) for row in dp))

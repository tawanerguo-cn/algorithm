from collections import deque
index = 0
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while True:
    index += 1
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [[0 for _ in range(w + 2)] for _ in range(h + 2)]
    for i in range(h):
        row = input()
        for j, char in enumerate(row):
            if char == 'X':
                board[i + 1][j + 1] = 1
    test_cases = []
    while True:
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break
        test_cases.append((x1, y1, x2, y2))
    def min_length(test_case):
        q = deque()
        q.append((test_case[1], test_case[0], 0, -1))
        visited = [[False for _ in range(w + 2)] for _ in range(h + 2)]
        min_length = 10000
        possible = False
        while q:
            nx, ny, length, dir_n = q.popleft()
            visited[nx][ny] = True
            for i, (dx, dy) in enumerate(dir):
                cx, cy = nx + dx, ny + dy
                if (cx, cy) == (test_case[3], test_case[2]):
                    possible = True
                    if dir_n == i:
                        min_length = min(min_length, length)
                    else:
                        min_length = min(min_length, length + 1)
            for i, (dx, dy) in enumerate(dir):
                cx, cy = nx + dx, ny + dy
                if 0 <= cx < h + 2 and 0 <= cy < w + 2 and not visited[cx][cy] and board[cx][cy] == 0 :
                    visited[cx][cy] = True
                    if i == dir_n:
                        q.append((cx, cy, length, i))
                    else:
                        q.append((cx, cy, length + 1, i))
                    visited[cx][cy] = False
        return possible, min_length
    print(f'Board #{index}:')
    for i, test_case in enumerate(test_cases):
        possible, length = min_length(test_case)[0], min_length(test_case)[1]
        if possible:
            print(f'Pair {i + 1}: {length} segments.')
        if not possible:
            print(f'Pair {i + 1}: impossible.')
    print()
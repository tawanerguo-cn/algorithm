from collections import deque
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
k = 0
while True:
    k += 1
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    board = ['']
    board[0] = ' ' * (w + 2)
    for _ in range(h):
        row = ' '
        row1 = input()
        row = row + row1 + row
        board.append(row)
    board.append(board[0])
    cards = []
    while True:
        x1, y1, x2, y2 = map(int, input().split())
        if (x1, y1, x2, y2) == (0, 0, 0, 0):
            break
        cards.append((y1, x1, y2, x2))
    def min_way(w, h, board, card):
        visited = [[False for _ in range(w + 2)] for _ in range(h + 2)]
        q = deque()
        q.append((card[0], card[1], 0, -1))
        visited[card[0]][card[1]] = True
        min_length = 100000
        possible = False
        while q:
            nx, ny, length, last_dir = q.popleft()
            for i in range(4):
                cx, cy = nx + dir[i][0], ny + dir[i][1]
                if 0 <= cx < h + 2 and 0 <= cy < w + 2 and not visited[cx][cy]:
                    if board[cx][cy] == ' ' and i == last_dir:
                        visited[cx][cy] = True
                        q.append((cx, cy, length, i))
                    elif board[cx][cy] == ' ' and i != last_dir:
                        visited[cx][cy] = True
                        q.append((cx, cy, length + 1, i))
                    elif (cx, cy) == (card[2], card[3]) and i == last_dir:
                        min_length = min(length, min_length)
                        possible = True
                    elif (cx, cy) == (card[2], card[3]) and i != last_dir:
                        min_length = min(length + 1, min_length)
                        possible = True
        return possible, min_length
    n1 = len(cards)
    print(f'Board #{k}:')
    for i in range(n1):
        find, min_length = min_way(w, h, board, cards[i])
        if find:
            print(f'Pair {i + 1}: {min_length} segments.')
        else:
            print(f'Pair {i + 1}: impossible.')
    print()
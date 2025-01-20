ans = []
queens = [-1] * 8#初始化位置
columns = set()
dia1 = set()
dia2 = set()
def backtrack(row):
    if row == 8:
        ans.append(queens[:])
        return
    for col in range(8):
        if col in columns or (row - col) in dia1 or (row + col) in dia2:
            continue
        queens[row] = col
        columns.add(col)
        dia1.add(row - col)
        dia2.add(row + col)
        backtrack(row + 1)
        queens[row] = -1
        columns.remove(col)
        dia1.remove(row - col)
        dia2.remove(row + col)
backtrack(0)
list_q = []
for i in ans:
    queen = ''.join(str(col + 1) for col in i)
    list_q.append(int(queen))
list_q.sort()
n = int(input())
for _ in range(n):
    b = int(input())
    print(list_q[b - 1])

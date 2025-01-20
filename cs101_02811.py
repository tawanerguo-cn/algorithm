def toggle(board, r, c):
    board[r][c] ^= 1
    if r > 0:
        board[r-1][c] ^= 1
    if r < 4:
        board[r+1][c] ^= 1
    if c > 0:
        board[r][c-1] ^= 1
    if c < 5:
        board[r][c+1] ^= 1
def solve_lights_out(lights):
    import copy
    for first_row_state in range(64):
        press = [[0]*6 for _ in range(5)]
        temp = copy.deepcopy(lights)
        row_0_bits = [ (first_row_state >> c) & 1 for c in range(6) ]
        row_0_bits.reverse()
        for c in range(6):
            if row_0_bits[c] == 1:
                press[0][c] = 1
                toggle(temp, 0, c)
        for r in range(4):
            for c in range(6):
                if temp[r][c] == 1:
                    press[r+1][c] = 1
                    toggle(temp, r+1, c)
        if all(temp[4][c] == 0 for c in range(6)):
            return press
    return None
lights = []
for _ in range(5):
    row = list(map(int, input().split()))
    lights.append(row)
solution = solve_lights_out(lights)
for r in range(5):
    print(" ".join(map(str, solution[r])))


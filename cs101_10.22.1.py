from math import gcd
def cycle_decomposition(num):
    n = len(num)
    visited = [False] * n
    cycles = []
    cycle_index = [-1] * n
    pos_in_cycle = [-1] * n
    current_cycle_id = 0
    for start in range(n):
        if not visited[start]:
            cycle = []
            cur = start
            while not visited[cur]:
                visited[cur] = True
                cycle_index[cur] = current_cycle_id
                pos_in_cycle[cur] = len(cycle)
                cycle.append(cur)
                cur = num[cur]
            cycles.append(cycle)
            current_cycle_id += 1
    return cycles, cycle_index, pos_in_cycle
def encode_once_with_decomposition(message, cycles, cycle_index, pos_in_cycle, k):
    n = len(message)
    encoded = [' '] * n
    for i in range(n):
        c_idx = cycle_index[i]
        offset = pos_in_cycle[i]
        cycle = cycles[c_idx]
        c_len = len(cycle)
        new_pos = cycle[(offset + k) % c_len]
        encoded[new_pos] = message[i]
    return encoded
while True:
    n_line = input().strip()
    if not n_line:
        continue
    n = int(n_line)
    if n == 0:
        break
    permutation_line = input().strip()
    nums = list(map(int, permutation_line.split()))
    num = [x - 1 for x in nums]
    cycles, cycle_index, pos_in_cycle = cycle_decomposition(num)
    while True:
        line = input().rstrip('\n')
        if line == '0':
            break
        parts = line.split(' ', 1)
        k = int(parts[0])
        message = parts[1] if len(parts) > 1 else ""
        message = list(message) + [' '] * (n - len(message))
        message = message[:n]
        encoded = encode_once_with_decomposition(message, cycles, cycle_index, pos_in_cycle, k)
        print("".join(encoded))
    print()

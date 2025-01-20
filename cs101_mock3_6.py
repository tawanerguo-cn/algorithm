n = int(input().strip())
king_a, king_b = map(int, input().strip().split())
ministers = [tuple(map(int, input().strip().split())) for _ in range(n)]
ministers.sort(key=lambda x: x[0] * x[1])
current_product = king_a
max_reward = 0
for a, b in ministers:
    reward = (current_product // b)
    if reward > max_reward:
        max_reward = reward
    current_product *= a
print(max_reward)

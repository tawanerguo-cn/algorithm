def H(x):
    return 3 * x
def O(x):
    return int(0.5 * x)
dir = ['H', 'O']
while True:
    n, m = map(int,input().split())
    if (n, m) == (0, 0):
        break
    min_way1 = []
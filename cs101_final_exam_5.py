def H(x):
    return [int(3 * x),'H']
def O(x):
    return [int(0.5 * x),'O']
while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    operator = ''

def divisor(a,b):
    while a % b != 0:
        b = min(a - b,b)
        a = max(a-b,b)
    return b
while True:
    try:
        a,b = map(int,input().split())
        print(divisor(max(a,b),min(a,b)))
    except EOFError:
        break
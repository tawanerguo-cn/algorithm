while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break
    a, b = max(a, b), min(a, b)
    who = 1
    while a // b < 2 and a != b: 
        a = a - b
        a, b = b, a
        who *= -1
    if who == 1:
        print('win')
    else:
        print('lose')
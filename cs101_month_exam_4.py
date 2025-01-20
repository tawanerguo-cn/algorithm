n = int(input())
while n != 1:
    if n % 2 == 0:
        print(f'{n}/2={int(0.5 * n)}')
        n = int(0.5 * n)
    else:
        print(f'{n}*3+1={3 * n + 1}')
        n = 3 * n + 1
print('End')
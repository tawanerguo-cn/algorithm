n = int(input())
for _ in range(n):
    num = input()
    a = True
    if int(num) % 19 == 0:
        print('Yes')
        a = False
    else:
        n1 = len(num)
        for i in range(n1 - 1):
            if num[i] == '1' and num[i + 1] == '9':
                print('Yes')
                a = False
                break
    if a:
        print('No')
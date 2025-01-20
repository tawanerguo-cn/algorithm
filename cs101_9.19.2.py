lucky_number = []
for n in range(1,1001):
    list_n = [i for i in str(n)]
    if list_n.count('4') + list_n.count('7') == len(list_n):
        lucky_number.append(n)
n = int(input())
a = True
for i in lucky_number:
    if n % i == 0:
        print('YES')
        a = False
        break
if a:
    print('NO')
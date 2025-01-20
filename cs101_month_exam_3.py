n = int(input())
para = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
x_list = ['1','0','X','9','8','7','6','5','4','3','2']
for _ in range(n):
    string = input()
    x_number = x_list.index(string[-1])
    number = [int(string[i]) for i in range(len(string) - 1)]
    m = 0
    for i in range(len(number)):
        m += para[i] * number[i]
    m = m % 11
    if m == x_number:
        print('YES')
    else:
        print('NO')
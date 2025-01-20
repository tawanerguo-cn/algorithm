
list_1 = []
list_2 = []
for i in range(0,20):
    for j in range(0,i+1):
        list_1.append(3**i * 2**j)
        list_2.append(2*i-j)
t = int(input())
for _ in range(t):
    n = int(input())
    if n in list_1:
        print(list_2[list_1.index(n)])
    else:
        print(-1)
def prime_number(n):
    a = True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a = False
        return i
    if a:
        return n
t = int(input())
for _ in range(t):
    n = int(input())
    list_number = []
    while n != 1:
        list_number.append(prime_number(n))
        n = n // prime_number(n)
    n_2 = list_number.count(2)
    n_3 = list_number.count(3)
    if n_2 + n_3 != len(list_number):
        print(-1)
    elif n_2 > n_3:
        print(-1)
    else:
        print(2*n_3 - n_2)
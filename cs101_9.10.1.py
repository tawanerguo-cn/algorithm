n = int(input())
if n == 1 :
    print(1)
    exit()
def is_prime(number):
    bool_1 = True
    for i in range(2,int(number**0.5+1)):
        if number % i == 0:
            m = i
            bool_1 = False
            break
    if bool_1:
        m = number
    return m
list_prime = []
while is_prime(n) != n:
    list_prime.append(is_prime(n))
    n = n // is_prime(n)
list_prime.append(n)
bool_2 = True
for i in list_prime:
    if list_prime.count(i) >= 2:
        print(0)
        bool_2 = False
        break
if bool_2:
    if len(list_prime) % 2 == 0:
        print(1)
    else:
        print(-1)
n = int(input())
prime = []
is_prime = [True for _ in range(1000 + 1)]
is_prime[0] = False
is_prime[1] = False
for i in range(2, 1000 + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if is_prime[j] and i % j == 0:
            is_prime[i] = False
for i in range(2, 1000 + 1):
    if is_prime[i]:
        prime.append(i)
#现在已经获得了1-1000质数表
divide = []
while n > 1:
    is_prime_n = True
    for i in prime:
        if n % i == 0:
            divide.append(i)
            n = n // i
            is_prime_n = False
    if is_prime_n:
        divide.append(n)
        break
divide_even_odd = len(divide)
divide_dict = {}
for i in divide:
    if i in divide_dict:
        divide_dict[i]  += 1
    else:
        divide_dict[i] = 1
is_square = False
for i in divide:
    if divide_dict[i] % 2 == 0:
        is_square = True
        break
if divide_even_odd % 2 == 0 and not is_square:
    print('1')
elif divide_even_odd % 2 == 1 and not is_square:
    print('-1')
elif is_square:
    print('0')
x = int(input())
prime_list = []
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
for i in range(2,2001):
    if is_prime(i):
        prime_list.append(i)
if x < 6 or x % 2 != 0:
    print('Error!')
else:
    for number in prime_list:
        if x - number in prime_list and number <= x - number:
            print(f'{x}={number}+{x-number}')
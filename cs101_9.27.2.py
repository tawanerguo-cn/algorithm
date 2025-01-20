def ai_shi(m):
    is_prime = [True for _ in range(m + 1)]
    is_prime[0] = is_prime[1] = False
    prime = []
    for i in range(2,m + 1):
        if is_prime[i]:
            prime.append(i)
            for j in range(i * i,m + 1,i):
                is_prime[j] = False
    return is_prime
is_prime_list = tuple(ai_shi(1000000))
def is_square(m):
    return int(m ** 0.5) ** 2 == m
n = int(input())
test1 = list(map(int,input().split()))
print_list = []
for test in test1:
    if is_square(test) and is_prime_list[int(test**0.5)]:
        print_list.append('YES')
    else:
        print_list.append('NO')
for i in print_list:
    print(i)
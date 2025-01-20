s = int(input())
prime = []
for i in range(2,s + 1):
    a = True
    for j in range(2,int(i ** 0.5) + 1):
        if i % j == 0:
            a = False
            break
    if a:
        prime.append(i)
pro = []
for i in prime:
    if s - i in prime:
        pro.append(i * (s - i))
print(max(pro))
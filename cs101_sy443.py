num = list(map(int, input().split()))
number = []
for i, num1 in enumerate(num):
    number.extend([str(i) for _ in range(num1)])
number.reverse()
number = ''.join(i for i in number)
print(int(number))
#23554, 23564, 23555, 23556, 23558, 23568
n = int(input())
num = list(map(int, input().split()))
class_our = [[i + 1, 0] for i in range(n)]
class_other = []
for i in range(len(num)):
    if num[i] <= n:
        class_our[num[i] - 1][1] = 1
    else:
        class_other.append(num[i])
class_other.sort()
class_our_print = []
for i in class_our:
    if i[1] == 0:
        class_our_print.append(i[0])
print(' '.join((str(i) for i in class_our_print)))
print(' '.join(str(i) for i in class_other))
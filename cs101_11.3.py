from itertools import permutations
n = int(input())
num = list(map(int, input().split()))
num.sort()
unique_perms = sorted(set(permutations(num)))
for k in unique_perms:
    print(' '.join(str(i) for i in k))
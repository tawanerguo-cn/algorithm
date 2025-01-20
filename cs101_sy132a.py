from itertools import permutations
m = int(input())
list_m = list(permutations(range(m)))
for i in list_m:
    print(' '.join(str(i[j] + 1) for j in range(m)))

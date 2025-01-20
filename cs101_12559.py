n = int(input())
num = list(map(str,input().split()))
num_and_dec = [[num[i]] for i in range(n)]
m = max([len(num[i]) for i in range(n)])
for i in range(n):
    for j in range(m):
        num_and_dec[i].append(num[i][(j+1) % len(num[i]) - 1])
num_and_dec.sort(key = lambda x:[x[i+1] for i in range(m)])
print(''.join(num_and_dec[i-1][0] for i in range(len(num),0,-1)),''.join(num_and_dec[i][0] for i in range(len(num))))
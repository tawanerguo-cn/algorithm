n = int(input())
a = list(map(int,input().split()))
freq = [0 for _ in range(10 ** 5 + 1)]
for i in a:
    freq[i] += 1
p2,p1 = 0,freq[1]
for i in range(2,10 ** 5 + 1):
    c = max(p1,p2 + freq[i] * i)
    p2,p1 = p1,c
print(p1)

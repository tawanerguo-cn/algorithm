n = int(input())
print(2**n - 1)
start = [[] for _ in range(n)]
end = [[] for _ in range(n)]
start[0] = 'A'
end[0] = 'C'
for i in range(1,n):
    start1 = ['B' if x == 'C' else 'C' if x == 'B' else x for x in start[i-1]]
    start2 = ['B' if x == 'A' else 'A' if x == 'B' else x for x in start[i-1]]
    start[i].extend(start1)
    start[i].append('A')
    start[i].extend(start2)
    end1 = ['B' if x == 'C' else 'C' if x == 'B' else x for x in end[i-1]]
    end2 = ['B' if x == 'A' else 'A' if x == 'B' else x for x in end[i-1]]
    end[i].extend(end1)
    end[i].append('C')
    end[i].extend(end2)
for i in range(len(start[n-1])):
    print(f'{start[n-1][i]}->{end[n-1][i]}')
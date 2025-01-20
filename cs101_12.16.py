n = int(input())
a = list(map(int, input().split()))
monitor = []
for i in range(n):
    monitor.append([i - a[i], i + a[i]])
monitor.sort(key = lambda x:(x[0], -x[1]))
count = 0
end = monitor[0][1]
start = 0
for i in range(n):
    if monitor[i][0] <= start and monitor[i][1] >= start:
        end = max(end, monitor[i][1])
        if end >= n - 1:
            count += 1
            break
    else:
        count += 1
        start = 0
        start += end
print(count)
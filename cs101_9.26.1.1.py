while True:
    n = int(input())
    if n == 0:
        break
    speed = []
    start = []
    end = []
    for i in range(n):
        a,b = map(int,input().split())
        speed.append(a)
        start.append(b)
        end.append(start[-1] + 4.5 /speed[-1] * 3600)
    start_1 = min([i for i in start if i >= 0])
    end_1 = end[start.index(start_1)]
    end_final = [end_1]
    for i in range(n):
        if start[i] > start_1 and end[i] < end_1:
            end_final.append(end[i])
    print(int(-(-min(end_final) // 1)))
while True:
    n = int(input())
    if n == 0:
        break
    speed = []
    time = []
    end = []
    for i in range(n):
        a,b = map(int,input().split())
        speed.append(a)
        time.append(b)
        end.append(time[-1] + 4.5 / speed[-1] * 3600)
    eff = []
    for i in time:
        if i >= 0:
            eff.append(i)
    start_ = min(eff)
    end_ = end[time.index(start_)]
    end_eff = []
    for i in range(n):
        if time[i] >= start_ and end[i] <= end_:
            end_eff.append(end[i])
    print(int(-(-min(end_eff)//1)))
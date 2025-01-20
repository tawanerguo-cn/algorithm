n = int(input())
prog = []
for _ in range(n):
    cal1, write1 = map(int, input().split())
    prog.append([cal1, write1])
prog.sort(key = lambda x:x[1], reverse = True)
endtime = 0
cal_time = 0
for i in range(n):
    cal_time += prog[i][0]
    endtime = max(cal_time + prog[i][1], endtime)
print(endtime)
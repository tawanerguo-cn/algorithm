n = int(input())
s = list(map(int,input().split()))
a1,a2,a3,a4 = s.count(1),s.count(2),s.count(3),s.count(4)
taxi = a4
taxi += a3
a1 = max(0,a1 - a3)
taxi += a2 // 2
if a2 % 2 != 0:
    taxi += 1
    a1 = max(0,a1-2)
taxi += a1 // 4
if a1 % 4 != 0:
    taxi += 1
print(taxi)
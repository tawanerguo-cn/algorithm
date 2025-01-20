n = int(input())
s = list(map(int,input().split()))
taxi = 0
s4 = s.count(4)
s3 = s.count(3)
s2 = s.count(2)
s1 = s.count(1)
taxi += s4
taxi += s3
s1 = max(0,s1 - s3)
if s2 % 2 == 0:
    taxi += s2 // 2
else:
    taxi += (s2 - 1) // 2 + 1
    s1 = max(0,s1 - 2)
if s1 % 4 == 0:
    taxi += s1 // 4
else:
    taxi += s1 // 4 + 1
print(taxi)

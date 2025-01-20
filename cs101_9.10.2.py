n,m = map(int,input().split())
left = n
day = 0
while left > 0:
    left -= 1
    day += 1
    if day % m == 0:
        left += 1
print(day)
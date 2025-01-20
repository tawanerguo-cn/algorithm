n = int(input())
weekend_list = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
def weekend(date_list):
    year = int(''.join(date_list[0:4]))
    m = int(''.join(date_list[4:6]))
    if m < 3:
        m += 12
        year -= 1
    c = year // 100
    y = year % 100
    d = int(''.join(date_list[6:8]))
    w = (y + int(y/4) + int(c/4) - 2*c + int(2.6*(m+1)) + d - 1) % 7
    return w
for _ in range(n):
    date_list = [i for i in input()]
    print(weekend_list[weekend(date_list)])
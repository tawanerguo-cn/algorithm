list_number = []
m = 0
n = 2
while m <= 5.20:
    m += 1/n
    n+=1
    list_number.append(m)

while True:
    c = float(input())
    if c == 0.00:
        break
    for i in list_number:
        if i >= c:
            print(f'{list_number.index(i)+1} card(s)')
            break

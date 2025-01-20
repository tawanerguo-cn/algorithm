m = int(input())
for _ in range(m):
    Found = False
    list_number = list(map(int,input().split()))
    for i in range(0,2):
        for j in range(0,2):
            for k in range(0,2):
                for l in range(0,2):
                    if ((-1)**l) *list_number[0] + ((-1)**i) * list_number[1] + ((-1)**j) * list_number[2] + ((-1)**k) * list_number[3] == 24:
                        print('YES')
                        Found = True
                        break
                if Found:
                    break
            if  Found:
                break
        if  Found:
            break
    if not Found:
        print('NO')
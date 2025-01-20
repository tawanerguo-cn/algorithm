string = input()
list_teammates = [i for i in string]
count_same = 0
bool_1 = True
for i in range(len(list_teammates)-1):
    if list_teammates[i] == list_teammates[i+1]:
        count_same += 1
        if count_same == 6:
            print('YES')
            bool_1 = False
            break
    else:
        count_same = 0
if bool_1:
    print('NO')
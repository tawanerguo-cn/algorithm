string = input().lower()
list_str = [i for i in string]
list_squ = [[list_str[0],1]]
for i in range(len(list_str)-1):
    if list_str[i] == list_str[i+1]:
        list_squ[-1][1] += 1
    else:
        list_squ.append([list_str[i+1],1])
print(''.join(f'({list_squ[i][0]},{list_squ[i][1]})'for i in range(len(list_squ))))

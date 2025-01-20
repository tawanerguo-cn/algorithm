n = int(input())
list_input = list(map(int,input().split()))
output_list = [list_input[0]]
pm = 1
if list_input[1] < list_input[0]:
    pm = -1
for i in range(1,n):
    if list_input[i] > output_list[-1] and pm == 1:
        output_list.append(list_input[i])
        pm = -1
    elif list_input[i] > output_list[-1] and pm == -1:
        output_list[-1] = list_input[i]
    elif list_input[i] < output_list[-1] and pm == -1:
        output_list.append(list_input[i])
        pm = 1
    elif list_input[i] < output_list[-1] and pm == 1:
        output_list[-1] = list_input[i]
print(len(output_list))
#直接重写
num1 = int(input())
num2 = int(input())
if num1 < num2:
    num1,num2 = num2,num1
num1_list = [int(i) for i in str(num1)]
num2_list = [int(i) for i in str(num2)]
num1_list.reverse()
num1_list.append(0)
num2_list.reverse()
num2_list.extend([0 for i in range(len(num1_list) - len(num2_list) - 1)])
num_sum = []
for i in range(len(num2_list)):
    num_sum.append((num1_list[i] + num2_list[i]) % 10)
    num1_list[i + 1] += (num1_list[i] + num2_list[i]) // 10
if num1_list[-1] == 1:
    num_sum.append(1)
num_sum.reverse()
print(''.join(str(i) for i in num_sum))

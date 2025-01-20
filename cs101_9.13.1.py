n = int(input())
def relate_7(number):
    a = False
    number_list = [int(i) for i in str(number)]
    if number_list.count(7) != 0 or number % 7 == 0:
        a = True
    return a
sum_number = 0
for i in range(1,n+1):
    if not relate_7(i):
        sum_number += i**2
print(sum_number)
rome_list = ['I','V','X','L','C','D','M']
number_list = [1,5,10,50,100,500,1000]
rome_list1 = ['IV','IX','XL','XC','CD','CM']
number_list1 = [4,9,40,90,400,900]
n = input()
def r2n(num):
    output = 0
    while len(num) != 0:
        if ''.join(n[0:2]) not in rome_list1:
            output += number_list[rome_list.index(num[0])]
            num.pop(0)
        else:
            output += number_list1[rome_list1.index(''.join(n[0:2]))]
            num.pop(0)
            num.pop(0)
    return output
def n2r(num):
    output = ''
    n = len(number_list)
    for i in range(n):
        if num // number_list[n - 1 - i] > 0 and str(num)[0] != '4' and str(num)[0] != '9':
            output += rome_list[n - 1 - i] * (num // number_list[n - 1 - i])
            num -= number_list[n - 1 - i] * (num // number_list[n - 1 - i])
        elif num // number_list[n - 1 - i] > 0 and (str(num)[0] == '4' or str(num)[0] == '9'):
            output += rome_list1[n - 1 - i]
            num -= number_list1[n - 1 - i]
    return output
if ord(n[-1]) > 57:
    n = [i for i in n]
    print(r2n(n))
else:
    n = int(n)
    print(n2r(n))

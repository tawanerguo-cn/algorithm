dollar=int(input())
list_money=[100,20,10,5,1]
num=0
for i in list_money:
    num+=dollar//i
    dollar = dollar%i
print(num)

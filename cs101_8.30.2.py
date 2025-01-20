def round_number(number):
    n=number
    list_base=[10000,1000,100,10,1]
    list_num=[10000,1000,100,10,1]
    for i in range(5):
        list_num[i]=list_num[i]*(n//list_base[i])
        n=n%list_base[i]
    print(len(list_num)-list_num.count(0))
    print(' '.join(str(i) for i in list_num if i!=0))
t=int(input())
for i in range(t):
    round_number(int(input()))

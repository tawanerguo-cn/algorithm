n,k = map(int,input().split())
dict_1 = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
output = []
while n >= 1:
    output.append(dict_1[n % k])
    n = n // k
output.reverse()
print(''.join(str(i) for i in output))
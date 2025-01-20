from functools import cmp_to_key
n = int(input())
num = input().split()
num.sort(key = cmp_to_key(lambda x,y:(int(x + y) - int(y + x))))
number = ''.join(i for i in num).lstrip('0')
print(number if number else '0')
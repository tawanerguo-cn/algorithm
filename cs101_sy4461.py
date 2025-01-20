n = int(input())
num = input().split()

# 排序时构造排序键
num.sort(key=lambda x: x * 10)

# 拼接结果
num = ''.join(num).lstrip('0')
print(num if num else '0')

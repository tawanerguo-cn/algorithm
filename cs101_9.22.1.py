n = int(input())
list_bin = []
while n != 0:
    list_bin.append(n % 2)
    n = n // 2
print(list_bin)
a = True
for i in range(len(list_bin)):
    if list_bin[i] != list_bin[len(list_bin) - 1 - i]:
        print('No')
        a = False
        break
if a:
    print('Yes')
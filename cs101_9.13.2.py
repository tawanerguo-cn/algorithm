s = input()
word_list = [i for i in s]
target = ['h','e','l','l','o']
for i in range(5):
    if len(word_list) < 5:
        print('NO')
        exit()
    while word_list[i] != target[i] and len(word_list) > i+1:
        word_list.pop(i)
if word_list[0:5] == target:
    print('YES')
else:
    print('NO')

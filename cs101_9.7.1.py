n = int(input())
m = 0
for i in range(n):
    sentence = input().split()
    list_word = [[k for k in sentence[j]] for j in range(len(sentence))]
    list_word.append(['a'])
    for j in range(len(sentence)):
        if list_word[j][-1] == '#' and list_word[j+1][0] != '#':
            m+=1
print(m)
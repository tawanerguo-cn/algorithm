list_x = list(map(int,input().split()))
list_sorted = sorted(list_x)
list_answer = []
for i in range(3):
    list_answer.append(list_sorted[3] - list_sorted[i])
print(' '.join(str(list_answer[i]) for i in range(3)))
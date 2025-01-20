n=int(input())
list_initial=[]
solved_problem=0
for i in range(n):
    list_initial.append(list(map(int,input().split())))
    if list_initial[i].count(1)>=2:
        solved_problem+=1
print(solved_problem)
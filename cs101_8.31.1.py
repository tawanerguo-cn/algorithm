n=int(input())
list_event=list(map(int,input().split()))
list_condition=[0]
for i in list_event:
    list_condition.append(list_condition[-1]+i)
print(abs(min(list_condition)))
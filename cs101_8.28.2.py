n=int(input())
m=0
colors_list=[i for i in input()]
for i in range(len(colors_list)-1):
    if colors_list[i+1]==colors_list[i]:
        m+=1
print(m)
n = int(input())
wood = []
for _ in range(n):
    x1, h1 = map(int, input().split())
    wood.append([x1, h1])
if n == 1:
    print(1)
    exit()
count = 1
for i in range(1, n - 1):
    if wood[i][0] - wood[i - 1][0] > wood[i][1]:
        count += 1
    elif wood[i + 1][0] - wood[i][0] > wood[i][1]:
        count += 1
        wood[i][0] = wood[i][0] + wood[i][1]
count += 1
print(count)
#如果能往左边倒，倒在左边
#如果不能往左边倒，但能往右边倒，就倒在右边
#判断下一颗树能否往左边倒：
#如果上一颗树往左边倒，则下一颗树够短就能往左边倒
#这样子的讨论就显得太冗长了，好的（GPT的）思维方式如下：
#从前往后遍历，倒了一颗树就更新末端位置，因为判断能否向左倒的关键就在于末端位置是否重叠，而不在于树位置本身
# （觉得这个重要只是因为这里的末端只有两种情况）
# n = int(input())
# a = list(map(int,input().split()))
# a.sort()
# #贪心策略：排完序后，对于某个a[i]向后搜寻，如果有比其更大的，就放进这个里面，并且从这个开始往后搜寻
# #想一想能不能用for循环？
# visible = [0]
# for i in range(n):
#     if a[i] > visible[j]:
#         visible[j] = a[i]
#         break
#     else:
#         visible.append(a[i])
# print(len(visible))
# #一开始不对的原因：只搜索最后一个是有问题的
# #现在的问题在于超时
n = int(input())
a = list(map(int,input().split()))
a_set = set(a)
num = []
for i in a_set:
    num.append(a.count(i))
print(max(num))
#经过仔细地思考后
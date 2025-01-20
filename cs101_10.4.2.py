# n = int(input())
# queue = list(map(int,input().split()))
# queue.sort()
# queue_wait = [0]
# k = 0
# for i in range(n-1):
#     queue_wait.append(queue_wait[i] + queue[i])
# i = 0
# k = 0
# print(queue_wait)
# print(queue)
# while i != n:
#     if queue_wait[i] <= queue[i]:
#         k += 1
#         i += 1
#     else:
#         i += 1#这样写的时候首先就要求i一定会增加，否则无法跳出while循环
#         for j in range(i,n):
#             if queue[j] >= queue_wait[i-1]:
#                 queue[i-1],queue[j] = queue[j],queue[i-1]
#                 print(queue)
#                 k += 1
#                 i = j+1
#                 break
# print(k)
#上面的贪心思路是有问题的，已经失望了的应该排在后面
n = int(input())
queue = list(map(int,input().split()))
queue.sort()
wait = 0
k = 0
for i in range(n):
    if queue[i] >= wait:
        wait += queue[i]
        k += 1
print(k)
#思考一下怎么才能想到答案的解法：首先排序，如果这个人在从小到大排序时都无法满意，那么他就废了，于是直接剔掉，也就是判断条件，然后继续排队加人
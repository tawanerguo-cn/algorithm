# n = int(input())
# for num in range(6,n + 1):
#     for i in range(2,num):
#         for j in range(i,num):
#             for k in range(j,num):
#                 if num ** 3 == i ** 3 + j ** 3 + k ** 3:
#                     print(f'Cube = {num}, Triple = ({i},{j},{k})')
#时间复杂度更低的算法：
n = int(input())
cube = {i ** 3 : i for i in range(2,n + 1)}
cube_dict = {i : i ** 3 for i in range(2,n + 1)}
ans = []
for b in range(2,n):
    for c in range(b,n):
        for d in range(c,n):
            if cube_dict[d] + cube_dict[c] + cube_dict[b] in cube:
                ans.append([cube[cube_dict[d] + cube_dict[c] + cube_dict[b]],b,c,d])
ans.sort(key = lambda x:x[0])
for i in range(len(ans)):
    print(f'Cube = {ans[i][0]}, Triple = ({ans[i][1]},{ans[i][2]},{ans[i][3]})')

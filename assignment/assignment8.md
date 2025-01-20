# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>熊程宇 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：

延拓边界，然后讨论1的旁边有多少个0即可

代码：

```python
n,m = map(int,input().split())
map1 = [[0 for _ in range(m + 2)]]
for _ in range(n):
    l1 = [0]
    l1.extend(list(map(int,input().split())))
    l1.extend([0])
    map1.append(l1)
map1.append([0 for _ in range(m + 2)])
p = 0
for i in range(1,n + 1):
    for j in range(1,m + 1):
        if map1[i][j] == 1:
            if [map1[i-1][j],map1[i + 1][j],map1[i][j-1],map1[i][j + 1]].count(0) == 1:
                p += 1
            elif [map1[i-1][j],map1[i + 1][j],map1[i][j-1],map1[i][j + 1]].count(0) == 2:
                p += 2
            elif [map1[i-1][j],map1[i + 1][j],map1[i][j-1],map1[i][j + 1]].count(0) == 3:
                p += 3
            elif [map1[i-1][j],map1[i + 1][j],map1[i][j-1],map1[i][j + 1]].count(0) == 4:
                p += 4
print(p)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241117195221908](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241117195221908.png)

### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：

递推，利用i-2的矩阵构建i的矩阵，这样就只需要写边界了

代码：

```python
n = int(input())
dp = [[[0 for _ in range(i)] for _ in range(i)] for i in range(1,n + 1)]
dp[0] = [[1]]
dp[1] = [[1,2],[4,3]]
for i in range (2,n):
    for j in range(i + 1):
        for k in range(i + 1):
            if j == 0:
                dp[i][j][k] = k + 1
            elif j == i:
                dp[i][j][k] = 3 * i + 1 - k
            elif k == 0 and j != 0 and j != i:
                dp[i][j][k] = 4 * i + 1 - j
            elif k == i and j != 0 and j != i:
                dp[i][j][k] = i + 1 + j
            else:
                dp[i][j][k] = dp[i-2][j-1][k-1] + 4 * i
for i in range(n):
    print(' '.join(str(j) for j in dp[n-1][i]))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241117205203573](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241117205203573.png)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：

依然延拓矩阵，计算每一处垃圾位置对应的垃圾爆炸可波及范围，加上去就行。

代码：

```python
d = int(input())
n = int(input())
rub = []
for _ in range(n):
    xi,yi,i1 = map(int,input().split())
    rub.append([xi + d,yi + d,i1])
boom_mat = [[0 for _ in range(1025 + 2 * d)] for _ in range(1025 + 2 * d)]
for k in rub:
    for i in range(-d,d + 1):
        for j in range(-d,d + 1):
            boom_mat[k[0] + i][k[1] + j] += k[2]
boom_set = set([boom_mat[i][j] for i in range (d,1025 + d) for j in range(d, 1025 + d)])
max_rub = max(list(boom_set))
m0 = 0
for i in range(d,1025 + d):
    for j in range(d,1025 + d):
        if boom_mat[i][j] == max_rub:
            m0 += 1
print(m0,max_rub)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241117214440212](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241117214440212.png)



### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：

贪心，初始需要讨论，并且遇到更大/更小的需要更新末尾值，这就导致WA了两次

代码：

```python
n = int(input())
list_input = list(map(int,input().split()))
output_list = [list_input[0]]
pm = 1
if list_input[1] < list_input[0]:
    pm = -1
for i in range(1,n):
    if list_input[i] > output_list[-1] and pm == 1:
        output_list.append(list_input[i])
        pm = -1
    elif list_input[i] > output_list[-1] and pm == -1:
        output_list[-1] = list_input[i]
    elif list_input[i] < output_list[-1] and pm == -1:
        output_list.append(list_input[i])
        pm = 1
    elif list_input[i] < output_list[-1] and pm == 1:
        output_list[-1] = list_input[i]
print(len(output_list))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241117220643020](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241117220643020.png)



### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：

还不是特别会这种动态规划，询问GPT得到了思路

代码：

```python
n = int(input())

a = list(map(int,input().split()))

freq = [0 for _ in range(10 ** 5 + 1)]

for i in a:

  freq[i] += 1

p2,p1 = 0,freq[1]

for i in range(2,10 ** 5 + 1):

  c = max(p1,p2 + freq[i] * i)

  p2,p1 = p1,c

print(p1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241117230618956](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241117230618956.png)

### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：

不会…

代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

补每日选做……

终于把装箱问题做出来了😃






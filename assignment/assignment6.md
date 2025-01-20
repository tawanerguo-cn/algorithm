# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by <mark>熊程宇 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：

利用上一次的推下一次，BC互换，AB互换加上一个A到C即可

写列表推导式时，将if写在后面就行

询问GPT，还知道了可以使用map函数map(swap_AB（这是函数）,待交换列表)

代码：

```python
n = int(input())
print(2**n - 1)
start = [[] for _ in range(n)]
end = [[] for _ in range(n)]
start[0] = 'A'
end[0] = 'C'
for i in range(1,n):
    start1 = ['B' if x == 'C' else 'C' if x == 'B' else x for x in start[i-1]]
    start2 = ['B' if x == 'A' else 'A' if x == 'B' else x for x in start[i-1]]
    start[i].extend(start1)
    start[i].append('A')
    start[i].extend(start2)
    end1 = ['B' if x == 'C' else 'C' if x == 'B' else x for x in end[i-1]]
    end2 = ['B' if x == 'A' else 'A' if x == 'B' else x for x in end[i-1]]
    end[i].extend(end1)
    end[i].append('C')
    end[i].extend(end2)
for i in range(len(start[n-1])):
    print(f'{start[n-1][i]}->{end[n-1][i]}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102195805578](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241102195805578.png)



### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：

最后得重新排次序

代码：

```python
n = int(input())
list_n = [[] for _ in range(n)]
list_n[0] = '1'
for i in range(1,n):
    for m in range(len(list_n[i-1])):
        for j in range(i+1):
            list_n[i].append(list_n[i-1][m][:j] + f'{i+1}' + list_n[i-1][m][j:])
output = sorted([int(x) for x in list_n[n-1]])
for i in output:
    print(' '.join(str(i)))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241102201921310](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241102201921310.png)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：最长非递增子序列，标准的动态规划问题，于是开始问GPT……



代码：

```python
k = int(input())
m = list(map(int,input().split()))
dp = [1] * k
for i in range(1,k):
    for j in range(i):
        if m[j] >= m[i]:
            dp[i] = max(dp[i],dp[j] + 1)
print(max(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241102211340487](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241102211340487.png)

### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：

试图贪心，但不能部分拿走，所以不能使用贪心

动态规划似乎是小学奥数爬楼梯的升级版

代码：

```python
n,b = map(int,input().split())
p = list(map(int,input().split()))
w = list(map(int,input().split()))
dp = [0] * (b + 1)
for i in range(n):
    for j in range(b,w[i] - 1,-1):
        dp[j] = max(dp[j],dp[j - w[i]] + p[i])
print(dp[b])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241102214757465](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241102214757465.png)

### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：

完全不会……

代码：

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：

这道题的dp相对比较简单，但是边界判定有些繁杂

代码：

```python
n,a,b,c = map(int,input().split())
dp = [1 if i in [a,b,c] else 0 for i in range(n+1)]
for i in range(1,n+1):
    if dp[max(i-a,0)] != 0 or dp[max(i-b,0)] != 0 or dp[max(i-c,0)] != 0:
        dp[i] = max(dp[max(i-a,0)]+1,dp[max(i-b,0)]+1,dp[max(i-c,0)]+1)
print(dp[n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102232248457](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241102232248457.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>



期中季ing

八皇后问题过于困难，两道dp抄答案之后感觉已经粗浅理解dp了，最后一道题能比较顺利地写出（似乎本身就比较简单）


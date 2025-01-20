# Assignment #4: T-primes + 贪心

Updated 0337 GMT+8 Oct 15, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：忘了



代码

```python
# 
n,m = map(int,input().split())
list_ai = list(map(int,input().split()))
list_sorted = sorted(list_ai)
negative_number = 0
if list_sorted[n-1] < 0:
    negative_number = n
for i in range(n-1):
    if list_sorted[i+1] >= 0 and list_sorted[i] < 0:
        negative_number = i+1
        break
print(abs(sum(list_sorted[0:min(negative_number,m)])))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241016213738175](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241016213738175.png)

### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：忘了



代码

```python

n = int(input())
list_values = list(map(int,input().split()))
list_sorted = sorted(list_values,reverse=True)
values = sum(list_sorted)
sum_values = 0
for i in range(n):
    sum_values += list_sorted[i]
    if 2*sum_values > values:
        print(i+1)
        break
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241016213939660](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241016213939660.png)



### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：忘了



代码

```python
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    cost_1 = min(a)*n + sum(b)
    cost_2 = min(b)*n +sum(a)
    print(min(cost_1,cost_2))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241016214135025](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241016214135025.png)



### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：一步一步写，保证每辆车都填满



代码

```python
n = int(input())
s = list(map(int,input().split()))
taxi = 0
s4 = s.count(4)
s3 = s.count(3)
s2 = s.count(2)
s1 = s.count(1)
taxi += s4
taxi += s3
s1 = max(0,s1 - s3)
if s2 % 2 == 0:
    taxi += s2 // 2
else:
    taxi += (s2 - 1) // 2 + 1
    s1 = max(0,s1 - 2)
if s1 % 4 == 0:
    taxi += s1 // 4
else:
    taxi += s1 // 4 + 1
print(taxi)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241016221752173](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241016221752173.png)



### *230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：优化埃氏筛法+pypy可以过，一开始犯了很蠢的错误，指使用素数列表而不是每个数是否为素数的那个列表去筛，导致一开始甚至不如n**0.5暴力筛（只能过16，暴力最多过35）。



代码

```python
def ai_shi(m):
    is_prime = [True for _ in range(m + 1)]
    is_prime[0] = is_prime[1] = False
    prime = []
    for i in range(2,m + 1):
        if is_prime[i]:
            prime.append(i)
            for j in range(i * i,m + 1,i):
                is_prime[j] = False
    return is_prime
is_prime_list = tuple(ai_shi(1000000))
def is_square(m):
    return int(m ** 0.5) ** 2 == m
n = int(input())
test1 = list(map(int,input().split()))
print_list = []
for test in test1:
    if is_square(test) and is_prime_list[int(test**0.5)]:
        print_list.append('YES')
    else:
        print_list.append('NO')
for i in print_list:
    print(i)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241016213707604](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241016213707604.png)

### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：在对lambda的用法有新知识后就很直线了，一开始WA是使用lambda是少敲了一个+1，导致排序时优先按照输入整数排



代码

```python
n = int(input())
num = list(map(str,input().split()))
num_and_dec = [[num[i]] for i in range(n)]
m = max([len(num[i]) for i in range(n)])
for i in range(n):
    for j in range(m):
        num_and_dec[i].append(num[i][(j+1) % len(num[i]) - 1])
num_and_dec.sort(key = lambda x:[x[i+1] for i in range(m)])
print(''.join(num_and_dec[i-1][0] for i in range(len(num),0,-1)),''.join(num_and_dec[i][0] for i in range(len(num))))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241016230202001](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241016230202001.png)

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

代码熟练度还不是很高，最近练了一些简单题目提升代码熟练度，同时也学会了更多的python内置函数，如对lambda的理解更深了。做了一些洛谷的贪心题目，对递归的了解感觉也变深了一些


# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>熊程宇 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：

需要注意的点蛮多，比如题给数据要取余，最终结果要到d+m+1（这个是10.20没有做出来的主要原因……）

代码：

```python
count = 1
while True:
    p,e,i,d = map(int,input().split())
    if [p,e,i,d] == [-1,-1,-1,-1]:
        break
    p = p % 23;e = e % 28;i = i % 33
    m = 21252
    for k in range(d + 1,d + m + 1):
        if (k-p) % 23 == 0 and (k - e) % 28 == 0 and (k - i) % 33 == 0:
            print(f'Case {count}: the next triple peak occurs in {k - d} days.')
            break
    count += 1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241029175235038](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241029175235038.png)



### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：

我没想到竟然一遍过了……

由于只需要保证种类，所以尽量制作价格低的，卖出价格高的，故先排序，然后使用双指针（这叫对撞指针吗）。

本来觉得自己在边界有问题，结果过了，应该是因为尽管m = -1，但卖出价格更高的后必然可以买进价格更低的，所以while循环后的判断条件把m调回0了，就AC了

代码：

```python
p = int(input())
p_n = list(map(int,input().split()))
n = len(p_n)
p_n.sort()
m = 0
i = 0
j = n - 1
while i != j:
    if m < 0:
        break
    if p >= p_n[i]:
        m += 1
        p -= p_n[i]
        i += 1
    else:
        m -= 1
        p += p_n[j]
        j -= 1
if p >= p_n[i]:
    m += 1
print(m)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241029195720634](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241029195720634.png)



### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：

意外发现之前在洛谷上做过

代码：

```python
n = int(input())
t = list(map(int,input().split()))
t1 = []
for i in range(n):
    t1.append([t[i],i + 1])
t1.sort(key = lambda x:x[0])
wait = [0]
for i in range(n-1):
    wait.append(wait[i] + t1[i][0])
print(' '.join(str(t1[i][1]) for i in range(n)))
print(f'{sum(wait)/ n:.2f}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



<img src="C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241029201057108.png" alt="image-20241029201057108" style="zoom:200%;" />

### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：

这题怎么这么长啊……

笑点解析：RE半天还真是因为题目太长了，月份有19个，没注意到第十九个月份没跟前面18个连在一起，所以复制就漏了，问GPT才知道问题

代码：

```python
haab = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu','uayet']
tzolkin = ['imix','ik','akbal','kan','chicchan','cimi','manik','lamat','muluk','ok','chuen','eb','ben','ix','mem','cib','caban','eznab','canac','ahau']
n = int(input())
print(n)
for i in range(n):
    day,month,year = map(str,input().split())
    month = haab.index(month)
    day = day[:-1]
    all = int(year) * 365 + 20 * month + int(day)
    print(all % 13 + 1,tzolkin[all % 20],all // 260)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241029212720752](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241029212720752.png)

### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：

尽可能往一个方向倒，不能就换一个方向，左右两边的直接加就行

通过更新占用位置来判断

代码：

```python
n = int(input())
tree = []
for _ in range(n):
    xi, hi = map(int, input().split())
    tree.append([xi, hi])
if n == 1:
    print(1)
    exit()
m = 2
p = tree[0][0]
for i in range(1, n - 1):
    x, h = tree[i]
    if x - h > p:
        m += 1
        p = x
    elif x + h < tree[i+1][0]:
        m += 1
        p = x + h
    else:
        p = x
print(m)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241029222522533](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241029222522533.png)



### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：

询问GPT处理空行方式，对区间排序，然后每次都把雷达放在最右侧，

代码：

```python
from math import sqrt
case_number = 1
while True:
    line = input().strip()
    if not line:
        continue
    n, d = map(float, line.split())
    n = int(n)
    if n == 0:
        break
    x, y = [], []
    for _ in range(n):
        xi, yi = map(float, input().split())
        x.append(xi)
        y.append(yi)
    if max(y) > d:
        print(f'Case {case_number}: -1')
    else:
        x_c = []
        r = 0
        for i in range(n):
            x_c.append([x[i] - sqrt(d ** 2 - y[i] ** 2), x[i] + sqrt(d ** 2 - y[i] ** 2)])
        x_c.sort(key=lambda x: x[1])
        end = -float('inf')
        for interval in x_c:
            if interval[0] > end:
                r += 1
                end = interval[1]
        print(f'Case {case_number}: {r}')
    case_number += 1

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241029225239476](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241029225239476.png)

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

期中事情略多，这次作业赶ddl……雷达还不太做得来，之后得花时间补每日选做了。




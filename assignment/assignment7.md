# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>熊程宇 物理学院</mark>



**说明：**

⽉考： AC4 



## 1. 题目

### E07618: 病人排队

sortings, http://cs101.openjudge.cn/practice/07618/

代码：

```python
n = int(input())
p = []
for i in range(n):
    a,b = map(str,input().split())
    p.append([a,int(b)])
p1 = sorted(p,key = lambda x:x[1] ,reverse = True)
p2 = []
for i in range(len(p1)):
    if p1[i][1] >= 60:
        p2.append(p1[i][0])
for i in range(len(p2)):
    print(p2[i])
for i in range(len(p)):
    if p[i][1] < 60:
        print(p[i][0])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107190054220](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241107190054220.png)



### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

代码：

```python
n,m1,m2 = map(int,input().split())
matrix_1 = [[0 for _ in range(n)] for _ in range(n)]
matrix_2 = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m1):
    x,y,k = map(int,input().split())
    matrix_1[x][y] = k
for i in range(m2):
    x,y,k = map(int,input().split())
    matrix_2[x][y] = k
p = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            p[i][j] += matrix_1[i][k] * matrix_2[k][j]
for i in range(n):
    for j in range(n):
        if p[i][j] != 0:
            print(i,j,p[i][j]
```



代码运行截图 ==（至少包含有"Accepted"）==



![image-20241107190139624](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241107190139624.png)

### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：

一直WA，直到最后才发现时间忘记排序，着实没有想明白为什么看了那么多组测试数据都没发现……

代码：

```python
case = int(input())
for _ in range(case):
    n,m,b = map(int,input().split())
    skill = []
    time = []
    for _ in range(n):
        ti,xi = map(int,input().split())
        time.append(ti)
        skill.append([ti,xi])
    skill.sort(key = lambda x:(x[0],-x[1]))#获得的技能按照时间从小到大排序，对于同一个时间，按照技能值从大到小排序
    skill1 = [skill[0][1]]
    time = sorted(list(set(time)))
    k = 1
    for i in range(1,n):
        if skill[i][0] != skill[i-1][0]:
            k = 1
            skill1.append(skill[i][1])
        elif skill[i][0] == skill[i-1][0] and k < m:
            skill1[-1] += skill[i][1]
            k += 1
    skill1 = [[time[i],skill1[i]] for i in range(len(skill1))]
    a = True
    for i in range(len(skill1)):
        b -= skill1[i][1]
        if b <= 0:
            print(skill1[i][0])
            a = False
            break
    if a:
        print('alive')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241107190243855](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241107190243855.png)

### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：

无法兑换需要单独弄出来判断

代码：

```python
n,m = map(int,input().split())
p = list(map(int,input().split()))
dp = [1 if i in p else -1 for i in range(m + 1)]
for i in range(max(p),m + 1):
    p_list = [i-k for k in p]
    dp_list = [dp[i-k] + 1 for k in p if dp[i-k] != -1]
    if len(dp_list) == 0:
        dp[i] = -1
    else:
        dp[i]  = min(dp_list)
print(dp[m]
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107190617705](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241107190617705.png)



### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：

负号单独判断

代码：

```python
number = list(map(str,input().split()))
number1 = 0
dict1 = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90, 'hundred':100, 'thousand':1000, 'million':1000000}
neg = False
c = 0
r = 0
for i in number:
    if i == 'negative':
        neg = True
    elif i in dict1:
        v = dict1[i]
        if v == 100:
            c *= 100
        elif v == 1000 or v == 1000000:
            r += c * v
            c = 0
        else:
            c += v
r += c
if neg:
    print(-1 * r)
else:
    print(r)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107190708352](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241107190708352.png)



### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：

贪心贪错了……直接按照从前往后贪心就行

代码：

```python
n = int(input())
act = []
for i in range(n):
    start,end = map(int,input().split())
    act.append([start,end,end - start + 1])
act.sort(key = lambda x:x[1])
vac = [0 for _ in range(61)]
m = 0
for i in range(len(act)):
    if vac[act[i][0]:act[i][1]+1].count(1) == 0:
        vac[act[i][0]:act[i][1]+1] = [1 for i in range(act[i][2])] 
        m += 1
print(m)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107190530091](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241107190530091.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

只有AC4……代码熟练度还很不足，需要在期中后增加练习。

好消息是接下来几周有时间练了……




# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

熊程宇 物理学院

Oct⽉考： AC5

## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/



思路：一开始想列列表，然后发现麻烦，于是最后用ASCII来进行转换



代码

```python

k = int(input())
k = k % 26
code = [i for i in input()]
for i in range(len(code)):
    if (ord(code[i]) >= 65 + k and ord(code[i]) <= 90) or ord(code[i]) >= 97 + k:
        code[i] = chr(ord(code[i]) - k)
    else:
        code[i] = chr(ord(code[i]) + 26 - k)
print(''.join(i for i in code))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241012120820022](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241012120820022.png)



### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/



思路：过于简单



代码

```python
a,b = map(str,input().split())
a = int(a[0:2])
b = int(b[0:2])
print(a+b)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241012120854574](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241012120854574.png)



### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/



思路：也许我应该使用字典



代码

```python
n = int(input())
para = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
x_list = ['1','0','X','9','8','7','6','5','4','3','2']
for _ in range(n):
    string = input()
    x_number = x_list.index(string[-1])
    number = [int(string[i]) for i in range(len(string) - 1)]
    m = 0
    for i in range(len(number)):
        m += para[i] * number[i]
    m = m % 11
    if m == x_number:
        print('YES')
    else:
        print('NO')

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

突然发现这样截屏好废……

![image-20241012122138120](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241012122138120.png)

### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/



思路：无脑代码原题



代码

```python

n = int(input())
while n != 1:
    if n % 2 == 0:
        print(f'{n}/2={int(0.5 * n)}')
        n = int(0.5 * n)
    else:
        print(f'{n}*3+1={3 * n + 1}')
        n = 3 * n + 1
print('End')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==



![image-20241012122223235](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241012122223235.png)

### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/



思路：应该使用字典的，但是考试的时候我还不会，于是就调了很久。

罗马到数字：从前往后逐个判断并且加上去

数字到罗马：从大到小一项项转换并且减掉，问题在于转换需要判断4跟9，略麻烦



##### 代码

```python
rome_list = ['I','V','X','L','C','D','M']
number_list = [1,5,10,50,100,500,1000]
rome_list1 = ['IV','IX','XL','XC','CD','CM']
number_list1 = [4,9,40,90,400,900]
n = input()
def r2n(num):
    output = 0
    while len(num) != 0:
        if ''.join(n[0:2]) not in rome_list1:
            output += number_list[rome_list.index(num[0])]
            num.pop(0)
        else:
            output += number_list1[rome_list1.index(''.join(n[0:2]))]
            num.pop(0)
            num.pop(0)
    return output
def n2r(num):
    output = ''
    n = len(number_list)
    for i in range(n):
        if num // number_list[n - 1 - i] > 0 and str(num)[0] != '4' and str(num)[0] != '9':
            output += rome_list[n - 1 - i] * (num // number_list[n - 1 - i])
            num -= number_list[n - 1 - i] * (num // number_list[n - 1 - i])
        elif num // number_list[n - 1 - i] > 0 and (str(num)[0] == '4' or str(num)[0] == '9'):
            output += rome_list1[n - 1 - i]
            num -= number_list1[n - 1 - i]
    return output
if ord(n[-1]) > 57:
    n = [i for i in n]
    print(r2n(n))
else:
    n = int(n)
    print(n2r(n))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==



![image-20241012122558726](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241012122558726.png)

### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/



思路：只会写是个人都会写的暴力排序代码，没有什么放上来的价值



代码

```python


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

超时



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

代码熟练度还不够，并且感觉做题容易心急，导致经常大幅删减代码。以后应该先思考清楚再敲代码。

目前的代码能力离最后一题还过于遥远，并不想死磕这种，目前找了一些简单些的贪心题目练习，每日选做跟进。










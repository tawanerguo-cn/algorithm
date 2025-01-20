n = int(input())
list_a = ['A','B','C','D','E','F','G','H','I','J','K','L']
for _ in range(n):
    l = ['', '', '']
    r = ['', '', '']
    cond = ['', '', '']
    l[0], r[0], cond[0] = map(str, input().split())
    l[1], r[1], cond[1] = map(str, input().split())
    l[2], r[2], cond[2] = map(str, input().split())
    #现在对于每个硬币是真还是轻或者重判断
    for i in list_a:
        is_light = True
        is_heavy = True
        for j in range(3):
            if cond[j] == 'even':
                if i in l[j] or i in r[j]:
                    is_light = False
                    is_heavy = False
            elif cond[j] == 'up':
                if i in l[j]:
                    is_light = False
                if i in r[j]:
                    is_heavy = False
                if i not in l[j] and i not in r[j]:
                    is_light = False
                    is_heavy = False
            elif cond[j] == 'down':
                if i in l[j]:
                    is_heavy = False
                if i in r[j]:
                    is_light = False
                if i not in l[j] and i not in r[j]:
                    is_light = False
                    is_heavy = False
        if is_light:
            print(f'{i} is the counterfeit coin and it is light.')
            break
        if is_heavy:
            print(f'{i} is the counterfeit coin and it is heavy.')
            break
#一定能找出假币，对于所有可能的假币情况枚举，找到符合条件的假币情况就输出
#所以枚举一定是枚举这枚硬币轻或者重，枚举其为真币是错误的想法
#枚举这枚硬币为轻时，若验证发现其出现在even两侧，或者没有出现在up/down的判断里面，或者up/down反了，就枚举下一种情况
#一旦发现三种情况都能符合，就输出，然后跳出循环
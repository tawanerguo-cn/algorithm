#代码能力有待提升……
n,l = map(int,input().split())
a = list(map(int,input().split()))
a_ = sorted(list(set(a)))
b = [0]
for i in range(len(a_)-1):
    b.append(a_[i+1] - a_[i])
print(max(max(b) * 0.5,a_[0],l - a_[-1]))
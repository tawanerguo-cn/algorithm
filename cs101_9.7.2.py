l,m = map(int,input().split())
tree = [1 for _ in range(l+1)]
for i in range(m):
    start,end = map(int,input().split())
    for j in range(start,end+1):
        tree[j] = 0
print(tree.count(1))
w=int(input())
if w%2==0 and w>=4:
    print("YES")
elif w%2!=0 and w>=4:
    print("NO")
elif w==1 or w==2 or w==3:
    print("NO")
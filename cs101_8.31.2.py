n,k,l,c,d,p,nl,np = map(int,input().split())
volume = k * l
number_1 = volume // (n * nl)
slices = c * d
number_2 = slices // n
number_3 = p // (n * np)
print(min(number_1,number_2,number_3))

n = int(input())
for _ in range(n):
    a,b,c = map(float,input().split())
    if b**2 - 4*a*c > 0:
        x1 = (-b)/(2*a) + ((b**2 - 4*a*c)**0.5)/(2*a)
        x2 = (-b)/(2*a) - ((b**2 - 4*a*c)**0.5)/(2*a)
        print(f'x1={x1:.5f};x2={x2:.5f}')
    if b**2 - 4*a*c == 0:
        x1 = (-b)/(2*a)
        print(f'x1=x2={x1:.5f}')
    if b**2 - 4*a*c < 0:
        Re = (-b)/(2*a)
        Im = ((-b**2 + 4*a*c)**0.5)/(2*a)
        print(f'x1={Re:.5f}+{Im:.5f}i;x2={Re:.5f}-{Im:.5f}i')
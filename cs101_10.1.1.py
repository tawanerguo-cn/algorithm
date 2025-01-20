n = int(input())
def fib():
    a = 1
    b = 1
    fib = [a,b]
    for i in range(30):
        fib.append(a+b)
        a,b = b,a+b
    return fib
for _ in range(n):
    m = int(input())
    print(fib()[m-1])
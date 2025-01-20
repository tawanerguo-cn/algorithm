t = input()
a = True
for i in range(int(0.5 * len(t)),len(t)-1):
    if t[0:i] == t[len(t) - i - 1:len(t) - 1]:
        print('YES')
        print(t[0:i+1])
        a = False
        break
if a:
    print('NO')
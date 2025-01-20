s = input()
m = [1]
for i in range(1,len(s)):
    if s[i-1] != s[i]:
        m[-1] += 1
    else:
        m.append(1)
print(max(m))
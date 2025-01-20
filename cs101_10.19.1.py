haab = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu','uayet']
tzolkin = ['imix','ik','akbal','kan','chicchan','cimi','manik','lamat','muluk','ok','chuen','eb','ben','ix','mem','cib','caban','eznab','canac','ahau']
n = int(input())
print(n)
for i in range(n):
    day,month,year = map(str,input().split())
    month = haab.index(month)
    day = day[:-1]
    all = int(year) * 365 + 20 * month + int(day)
    print(all % 13 + 1,tzolkin[all % 20],all // 260)
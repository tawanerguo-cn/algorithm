string_1=input().lower()
string_2=input().lower()
string_1_split=list(map(str,string_1))
string_2_split=list(map(str,string_2))
if string_1_split == string_2_split:
    print(0)
    exit()
else:
    for i in range(len(string_1_split)):
        if string_1_split[i] == string_2_split[i] and i!=len(string_1_split):
            pass
        if ord(string_1_split[i]) > ord(string_2_split[i]):
            print(1)
            exit() 
        if ord(string_1_split[i]) < ord(string_2_split[i]):
            print(-1)
            exit()

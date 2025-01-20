string_input = input().lower()
string_list = [i for i in string_input]
vowels = ['a','o','y','e','u','i']
string_outlist = []
for i in range(len(string_list)):
    if string_list[i] not in vowels:
        string_outlist.append('.')
        string_outlist.append(string_list[i])
print(''.join(i for i in string_outlist))
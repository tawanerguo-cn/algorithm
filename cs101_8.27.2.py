username=input()
class_letter={}
for i in username:
    class_letter[i]=class_letter.get(i,0)+1
if len(class_letter)%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')


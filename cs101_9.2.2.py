word = input()
word_list = [i for i in word]
if 97 <= ord(word_list[0]) <= 122 :
    word_list[0] = chr(ord(word_list[0])-32)
print(''.join(i for i in word_list))

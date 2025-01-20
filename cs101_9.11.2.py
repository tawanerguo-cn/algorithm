direction = input()
dic_letter = {}
keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'
list_keyboard = [i for i in keyboard]
keyboard_right = '0qwertyuio0asdfghjkl0zxcvbnm,.'
keyboard_left = 'wertyuiop0sdfghjkl;0xcvbnm,./0'
list_right = [i for i in keyboard_right]
list_left = [i for i in keyboard_left]
list_input = [i for i in input()]
list_output = []
if direction == 'R':
    for i in list_input:
        list_output.append(list_right[list_keyboard.index(i)])
    print(''.join(i for i in list_output))
if direction == 'L':
    for i in list_input:
        list_output.append(list_left[list_keyboard.index(i)])
    print(''.join(i for i in list_output))
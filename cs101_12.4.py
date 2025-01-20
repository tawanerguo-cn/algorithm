stack = []
min_stack = []
while True:
    try:
        move = input().split()
        if move[0] == 'push':
            a = int(move[1])
            stack.append(a)
            if not min_stack or a <= min_stack[-1]:
                min_stack.append(a)
        elif move[0] == 'pop':
            if stack:
                a = stack.pop()
                if min_stack and min_stack[-1] == a:
                    min_stack.pop()
        elif move[0] == 'min':
            if stack:
                print(min_stack[-1])
    except EOFError:
        break
pig = []
min_stack = []

while True:
    try:
        command = input().split()
        if command[0] == 'push':
            weight = int(command[1])
            pig.append(weight)
            if not min_stack or weight <= min_stack[-1]:
                min_stack.append(weight)
        elif command[0] == 'pop':
            if pig:
                removed = pig.pop()
                if min_stack and removed == min_stack[-1]:
                    min_stack.pop()
        elif command[0] == 'min':
            if min_stack:
                print(min_stack[-1])
    except EOFError:
        break

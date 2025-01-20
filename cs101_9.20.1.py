while True:
    try:
        email = input().split()
        email_list = [i for i in email[0]]
        if email_list.count('@') == 1 and \
        email_list[0] != '@' and email_list[0] != '.' and \
        email_list[-1] != '@' and email_list[-1] != '.' and \
        email_list[email_list.index('@') + 1] != '.' and email_list[email_list.index('@') - 1] != '.' and \
        email_list[email_list.index('@') + 1:-1].count('.') >= 1:
            print('YES')
        else:
            print('NO')
    except EOFError:
        break
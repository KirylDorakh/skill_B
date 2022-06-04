correct_login = 'admin'
correct_pass = 'pass'

k = 3

for i in range(k - 1):
    login = input('input login: ')
    password = input('input password: ')
    k -= 1

    if login != correct_login or password != correct_pass:
        print(f'Wrong login or password. You have {k} try')
    else:
        print('Welcome')
        break
if k == 0:
    print('Entrance blocked')

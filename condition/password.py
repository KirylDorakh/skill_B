login_list = [
   'root',
   'username1'
   ]

password_list = {
   'root': '1q2w3e4r',
   'username1': 'qwerty123'
}

username = input('Введите логин:\n')
if username in login_list:
    print("correct username")
    password = input('Введите пароль:\n')
    if password_list[username] == password:
        print('correct password')
    else:
        print('not correct password')
else:
    print('not correct username')
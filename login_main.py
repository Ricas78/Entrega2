from subclass_user_default import default
from subclass_user_moderator import mod
from subclass_user_administrator import adm
import re

users = []
users.append(default('user1', 'password1'))
users.append(mod('user2', 'password2'))
users.append(adm('user3', 'password3'))

username = input('Digite seu nome de usuário: ')

while True:
    try:
        if not re.match(r'^\w+$', username):
            raise ValueError
        break
    except ValueError:
        print('O nome de usuário deve conter apenas letras, números e sublinhados')
        username = input('Digite seu nome de usuário: ')

password = input('Digite sua senha: ')

for user in users:
    if user.username == username and user.check_password(password):
        print('Usuário correto')
        user.check_userlevel()
        break
else:
    print('Usuário inválido')
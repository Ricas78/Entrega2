from class_user import User
import hashlib

class default(User):
    def __init__(self, username, password):
        User.__init__(self, username, password, 1)

    def check_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest() == self.password

    def check_userlevel(self):
        print('Usuário com permissão padrão')
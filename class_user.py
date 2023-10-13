import hashlib

class User:
    def __init__(self, username, password, levels):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.levels = levels
    
    def check_password(self,password):
        pass

    def check_userlevel(self):
        pass
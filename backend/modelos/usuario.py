# backend/models/usuario.py
class Usuario:
    def __init__(self, username, password):
        self.username = username
        self._password = password

    def autenticar(self, pwd):
        return self._password == pwd

class Moderador(Usuario):
    def __init__(self, username, password):
        super().__init__(username, password)

    def autenticar(self, pwd):
        if pwd.startswith("mod_"):
            return super().autenticar(pwd)
        return False

import re

class Admin(Usuario):
    def __init__(self, username, password):
        super().__init__(username, password)

    def autenticar(self, pwd):
        # Comprobamos si la contraseña tiene al menos un carácter especial
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd):
            return super().autenticar(pwd)
        return False

def login(usuario: Usuario, pwd: str) -> bool:
    return usuario.autenticar(pwd)

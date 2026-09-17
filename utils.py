from models import User

def enter_username():
    input('Introduce el nombre de usuario')

def enter_password():
    input('Introduce la constraseña')

def is_username(registration:list, new_user:User)->bool:
    found = False
    for i in registration:
        if registration[i].username == new_user.username:
            found = True
    return found


def verify_login(registration, username, password):
    return registration[password] == password
    
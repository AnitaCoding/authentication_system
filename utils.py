from models import User

def enter_username():
    input('Introduce el nombre de usuario')

def enter_password():
    input('Introduce la constraseña')

def is_username(registration:list, new_user)->bool:
    found = False
    for i in range(len(registration)):
        if registration[i]['nickname'] == new_user:
            found = True
            print(found)
    return found

def add_user(new_user, registration):
    registration.update(new_user)


def verify_login(registration, username, password):
    return registration[password] == password
    
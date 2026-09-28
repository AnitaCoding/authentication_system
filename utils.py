#from models import User

def enter_username():
    return input('Introduce el nombre de usuario: ')

def enter_password():
    return input('Introduce la constraseña: ')

def add_user(new_user, registration):
    registration.update(new_user)


def verify_login(registration, username, password):
    return registration[password] == password
    
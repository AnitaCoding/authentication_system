from utils import *
from models import *
users_list = [{'nickname':'Ana', 'password': 'mypassword', 'role':'admin'},
              {'nickname':'David', 'password': 'mypassword', 'role':'customer'},
              {'nickname':'Carmen', 'password': 'mypassword', 'role':'customer'}]

authentication = True

while authentication:
    print('---Elige una opción---')
    print('1. Registrar nuevo usuario.')
    print('2. Iniciar sesión.')
    print('3. Salir')
    chosen_option = input('Inserta la opción elegida ')

    if chosen_option == '1':
        username = enter_username
        if not is_username(users_list, username):
            print('Usuario no encontrado. Contacte con el administrador del sitio')

        else:
            current_user = User() #Hay que saque al usuario de la lista y lo almacene aquí.
            password = enter_password()
            
    elif chosen_option == '3':
        authentication = False
    else:
        print('La opción introducida no es correcta. Inténtelo de nuevo')

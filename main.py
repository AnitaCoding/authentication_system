from utils import *
from models import *

users_list = [{'nickname':'Ana', 'password': 'mypassword', 'role':'admin'},
              {'nickname':'David', 'password': 'mypassword', 'role':'customer'},
              {'nickname':'Carmen', 'password': 'mypassword', 'role':'customer'}]

main_menu = True
auth = Authentication()
while main_menu:
    print('---Elige una opción---')
    print('1. Registrar nuevo usuario.')
    print('2. Iniciar sesión.')
    print('3. Salir')
    chosen_option = input('Inserta la opción elegida ')

    if chosen_option == 1:
        print('Registrar usuario')
    elif chosen_option == '2':

        logged_user = auth.log_in(users_list)
        logged_user.show_menu()

            
    elif chosen_option == '3':
        main_menu = False
    else:
        print('La opción introducida no es correcta. Inténtelo de nuevo')

#Dudas: todo lo que podamos convertir en una función, lo separamos del main?
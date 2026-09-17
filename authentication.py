authentication = True

while authentication:
    print('---Elige una opción---')
    print('1. Registrar nuevo usuario.')
    print('2. Iniciar sesión.')
    print('3. Salir')
    chosen_option = input('Inserta la opción elegida')

    if chosen_option == '3':
        authentication = False
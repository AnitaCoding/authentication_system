from utils import *
class User:
    def __init__(self, username):
        self.username = username
        self.password = None
        self.role = None
        self.menu_options = None

    def show_menu(self):
        pass

class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.menu_options = ['1. Ver lista de usuarios','2. Crear nuevo usuario','3. Eliminar usuario']

    def create_new_user(self, registration:list[dict], new_user:User):
        registration.update(new_user)
        
    def delete_user(self, registration:list[dict], u:User):
        registration.pop(u.username)

    def show_menu(self, system):

        while True:
            for i in range(len(self.menu_options)):
                print(self.menu_options[i])
                chosen_option = input('Introduce la opción elegida: ')

            if chosen_option == '1':
                system.registrar_usuarios()
            elif chosen_option == '2':
                system.delete_user()
            elif chosen_option == '3':
                print('Cierre de sesión')
                break
            else:
                print('Opción inválida')


class Customer(User):
    def __init__(self, username):
        super().__init__(username)
        self.menu_options = ['1. Ver lista de productos', '2. Comprar']

    def get_products(self, products:list[dict]):
        print(products)

    def buy_products(self, product):
        print(f'La compra de {product} se ha realizado correctamente')


class Authentication:
    def __init__(self):
        pass

    def registrar_usuario(self):
        pass

    def enter_password(self):
        self.password = input('Introduce la constraseña: ')

    def get_user(self, registration):
        for i in range(len(registration)):
            if registration[i]['nickname'] == self.username:
                self.password = registration[i]['password']
                self.role = registration[i]['role']

    def is_username(self, registration, username):
        found = False
        for i in range(len(registration)):
            if registration[i]['nickname'] == username:
                found = True
        return found

    def log_in(self, users_list):
        username = enter_username()
        if not self.is_username(users_list, username):
            print('Usuario no encontrado. Contacte con el administrador del sitio para registrarlo.')

        else:
            current_user = User(username)
            current_user.get_user(users_list)
            wrong_password = True

            while wrong_password:
                password = enter_password()
                if password == current_user.password:
                    wrong_password = False

        if current_user.role == 'admin':
            logged_user = Admin(username)

        else:
            logged_user = Customer(username)

        return logged_user

    def show_main_menu(self)


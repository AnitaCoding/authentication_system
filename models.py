class User:
    def __init__(self, username, password, role):
        self.username = None
        self.password = None
        self.role = None
        self.menu_options = None

    def enter_username(self):
        self.username = input('Introduce el nombre de usuario')

    def enter_password(self):
        self.password = input('Introduce la constraseña')

    def show_menu(self):
        for i in range(len(self.menu_options)):
            print(self.menu_options[i])
        input('Introduce la opción elegida: ')

class Admin(User):
    def __init__(self):
        super().__init__()
        self.menu_options = ['1. Ver lista de usuarios','2. Crear nuevo usuario','3. Eliminar usuario']
    
    def get_users(self, registration):
        print(registration)

    def create_new_user(self, registration:dict[User], new_user:User):
        registration.update(new_user)
        
    def delete_user(self, registration:dict[User], u:User):
        registration.pop(u.username)
        
class Customer(User):
    def __init__(self):
        super().__init__()
        self.menu_options = ['1. Ver lista de productos', '2. Comprar']

    def get_products(self, products):
        print(products)

    def buy_products(self, product):
        print(f'La compra de {product} se ha realizado correctamente')

'''
adm = Admin()
adm.show_menu()
'''

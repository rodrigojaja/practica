class User():
    is_registered = True

    def __init__(self, name, login):
        self.user_name = name
        self.user_login = login

    def describe(self):
        return f'Nombre: {self.user_name}, iniciar sesión {self.user_login}'


class Group():
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, user):
        if user not in self.members:
            print(f'Se ha agregado un nuevo miembro al grupo {self.name}')
            self.members.append(user)

    def print_member_descriptions(self):
        print(f'Información sobre los miembros del grupo {self.name}:')
        for member in self.members:
            print(member.describe())

user1 = User('Mark', 'supermarkus94') # Crear un usuario o usuaria
group1 = Group('Dog Lovers') # Crear un grupo de amantes de los perros
group1.add_member(user1) # Agregar un nuevo usuario o usuaria al grupo
user1_description = group1.members[0].describe() # Guardar la descripción del usuario o usuaria
print(user1_description) # Mostrar la descripción
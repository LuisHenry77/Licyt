class Usuarios:

    tipo_usuario = "Free"
    publicidad = True

    def __init__(self, carnet, alias, nombre, apellidos):
        self.carnet = carnet
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos

    def muestra_datos(self):
        print("El nombre y los apellidos del usuario son: " + self.nombre, self.apellidos)
        print("El número de carnet es:" + self.carnet + ".")
        print("El alias del usuario es: " + self.alias)

class UsuariosPremium(Usuarios):
    tipo_usuario = "Premium"
    publicidad = False
    participacion_sorteos = 10

class UsuariosPremiumPluss(UsuariosPremium):
    participacion_sorteos = 25

usuario1=Usuarios("001", "Carlox77","Carlos", "Mamani Mamani")

usuario2=UsuariosPremium("002", "H3NRY", "Luis Henry", "Flores Soliz")

usuario3=UsuariosPremiumPluss("003","pedritoxx","Pedro","Hernández Salvatore")

usuario3.muestra_datos()

print(usuario2.participacion_sorteos)
print(usuario3.participacion_sorteos)



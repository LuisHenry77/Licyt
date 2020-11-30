class Musica:
    def __init__(self, banda, integrantes, genero, pais):
        self.banda = banda
        self.integrantes = integrantes
        self.genero = genero
        self.pais = pais

    def cantar(self):
        return f"Hola somos el grupo {self.banda}, somos {self.integrantes}, nuestro estilo es de {self.genero}, somos de {self.pais}"
class grupo(Musica):
    def grupo(self):
        return f"Hola somos la banda {self.banda}, somos {self.integrantes}, hacemos musica de {self.genero}, somos de {self.pais}"

class grupo(Musica):
    def grupo(self):
        return f"Hola somos el grupo {self.banda}, somos {self.integrantes}, hacemos musica de {self.genero}, somos de {self.pais}"

grupo = Musica ("Twenty One Pilots", "Tyler Josep, Josh Dun, Nick Thomas, Chris Salih", "Rap alternativo, Electropop,etc", "Columbus, Ohio")
print(grupo.cantar())


canciones = Musica("Foster The People", "Mark Foster, Mark Pontius, Danyew, Jacob Fink", "Indie Pop, Rock alternativo", "Los Angeles, California")
print(canciones.cantar())


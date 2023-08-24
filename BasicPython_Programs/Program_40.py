# Created by: Brayan Adrian Galvan Flores #

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.amigos = []
        self.publicaciones = []

    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)
        amigo.amigos.append(self)

    def hacer_publicacion(self, contenido):
        publicacion = Publicacion(self, contenido)
        self.publicaciones.append(publicacion)

    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print("Amigos:")
        for amigo in self.amigos:
            print(amigo.nombre)
        print("Publicaciones:")
        for publicacion in self.publicaciones:
            print(f"{publicacion.autor.nombre}: {publicacion.contenido}")


class Publicacion:
    def __init__(self, autor, contenido):
        self.autor = autor
        self.contenido = contenido


# Crear usuarios
usuario1 = Usuario("Usuario1", 25)
usuario2 = Usuario("Usuario2", 30)

# Conectar usuarios como amigos
usuario1.agregar_amigo(usuario2)

# Hacer publicaciones
usuario1.hacer_publicacion("¡Hola a todos! Esta es mi primera publicación.")
usuario2.hacer_publicacion("Saludos, amigos. ¡Feliz día!")

# Mostrar perfiles
usuario1.mostrar_perfil()
print("\n")
usuario2.mostrar_perfil()

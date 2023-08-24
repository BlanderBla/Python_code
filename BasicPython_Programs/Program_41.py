from os import system

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.libro = {
            "titulo": "",
            "autor": "",
            "isbn": "",
            "editorial": "",
            "anio": 0,
            "descripcion": ""
        }

        self.izquierda = None
        self.derecha = None

class Arbol:
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __agregar_recursivo(self, nodo, dato, libro_datos):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
                nodo.izquierda.libro = libro_datos
            else:
                self.__agregar_recursivo(nodo.izquierda, dato, libro_datos)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
                nodo.derecha.libro = libro_datos
            else:
                self.__agregar_recursivo(nodo.derecha, dato, libro_datos)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, nodo.libro)
            self.__inorden_recursivo(nodo.derecha)

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)
        

    # Funciones públicas
    def agregar(self, dato, libro_datos):
        self.__agregar_recursivo(self.raiz, dato, libro_datos)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)

def menu():
    system("cls")
    print("LIBROS\n\t1. Agregar\n\t2. Buscar\n\t3. Salir\n\t")
    return int(input(" > "))

def agregar_libro():
    titulo = input("\tTitulo del libro: ")
    autor = input("\tAutor del libro: ")
    isbn = input("\tISBN del libro: ")
    editorial = input("\tEditorial del libro: ")
    anio = int(input("\tAño del libro: "))
    descripcion = input("\tDescripcion del libro: ")
    libro = {
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "editorial": editorial,
        "anio": anio,
        "descripcion": descripcion
    }
    return libro

arbol = Arbol("")
count = 0
opc = menu()
while opc != 3:
    if opc == 1:
        system("cls")
        print("AGREGAR\n")
        count += 1        
        libro_datos = agregar_libro()
        arbol.agregar(str(count),libro_datos)
    elif opc == 2:
        system("cls")
        print("BUSCAR\n")
        arbol.inorden()
        x = input("Presiona cualquier tecla para continuar >")
    elif opc == 3:
        system("cls")
        print("SALIR\nPresiona una tecla para salir")
    opc = menu()
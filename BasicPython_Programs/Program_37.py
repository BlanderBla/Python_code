# Created by: Brayan Adrian Galvan Flores #

class Calculadora:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def suma(self):
        print(f"La suma de {self.x} y {self.y} es: {self.x+self.y}")

    def resta(self):
        print(f"La resta de {self.x} y {self.y} es: {self.x-self.y}")

    def multiplicacion(self):
        print(f"El producto de {self.x} y {self.y} es: {self.x*self.y}")

    def division(self):
        print(f"La división de {self.x} y {self.y} es: {self.x/self.y}")


val_1 = int(input("Ingrese el primer valor: "))
val_2 = int(input("Ingrese el segundo valor: "))

operaciones = Calculadora(val_1, val_2)
operaciones.suma()
operaciones.resta()
operaciones.multiplicacion()
operaciones.division()


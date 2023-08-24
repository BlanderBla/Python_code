# Created by: Brayan Adrian Galvan Flores #

import random as rnd

# OBJETO DADO
class Dado:
    def __init__(self, puntaje = 0):
        self.puntaje = puntaje

    def aleatorio(self):
        self.puntaje = rnd.randint(1,6)
        return self.puntaje

# OBJETO PERSONA
class Persona:
    def __init__(self,nombre, intento):
        self.nombre = nombre
        self.intento = intento
        self.valor = 0

    def decremento(self):
        self.intento = self.intento - 1
        return self.intento
    
    def cantidad(self, valor):
        self.valor += valor
        return self.valor

i = 0
n = int(input("Ingrese la cantidad de personas a jugar: "))
x = int(input("Ingrese la cantidad de intentos a jugar: "))

dicJugadores = {}
while i != n:
    nombre = input(f"Nombre del jugador {i}: ")
    dicJugadores[nombre] = x
    i = i + 1

print(dicJugadores)

listJugador = []
jugar = Dado()
for nombre, intento in dicJugadores.items():
    jugador = Persona(nombre, intento)
    print(f"Jugador: {jugador.nombre} - Intentos: {jugador.intento}")
    i = jugador.intento
    while i > 0:
        partida = jugador.decremento()
        valor = jugar.aleatorio()
        print(f"Intento {partida}: {valor}")
        x= jugador.cantidad(valor)
        i = i - 1
    print(f"Puntos: {x}\n")
    listJugador.append(jugador)

for i in listJugador:
    print(f"-----\nNombre: {i.nombre}\nIntentos: {i.intento}\nPuntuación: {i.valor}")
# Created by: Brayan Adrian Galvan Flores #

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de ${monto} realizado. Saldo actual: ${self.saldo}")
        else:
            print("Monto inválido para depósito.")
    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de ${monto} realizado. Saldo actual: ${self.saldo}")
        else:
            print("Fondos insuficientes o monto inválido para retiro.")
    def obtener_saldo(self):
        return self.saldo


class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []
    def abrir_cuenta(self, titular, saldo_inicial=0):
        cuenta = CuentaBancaria(titular, saldo_inicial)
        self.cuentas.append(cuenta)
        print(f"Cuenta creada para {titular} en el banco {self.nombre}.")
    def buscar_cuenta(self, titular):
        for cuenta in self.cuentas:
            if cuenta.titular == titular:
                return cuenta
        return None


banco = Banco("MiBanco")
while True:
    print("\n1. Abrir cuenta")
    print("2. Realizar depósito")
    print("3. Realizar retiro")
    print("4. Salir")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        titular = input("Ingrese el nombre del titular de la cuenta: ")
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
        banco.abrir_cuenta(titular, saldo_inicial)
    elif opcion == 2:
        titular = input("Ingrese el nombre del titular de la cuenta: ")
        cuenta = banco.buscar_cuenta(titular)
        if cuenta:
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        else:
            print("Cuenta no encontrada.")
    elif opcion == 3:
        titular = input("Ingrese el nombre del titular de la cuenta: ")
        cuenta = banco.buscar_cuenta(titular)
        if cuenta:
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        else:
            print("Cuenta no encontrada.")
    elif opcion == 4:
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

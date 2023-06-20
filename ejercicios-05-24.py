from math import pi
import os
from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

def Limpiar():
    os.system('cls')

def area_rectangulo(base, altura):
    area = base * altura
    print(f"El area del rectangulo es {area}")
    input("Enter para continuar")

def area_circulo(radio):
    area = pi * (radio**2)
    print(f"El area del circulo es {round(area,2)}")
    input("Enter para continuar")

def tabla_multiplicar(numero):
    for i in range(1,13):
        print(f"{i} x {numero}: {i*numero}")
    input("\nEnter para continuar")

status = True

while status:
    Limpiar()
    print("Bienvenido al menu")
    print("Que deseas hacer?")
    print("1- Area rectangulo")
    print("2- Area circulo")
    print("3- Imprimir tabla de multiplicar")
    print("4- Por implementar")
    print("5- Salir")

    option = int(input("Ingrese opcion: "))
    if option == 1:
        Limpiar()
        print("Calcular area de rectangulo\n")
        base = int(input("Ingresa el valor de base: "))
        altura = int(input("Ingresa el valor de altura: "))
        area_rectangulo(base, altura)
    elif option == 2:
        Limpiar()
        print("Calcular area de un circulo\n")
        radio = int(input("Ingrese el valor del radio: "))
        area_circulo(radio)
    elif option == 3:
        Limpiar()
        print("Tabla de multiplicar\n")
        numero = int(input("Ingrese el numero a multiplicar: "))
        Limpiar()
        tabla_multiplicar(numero)
    elif option == 4:
        Limpiar()
        print("Consultar digito verificador\n")
        rut = input("Ingrese su rut, sin puntos ni digito verificador\n")
        dv = digito_verificador(rut)
        inputdv = input("Ingrese su digito verificador")
        if str(dv) == str(inputdv):
            print("Digito verificador valido")
        else:
            print("Digito verificador incorrecto")
        input("Enter para continuar")
    elif option == 5:
        Limpiar()
        print("Gracias por usar la aplicacion\n")
        input("Enter para salir")
        status = False
    else:
        Limpiar()
        print("Ingresa una opcion valida")
import os
import numpy as np
from datetime import date
from itertools import cycle

def limpiar():
    # limpia la pantalla
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def separador_miles(valor):
    desglose = []
    mirrorvalor = list(reversed(str(valor)))

    for n in range(0,len(mirrorvalor)):
        if n % 3 == 0 and n != 0:
            desglose.append(".")
        desglose.append(mirrorvalor[n])
        
    mirrorvalor = ''.join(str(e) for e in desglose)

    return mirrorvalor[::-1]

def menu_principal():
    limpiar()
    print("Productora 'Creativos.cl'")
    print("Venta de entradas 'Michael Jam'\n")
    print("1- Comprar entradas")
    print("2- Mostrar ubicaciones disponibles")
    print("3- Ver listado de asistentes")
    print("4- Mostrar ganancias totales")
    print("5- Salir\n")
    try:
        user_input = int(input("Escoge una opcion: "))
    except ValueError:
        limpiar()
        print("Error\n")
        print("Ingresa una opcion correcta")
        input("Enter para continuar")
        user_input = menu_principal()

    return user_input

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

def validador(rut):
    dv = digito_verificador(rut)
    if dv == 10:
        return 'k'
    else:
        return dv

def ingresar_rut():
    try:
        user_input = int(input("Ingresa el rut sin puntos ni guion ni digito verificador: "))
    except ValueError:
        print("ValueError")
        user_input = 0

    if 4000000 < user_input < 99999999:
        return user_input
    else:
        print("Rut erroneo, ingresa un rut valido")
        user_input = ingresar_rut()
        return user_input

def imprimir_matriz(matriz,x,y):
    matriz = matriz.reshape(x,y)
    shape = matriz.shape

    for i in range(shape[0]):
        for j in range(shape[1]):
            if j == 0:
                print("|",end=" ")
            print(f"{matriz[i][j]}\t",end=" ")
            if j == shape[1]-1:
                print("|")

def ingresar_entero(concepto="valor"):
    try:
        user_input = int(input(f"Ingresa el {concepto}: "))
    except ValueError:
        print("Error")
        user_input = ingresar_entero(concepto)

    return user_input

def comprar_entrada():
    limpiar()
    print("Selecciona tu asiento:\n")
    imprimir_matriz(arreglo,10,10)
    print("")
    asiento = ingresar_entero('numero de asiento')
    if asiento in arreglo:
        if asiento in ubicaciones["platinium"]:
            print(f"El valor de la entrada es: {separador_miles(precios['platinium'])}")
            posiciones[0] += 1
            rut = ingresar_rut()
            arreglo[asiento-1] = 0
            return [rut,asiento]
        elif asiento in ubicaciones["gold"]:
            print(f"El valor de la entrada es: {separador_miles(precios['gold'])}")
            posiciones[1] += 1
            rut = ingresar_rut()
            arreglo[asiento-1] = 0
            return [rut,asiento]
        elif asiento in ubicaciones["silver"]:
            print(f"El valor de la entrada es: {separador_miles(precios['silver'])}")
            posiciones[2] += 1
            rut = ingresar_rut()
            arreglo[asiento-1] = 0
            return [rut,asiento]
    else:
        print("El asiento no es valido")
        input("Enter para continuar")
        return comprar_entrada()
    
def calcular_ganancias(posiciones,precios):
    plati = precios['platinium'] * posiciones[0]
    gold = precios['gold'] * posiciones[1]
    silver = precios['silver'] * posiciones[2]

    print("Tipo de entrada\t\tCantidad\tTotal")
    print(f"Platinium: {separador_miles(precios['platinium'])}\t{posiciones[0]}\t\t{separador_miles(plati)}")
    print(f"Gold: {separador_miles(precios['gold'])}\t\t{posiciones[1]}\t\t{separador_miles(gold)}")
    print(f"Silver: {separador_miles(precios['silver'])}\t\t{posiciones[2]}\t\t{separador_miles(silver)}")
    print(f"TOTAL\t\t\t{sum(posiciones)}\t\t{separador_miles(sum([plati,gold,silver]))}")

    
def imprimir_listado_ordenado(vendidos):
    sorted_holder = dict(sorted(vendidos.items(),key=lambda item:item[1]))
    for key, value in sorted_holder.items():
        print(f"{separador_miles(value)}-{validador(value)} - asiento {key}")



if __name__ == '__main__':
    arreglo = np.arange(1,101)
    precios = {
        'platinium': 120000,
        'gold': 80000,
        'silver': 50000
    }
    ubicaciones = {
        'platinium': np.arange(1,21),
        'gold': np.arange(21,51),
        'silver': np.arange(51,101)
    }
    posiciones = [0,0,0]

    vendidos = {}

    status = True

    while status:
        option = menu_principal()
    
        if option == 1:
            limpiar()
            print('Comprar entradas:\n')
            cant_entradas = ingresar_entero('numero de entradas')
            if 1 <= cant_entradas <= 3:
                for n in range(0,cant_entradas):
                    asiento = comprar_entrada()
                    vendidos[f'{asiento[1]}'] = asiento[0]
            else:
                print("Solo puedes comprar entre 1 y 3 entradas")
                input("Enter para continuar")
        elif option == 2:
            limpiar()
            print("Ubicaciones disponibles")
            imprimir_matriz(arreglo,10,10)
            input("\nEnter para continuar")
        elif option == 3:
            if len(vendidos) == 0:
                limpiar()
                print("Lista de asistentes:\n")
                print("No existen registros")
                input("\nEnter para continuar")
            else:
                limpiar()
                print("Lista de asistentes:\n")
                imprimir_listado_ordenado(vendidos)
                input("\nEnter para continuar")
        elif option == 4:
            limpiar()
            calcular_ganancias(posiciones,precios)
            input("\nEnter para continuar")
        elif option == 5:
            limpiar()
            print("Saliendo del programa\n\n")
            print(f"Creado por: Rodrigo Lopez {date.today()}")
            status = False


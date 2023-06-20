import os
import numpy as np
from itertools import cycle

def limpiar():
    os.system('cls')

def separador_miles(valor):
    desglose = []
    strvalor = str(valor)
    lenvalor = len(strvalor)
    mirrorstrvalor = strvalor[-1::-1]

    for n in range(0,lenvalor):
        if n % 3 == 0 and n != 0:
            desglose.append(".")
        desglose.append(mirrorstrvalor[n])
        
    mirrorstrvalor2 = ''.join(str(e) for e in desglose)
    strvalor = mirrorstrvalor2[-1::-1]

    return strvalor    

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11
 
def ingresar_rut():
    try:
        user_input = int(input("Ingresa el rut: "))
    except ValueError:
        print("ValueError")
        user_input = 0

    if 4000000 < user_input < 99999999:
        return user_input
    else:
        print("Rut erroneo, ingresa un rut valido")
        user_input = ingresar_rut()
        return user_input

def ingresar_celular():
    # Celular: numero entero de largo 9 (len = 9)
    try:
        user_input = int(input("Ingresa el telefono: "))
    except ValueError:
        #print("ValueError")
        print("Ingresa un telefono correcto")
        user_input = 0

    if len(str(user_input)) == 9:
        #print("Telefono valido")
        return user_input
    else:
        print("Telefono invalido")
        user_input = ingresar_celular()
        return user_input
 
def imprimir_matriz(matriz,x,y):
    matriz = matriz.reshape(x,y)
    shape = matriz.shape

    for i in range(shape[0]):
        for j in range(shape[1]):
            if j == 0:
                print("|",end="\t")
            print(f"{matriz[i][j]}\t",end=" ")
            if j == (shape[1]/2)-1:
                print("\t",end=" ")
            if j == shape[1]-1:
                print("|")

def menu_principal():
    limpiar()
    print("Vuelos - Duoc")
    print("Sistema de reserva de asientos\n")
    print("1- Ver asientos disponibles")
    print("2- Comprar asiento")
    print("3- Anular vuelo")
    print("4- Modificar datos de pasajero")
    print("5- Salir\n")
    try:
        user_input = int(input("Escoge una opcion: "))
    except ValueError:
        limpiar()
        print("Value Error")
        print("Ingresa una opcion correcta")
        input("Enter para continuar")
        user_input = menu_principal()

    return user_input

def comprar_asiento(precios, normal, vip):
    print("Seleccion de asiento\n")
    print("Asientos normales")
    imprimir_matriz(normal,5,6)
    print("Asientos vip")
    imprimir_matriz(vip,2,6)
    print("")
    for key, value in precios.items():
        print(f"Asiento {key}\t: ${separador_miles(value)}")
    print("")
    user_input = seleccionar_asiento(arreglo)

    if user_input in normal:
        print(f"\nEl asiento {user_input} tiene un valor de: ${separador_miles(precios['normal'])}\n")
    elif user_input in vip:
        print(f"\nEl asiento {user_input} tiene un valor de: ${separador_miles(precios['vip'])}\n")
    else:
        user_input = comprar_asiento()

    return user_input

def registro_pasajero():
    limpiar()
    print("Registro pasajero\n")
    nombre = input('Ingrese nombre: ')
    rut = ingresar_rut()
    dv = digito_verificador(rut)

    pasajero = {
        'nombre': nombre,
        'rut': rut,
        'dv': dv,
        'telefono': ingresar_celular()
    }

    return pasajero

def seleccionar_asiento(matriz):
    try:
        user_input = int(input("Ingrese el numero de asiento: "))
    except ValueError:
        print("Error, ingrese un numero valido")

    if user_input in matriz:
        #print("Asiento se encuentra disponible")
        return user_input
    else:
        #print("Asiento no se encuentra disponible")
        user_input = seleccionar_asiento()

def busqueda_por_rut(matriz):
    listado = {}
    for key in matriz.keys():
        listado[matriz[key]['rut']] = key

    return listado

if __name__ == '__main__':
    status = True
    substatus = True
    precios = {
        'normal': 78900,
        'vip': 240000
    }
    asientosReservados = {}

    #Creacion de matrices
    arreglo = np.arange(1,43)
    arr_asientos = np.arange(1,43)
    normal = np.arange(1,31)
    vip = np.arange(31,43)
    
    while status:
        opcion = menu_principal()
        if opcion == 1:
            limpiar()
            print("Asientos disponibles\n")
            imprimir_matriz(arreglo,7,6)
            input("\nEnter para continuar")
        elif opcion == 2:
            pasajero = registro_pasajero()
            limpiar()
            print(f"Pasajero {pasajero['nombre']} registrado\n")
            asiento = comprar_asiento(precios,normal, vip)
            user_input = input(f"Confirmar la reserva de {asiento} a nombre de {pasajero['nombre']}? [Si para confirmar]")
            if user_input.lower() == 'si':
                arreglo[asiento-1] = 0
                asientosReservados[asiento] = pasajero
                input("Enter para continuar")
            else:
                print("La reserva no se a concretado, volviendo al menu principal")
                input("\nEnter para continuar")
        elif opcion == 3:
            limpiar()
            print("Anulacion de vuelo\n")
            user_input = seleccionar_asiento(arr_asientos)
            if user_input in asientosReservados:
                cliente = asientosReservados[user_input]
                print(f"\nAsiento {user_input} reservado por {cliente['nombre']}\n")
                resp = input(f"Desea anular la reserva del asiento {user_input}? [Si/No] ")
                if resp.lower() == "si":
                    arreglo[user_input-1] = user_input
                    asientosReservados.pop(user_input)
                    print("La reserva se a anulado")
                    input("\nEnter para continuar")
                else:
                    print("\nVolviendo al menu principal")
                    input("\nEnter para continuar")
            else:
                print("El asiento seleccionado no se encuentra reservado.")
                input("\nEnter para continuar")
            
        elif opcion == 4:
            limpiar()
            listarut = busqueda_por_rut(asientosReservados)
            user_input = ingresar_rut()
            print(listarut)
            if user_input in listarut:
                print("Rut encontrado")
                numero_asiento = listarut[user_input]
                while substatus:
                    limpiar()
                    print(f"Modificacion de datos reserva asiento {numero_asiento}\n")
                    datos = asientosReservados[numero_asiento]
                    print("1- Modificar nombre")
                    print("2- Modificar telefono")
                    print("3- Salir")
                    subopcion = input("\nIngrese opcion: ")
                    if subopcion == '1':
                        new_name = input("Ingrese el nombre: ")
                        datos['nombre'] = new_name
                    elif subopcion == '2':
                        new_num = ingresar_celular()
                        datos['telefono'] = new_num
                    elif subopcion == '3':
                        substatus = False
                    else:
                        print("Ingrese una opcion valida")
                        input("\nEnter para continuar")
                    
            input("Enter para continuar")
            
        elif opcion == 5:
            status = False
        else:
            limpiar()
            print("Ingresa una opcion valida")
            input("Enter para continuar")


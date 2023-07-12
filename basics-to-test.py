# importacion de librerias usadas anteriormente
# si no usaras alguna se recomienda borrarla
import os
import numpy as np
from datetime import timedelta, datetime, date
from itertools import cycle

def limpiar():
    # limpia la pantalla
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def menu_principal():
    """Funcion recursiva que retorna un entero
    print de menu
    comprobacion de input mediante try y except ValueError
    """
    limpiar()
    print("Menu Principal")
    print("opciones\n")
    print("1- ")
    print("2- ")
    print("3- ")
    print("4- \n")
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
    """Funcion que retorna el digito verificador de un rut"""
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

def ingresar_rut():
    """Funcion recursiva que retorna un entero
    comprobacion entre 4.000.000 y 99.999.999"""
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
    """Funcion recursiva que retorna un entero de largo 9"""
    try:
        user_input = int(input("Ingresa el telefono: "))
    except ValueError:
        #print("ValueError")
        print("Ingresa un telefono correcto")
        user_input = 0
    #comprobamos que el largo del numero es 9
    if len(str(user_input)) == 9:
        #print("Telefono valido")
        return user_input
    else:
        print("Telefono invalido")
        user_input = ingresar_celular()
        return user_input
    
def separador_miles(valor):
    """Funcion que recibe un entero 
    retorna un str con separadores de miles"""
    #creamos una lista vacia
    desglose = []
    # Guardamos una lista con el valor ingresado invertido en formato str
    mirrorvalor = list(reversed(str(valor)))

    # for recore un rango entre 0 y el largo del str
    for n in range(0,len(mirrorvalor)):
        # si la division de n en 3 es exacta y n no es 0
        if n % 3 == 0 and n != 0:
            #agregaremos un punto antes de agregar n
            desglose.append(".")
        # añadimos n a lista vacia creada anteriormente
        desglose.append(mirrorvalor[n])
        
    mirrorvalor = ''.join(str(e) for e in desglose)

    return mirrorvalor[::-1]

def registro_():
    """Funcion que retorna un diccionario"""
    limpiar()
    print("Registro \n")

    #Aqui abajo se ingresan los datos al diccionario
    #Se libre de modificar la cantidad de atributos
    #Tambien puedes modificar los input o añadir funciones
    holder = {
        'atributo1': input("Ingresa atributo 1: "),
        'atributo2': input("Ingresa atributo 2: "),
        'atributo3': input("Ingresa atributo 3: "),
        'atributo4': input("Ingresa atributo 4: "),
        'atributo5': input("Ingresa atributo 5: ")
    }

    return holder

def seleccionar_(matriz):
    """Funcion recursiva que comprueba si un entero 
    se encuentra en un array ingresado a la funcion"""
    try:
        user_input = int(input("Ingrese el numero: "))
    except ValueError:
        print("Error, ingrese un numero valido")
        #modificar si es que se modifica el nombre de la funcion
        user_input = seleccionar_()

    if user_input in matriz:
        #print("Input se encuentra en la matriz")
        return user_input
    else:
        #print("Input no se encuentra en la matriz")
                #modificar si es que se modifica el nombre de la funcion
        user_input = seleccionar_()

def ingresar_fecha():
    #Funcion recursiva que valida una fecha en formato Año-Mes-Dia
    try:
        fecha = input("Ingresa fecha con formato AAAA-MM-DD: ")
        datetime.strptime(fecha,r'%Y-%m-%d')
        print('Fecha valida')
        return fecha
    except ValueError:
        print('Fecha invalida')
        fecha = ingresar_fecha()
        return fecha

def ingresar_fecha_nac():
    """funcion que retorna una fecha
    en el formato que entrega la libreria datetime"""
    limpiar()
    print("Ingreso fecha de nacimiento\n")
    dia = ingresar_dia()
    mes = ingresar_mes()
    year = ingresar_year()

    fecha = date(year,mes,dia)
    limpiar()
    
    return fecha

def ingresar_dia():
    """funcion que comprueba un entero entre 1 y 31"""
    try:
        dia = int(input("Ingresa el dia: "))
        if 1 <= dia <= 31:
            print("El dia es valido")
        else:
            print("Dia invalido")
            dia = ingresar_dia()
    except ValueError:
        print("ValueError")

    return dia

def ingresar_mes():
    """funcion que comprueba un entero entre 1 y 12"""
    try:
        mes = int(input("Ingresa el mes: "))
        if 1 <= mes <= 12:
            pass
        else:
            print("Mes invalido")
            mes = ingresar_mes()
    except ValueError:
        print("ValueError")

    return mes    

def ingresar_year():
    # edad entre 15 y 110 años.
    actual_year = date.today().year
    try:
        year = int(input("Ingresa el año: "))
        if (actual_year - 110) <= year <= (actual_year - 15):
            pass
        else:
            print("Año invalido")
            year = ingresar_year()
    except ValueError:
        print("ValueError")

    return year

def comprobacion_entre(x,y):
    """funcion recursiva que retorna un entero dentro de un rango
    comprueba si un input entero se encuentra entre los parametros x e y
    perdona errores si agregaste los parametros al revez"""
    if x > y:
        a = x
        x = y
        y = a
    elif x == y:
        print("Error en la funcion, corrige las referencias de la funcion")
        x = 0
        y = 1

    try:
        user_input = int(input("Ingrese el valor: "))
    except ValueError:
        print("ValueError")
        user_input = comprobacion_entre(x,y)

    if x <= user_input <= y:
        print("Valido")
        return user_input
    else:
        print(f"Error, un valor valido va desde {x} hasta {y}")
        user_input = comprobacion_entre(x,y)
        return user_input

def ingresar_entero(concepto="valor"):
    try:
        user_input = int(input(f"Ingresa el {concepto}: "))
    except ValueError:
        print("Error")
        user_input = ingresar_entero(concepto)

    return user_input

def arrival_time(hours):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

if __name__ == '__main__':
    status = True

    while status:
        option = menu_principal()
    
        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        else:
            status = False
        

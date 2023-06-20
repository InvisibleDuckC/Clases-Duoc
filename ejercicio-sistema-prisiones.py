import os
from datetime import date
from itertools import cycle

def limpiar():
    os.system('cls')

def menu_principal():
    limpiar()
    print("Gendarmeria de Chile")
    print("Sistema de registro de internos\n")
    print("1- Registrar Internos")
    print("2- Buscar Internos")
    print("3- Imprimir certificados a fiscalia")
    print("4- Salir\n")
    try:
        user_input = int(input("Escoge una opcion: "))
    except ValueError:
        limpiar()
        print("Value Error")
        print("Ingresa una opcion correcta")
        input("Enter para continuar")
        user_input = menu_principal()

    return user_input

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

def registrar_interno():
    """Registrar Internos: Corresponde guardar información de los internos que van ingresando a las
        Unidades Penales, tales como:
        RUT, NOMBRES, APELLIDOS, FECHA NACIMIENTO, DELITOS, AÑOS DE
        CONDENA, UNIDAD PENAL DE DETENCIÓN, PESO(KG), ALTURA(CM)
        El programa debe validar los siguientes aspectos:
        ● peso se encuentre entre 20 y 150 KG
        ● edad entre 15 y 110 años.
        ● Los años de condena deben estar dentro del rango de 1 a 50 años.
    """
    rut = ingresar_rut()
    dv = digito_verificador(rut)
    if dv == 10:
        dv = "k"
    
    interno = {
        'rut': rut,
        'dv': dv,
        'nombres': input("Ingrese nombres: ").upper(),
        'apellidos': input("Ingrese apellidos: ").upper(),
        'fecha nacimiento': ingresar_fecha_nac(),
        'delitos': input("Ingrese delitos: ").upper(),
        'años de condena': ingresar_anos_condena(),
        'unidad penal de detencion': input("Ingrese unidad penal de detencion: ").upper(),
        'peso(kg)': ingresar_peso(),
        'altura(cm)': ingresar_altura() 
    }

    return interno
    
def ingresar_rut():
    try:
        user_input = int(input("Ingresa el rut sin digito verificador: "))
    except ValueError:
        print("ValueError")
        user_input = 0

    if 4000000 < user_input < 99999999:
        return user_input
    else:
        print("Rut erroneo, ingresa un rut valido")
        user_input = ingresar_rut()
        return user_input

def ingresar_fecha_nac():
    limpiar()
    print("Ingreso fecha de nacimiento\n")
    dia = ingresar_dia()
    mes = ingresar_mes()
    year = ingresar_year()

    fecha = date(year,mes,dia)
    limpiar()
    
    return fecha

def ingresar_dia():
    try:
        dia = int(input("Ingresa el dia: "))
        if 1 <= dia <= 31:
            print("El dia es valido")
            #input("Enter para continuar")
        else:
            print("Dia invalido")
            #input("Enter para continuar")
            dia = ingresar_dia()
    except ValueError:
        print("ValueError")

    return dia

def ingresar_mes():
    try:
        mes = int(input("Ingresa el mes: "))
        if 1 <= mes <= 12:
            print("El mes es valido")
            #input("Enter para continuar")
        else:
            print("Mes invalido")
            #input("Enter para continuar")
            mes = ingresar_mes()
    except ValueError:
        print("ValueError")

    return mes    

def ingresar_year():
    #● edad entre 15 y 110 años.
    actual_year = date.today().year
    try:
        year = int(input("Ingresa el año: "))
        if (actual_year - 110) <= year <= (actual_year - 15):
            print("El año es valido")
            input("Enter para continuar")
        else:
            print("Año invalido")
            input("Enter para continuar")
            year = ingresar_year()
    except ValueError:
        print("ValueError")

    return year

def ingresar_anos_condena():
    #● Los años de condena deben estar dentro del rango de 1 a 50 años.
    try:
        user_input = int(input("Ingrese años de condena: "))
    except ValueError:
        print("ValueError")
        user_input = 0

    if 1 <= user_input <= 50:
        return user_input
    else:
        print("Error, la condena debe estar entre 1 y 50 años")
        user_input = ingresar_anos_condena()
        return user_input

def ingresar_peso():
    #● peso se encuentre entre 20 y 150 KG
    try:
        user_input = int(input("Ingrese el peso: "))
    except ValueError:
        print("ValueError")
        user_input = 0

    if 20 <= user_input <= 150:
        return user_input
    else:
        print("Error, un peso valido va desde 20 hasta 150 kg")
        user_input = ingresar_peso()
        return user_input

def ingresar_altura():
    try:
        user_input = int(input("Ingrese la altura: "))
    except ValueError:
        print("ValueError")
        user_input = 0

    if 50 <= user_input <= 300:
        return user_input
    else:
        print("Error, los rangos de altura permitidos estan entre 50 y 300 cm")
        user_input = ingresar_altura()
        return user_input

def buscar_interno(interno):
    """ Buscar Internos: Corresponde buscar un recluso por su rut y mostrar toda su información
        almacenada.
    """
    for key, value in interno.items():
        print(f"{key}: {value}")
    input("\nEnter para continuar")

def imprimir_certificado(interno):
    """Imprimir certificados a fiscalía: Fiscalía Nacional solicita información a Gendarmería de Chile
        certificados de ciertos internos, el sistema debe permitir y generar dicho certificado, se debe
        generar preguntando por RUN del condenado. y mostrar como se muestra a continuación:
        CERTIFICADO DE INTERNOS VIGENTES
        Run: xxxxxxxxxxxxxxx
        Interno: XXXXXXX XXXXXXXX XXXXXXX
        DELITOS: ROBO CON INTIMIDACIÓN
        AÑOS DE CONDENA: 15 AÑOS
        UNIDAD PENAL DE DETENCIÓN: COLINA II
        GENDARMERÍA DE CHILE"""
    
    print("CERTIFICADO DE INTERNOS VIGENTES\n")
    print(f"Run: {interno['rut']}-{interno['dv']}")
    print(f"Interno: {interno['nombres']} {interno['apellidos']}")
    print(f"DELITOS: {interno['delitos']}")
    print(f"AÑOS DE CONDENA: {interno['años de condena']}")
    print(f"UNIDAD PENAL DE DETENCIÓN: {interno['unidad penal de detencion']}")
    print("\n\t\tGENDARMERÍA DE CHILE")
    input("\nEnter para continuar")
    

if __name__ == '__main__':
    lista = {}
    actual_year = date.today().year
    now = date.today()
    status = True
    while status:
        opcion = menu_principal()        
        if opcion == 1:
            limpiar()
            print("Registro de interno\n")
            interno = registrar_interno()
            lista[interno["rut"]] = interno
        elif opcion == 2:
            limpiar()
            print("Busqueda de interno\n")
            user_input = ingresar_rut()
            limpiar()
            if user_input in lista:
                buscar_interno(lista[user_input])
            else:
                print("El rut ingresado no se encuentra en los registros")
                input("Enter para continuar")
        elif opcion == 3:
            limpiar()
            print("Imprimir certificados a fiscalía\n")
            user_input = ingresar_rut()
            limpiar()
            if user_input in lista:
                imprimir_certificado(lista[user_input])
            else:
                print("El rut ingresado no se encuentra en los registros")
                input("Enter para continuar")
        elif opcion == 4:
            limpiar()
            print("Saliendo del programa\n")
            input("Enter para continuar")
            status = False
        else:
            limpiar()
            print("Ingresa una opcion valida")
            input("Enter para continuar")

    
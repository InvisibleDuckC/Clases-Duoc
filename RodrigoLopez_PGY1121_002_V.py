import os
from datetime import date

def limpiar():
    os.system('cls')

def menu_principal():
    """Funcion recursiva que retorna un entero
    print de menu
    comprobacion de input mediante try y except ValueError
    """
    limpiar()
    print("REGISTRO CIVIL\n")
    print("Opciones:")
    print("1- Grabar")
    print("2- Buscar")
    print("3- Imprimir certificado")
    print("4- Salir\n")
    try:
        user_input = int(input("Escoge una opcion: "))
    except ValueError:
        limpiar()
        print("Error\n")
        print("Ingresa una opcion correcta")
        input("Enter para continuar")
        user_input = menu_principal()

    return user_input

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
            return dia
        else:
            print("Dia invalido")
            dia = ingresar_dia()
    except ValueError:
        print("ValueError")

def ingresar_mes():
    """funcion que comprueba un entero entre 1 y 12"""
    try:
        mes = int(input("Ingresa el mes: "))
        if 1 <= mes <= 12:
            return mes
        else:
            print("Mes invalido")
            mes = ingresar_mes()
    except ValueError:
        print("ValueError")

def ingresar_year():
    # edad mayor a 15
    actual_year = date.today().year
    try:
        year = int(input("Ingresa el año: "))
        if year <= (actual_year):
            return year
        else:
            print("Año invalido")
            year = ingresar_year()
    except ValueError:
        print("ValueError")
    
def registro_datos():
    """Funcion que retorna un diccionario"""
    limpiar()
    print("Registro datos\n")

    holder = {
        'nif': ingresar_nif(),
        'nombre': ingresar_str(8,"nombre"),
        'fecha nacimiento': ingresar_fecha_nac(),
        'estado conyugal': input("Ingresa estado conyugal: "),
    }

    return holder

def ingresar_nif():
    nif = ingresar_entero("NIF")
    dv_nif = ingresar_str(3,"verificador",3)
    completo = f"{str(nif)}-{dv_nif.upper()}"

    return completo

def ingresar_entero(concepto="valor"):
    try:
        user_input = int(input(f"Ingresa el {concepto}: "))
    except ValueError:
        print("Error")
        user_input = ingresar_entero(concepto)

    return user_input

def ingresar_str(minimo,concepto="dato",maximo=9999):
    user_input = input(f"Ingresa {concepto}: ")
    if minimo <= len(user_input) <= maximo and maximo != 9999:
        return user_input
    elif minimo <= len(user_input):
        return user_input
    else:
        print("Error")
        user_input = ingresar_str(minimo,concepto,maximo)

def imprimir_certificado(persona):
    limpiar()
    print("CERTIFICADO REGISTRO CIVIL\n")
    print(f"NIF: {persona['nif']}")
    print(f"Nombre: {persona['nombre'].upper()}")
    print(f"Fecha de Nacimiento: {persona['fecha nacimiento']}")
    print(f"Estado conyugal: {persona['estado conyugal'].upper()}")

def buscar_persona(persona):
    for key, value in persona.items():
        print(f"{key}: {value}")
    input("\nEnter para continuar")

if __name__ == '__main__':
    personas = {}
    status = True
    while status:
        opcion = menu_principal()
        if opcion == 1:
            persona = registro_datos()
            personas[persona['nif']] = persona
        elif opcion == 2:
            limpiar()
            print("BUSQUEDA DE PERSONA\n")
            user_input = ingresar_nif()
            if user_input in personas:
                limpiar()
                print("BUSQUEDA DE PERSONA\n")
                buscar_persona(personas[user_input])
            else:
                limpiar()
                print("BUSQUEDA DE PERSONA\n")
                print("NIF no encontrado en los registros\n")
                input("Enter para continuar")
        elif opcion == 3:
            limpiar()
            print("IMPRESION DE CERTIFICADOS\n")
            user_input = ingresar_nif()
            if user_input in personas:
                limpiar()
                imprimir_certificado(personas[user_input])
                input("\n\nEnter para continuar")
            else:
                limpiar()
                print("IMPRESION DE CERTIFICADOS\n")
                print("NIF no encontrado en los registros\n")
                input("Enter para continuar")
            
        elif opcion == 4:
            limpiar()
            print("Saliendo del programa\n")
            print("Programa creado por Rodrigo Lopez - v1.0\n")
            input("Enter para continuar")
            status = False
        else:
            print("Ingresa una opcion valida\n")
            input("Enter para continuar")
import os

def limpiar():
    os.system('cls')

def menu_principal():
    limpiar()
    print("Menu Principal")
    print("Opciones\n")
    print("1- Grabar")
    print("2- Buscar")
    print("3- Imprimir certificados")
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

def registro_vehiculo():
    limpiar()
    print("Registro vehiculo\n")

    holder = {
        'tipo': input("Ingrese el tipo de vehiculo: "),
        'patente': ingresar_patente(),
        'marca': ingresar_marca(),
        'precio': ingresar_precio(),
        'valor multa': ingresar_entero("valor de multa"),
        'fecha multa': input("Ingrese fecha de multa: "),
        'fecha registro': input("Ingrese fecha de registro: "),
        'nombre dueño': input("Ingrese nombre de dueño: ")
    }

    return holder

def ingresar_patente():
    user_input = input("Ingrese la patente: ")
    if len(user_input) == 6:
        return user_input
    else:
        user_input = ingresar_patente()
        return user_input
    
def ingresar_entero(concepto="valor"):
    try:
        user_input = int(input(f"Ingresa el {concepto}: "))
    except ValueError:
        print("Error")
        user_input = ingresar_entero(concepto)

    return user_input

def ingresar_precio():
    user_input = ingresar_entero("precio")

    if user_input >= 5000000:
        return user_input
    else:
        print("Ingresa un valor superior o igual a 5.000.000")
        user_input = ingresar_precio()
        return user_input

def ingresar_marca():
    user_input = input("Ingresa la marca: ")
    if 2 <= len(user_input) <= 15:
        return user_input
    else:
        user_input = ingresar_marca()

def buscar_vehiculo(vehiculo):
    for key, value in vehiculo.items():
        print(f"{key}: {value}")
    input("\nEnter para continuar")

if __name__ == '__main__':
    listado = {}
    status = True
    while status:
        opcion = menu_principal()
        if opcion == 1:
            limpiar()
            vehiculo = registro_vehiculo()
            listado[vehiculo['patente']] = vehiculo
        elif opcion == 2:
            user_input = ingresar_patente()
            if user_input in listado:
                print(f"La patente {user_input} se encuentra en el listado")
                buscar_vehiculo(listado[user_input])
            else:
                print(f"La patente {user_input} no se encuentra en el listado")
        elif opcion == 3:
            pass
        elif opcion == 4:
            limpiar()
            print("Saliendo del programa")
            input("Enter para continuar")
            status = False
        else:
            print("Escoge una opcion valida")
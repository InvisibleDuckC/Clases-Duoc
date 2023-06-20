import os
from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2,8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

def limpiar():
    #limpia la pantalla.
    os.system('cls')

def menu_principal():
    #imprimer el menu principal y retorna la opcion escogida como int
    limpiar()
    print("Bienvenido al menu:")
    print("1- Registrar Cliente")
    print("2- Mostrar Cliente")
    print("3- Salir")
    
    try:
        user_input = int(input("Escoge una opcion: "))
    except ValueError:
        print("Value Error")
        print("Ingresa una opcion correcta")
        input("Enter para continuar")
        user_input = menu_principal()
    
    return user_input

def agregar_cliente():
    limpiar()
    rut = ingresar_rut()
    dv = digito_verificador(rut)
    if dv == 10:
        dv = "k"
    nombre = input("Ingrese el nombre: ")
    direccion = input("Ingrese la dirección: ")
    comuna = input("Ingrese la comuna: ")

    cliente = {
        "rut": rut,
        "dig_verif": dv,
        "nombre": nombre,
        "direccion": direccion,
        "comuna": comuna,
        "correo": ingresar_correo(),
        "edad": ingresar_edad(),
        "genero": ingresar_genero(),
        "celular": ingresar_celular(),
        "tipo_cliente": ingresar_tipo_cliente()
    }

    limpiar()
    print(f"Cliente {nombre} registrado con el rut: {rut}-{dv}")
    input("Enter para continuar")
    
    return cliente

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

def ingresar_correo():
    #Correo: cadena de caracteres que contenga al menos un carácter. Ejemplo “@”, ejemplo → juan@lopez
    user_input = input("Ingrese el correo: ")
    if "@" in user_input:
        return user_input
    else:
        print("ingresa un correo valido")
        user_input = ingresar_correo()
        return user_input
    
def ingresar_edad():
    # Edad: número entero que se encuentre en el rango 0 y 110.
    try:
        user_input = int(input("Ingrese la edad: "))
    except ValueError:
        #print("ValueError")
        print("Ingresa un valor correcto")
        user_input = -1

    if 0 <= user_input <= 110:
        #print("Edad correcta")
        return user_input
    else:
        #print("Error, la edad ingresada no esta dentro del rango valido")
        user_input = ingresar_edad()
        return user_input

def ingresar_genero():
    # Género: carácter que sólo acepta una letra (mayúscula y minúscula), usted defina el carácter y déjelo explícito en el programa.
    generos = ["m","f","o"]
    print("Ingrese el genero:")
    print("[M] para Masculino")
    print("[F] para Femenino")
    print("[O] para Otros")
    user_input = input("Ingrese opcion: ")

    if user_input.lower() in generos:
        return user_input.upper()
    else:
        print("Ingresa una opcion de las indicadas anteriormente")
        user_input = ingresar_genero()
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
        print("Telefono valido")
        return user_input
    else:
        print("Telefono invalido")
        user_input = ingresar_celular()
        return user_input

def ingresar_tipo_cliente():
    # Tipo: cadena de caracteres que sólo acepta los valores “PREMIUM” “GOLD” y “SILVER”.
    tipos = ["premium","gold","silver"]
    print("Ingrese el tipo de cliente:")
    print("- PREMIUM")
    print("- GOLD")
    print("- SILVER")
    user_input = input("Ingrese opcion: ")

    if user_input.lower() in tipos:
        return user_input.upper()
    else:
        print("Ingresa una opcion de las indicadas anteriormente")
        user_input = ingresar_genero()
        return user_input

def mostrar_cliente(clientes):
    for key, value in clientes.items():
        print(f"{key}: {value}")
    input("Enter para continuar")

if __name__ == '__main__':
    
    status = True
    lista = {}

    while status:
        opcion = menu_principal()
        if opcion == 1:
            cliente = agregar_cliente()
            lista[cliente["rut"]] = cliente
        elif opcion == 2:
            user_input = ingresar_rut()
            if user_input in lista:
                mostrar_cliente(lista[user_input])
            else:
                print("El rut ingresado no se encuentra en los registros")
                input("Enter para continuar")
        elif opcion == 3:
            print("Gracias por suscribirse a la App de Juan Maestro")
            input("Enter para salir")
            status = False
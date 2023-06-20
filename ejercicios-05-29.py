import os

def limpiar():
    os.system('cls')

def ejercicio1():
    numero = int(input("Ingrese un numero: "))
    lista = []

    for n in range(1,11):
        lista.append(numero*n)

    print(lista)

def registrar_alumno():
    rut = input("Ingresa el rut del alumno: ")
    nombre = input("Ingresa el nombre del alumno: ")
    nota1 = float(input("Ingresa nota nº1: "))
    nota2 = float(input("Ingresa nota nº2: "))

    return [nombre, rut, nota1, nota2]


if __name__ == '__main__':

    status = True
    alumnos = {}
    
    while status:

        limpiar()
        print("1- Agregar alumno")
        print("2- Buscar alumno")
        print("3- Mostrar alumnos")
        print("4- Salir")

        user_input = input("Opcion: ")
        if user_input == '1':
            limpiar()
            alumno = registrar_alumno()
            alumnos[alumno[1]] = alumno
            input("Enter para continuar")
        elif user_input == '2':
            limpiar()
            buscar = input("Ingresa el rut: ")
            if buscar in alumnos:
                resultado = alumnos[buscar]
                print(f"Nombre\t: {resultado[0]}")
                print(f"Rut\t: {resultado[1]}")
                print(f"Nota 1\t: {resultado[2]}")
                print(f"Nota 2\t: {resultado[3]}")
            else:
                print("No se encontro el rut")
            input("Enter para continuar")
        elif user_input == '3':
            limpiar()
            for a, b in alumnos.items():
                print(f"{a} : {b}")
            input("Enter para continuar")
        elif user_input == '4':
            status = False
        else:
            limpiar()
            print("Ingresa una opcion valida")
            input("Enter para continuar")

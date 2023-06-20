import os

status =  True
agenda = []

while status:
    os.system('cls')
    print("Bienvenido a la agenda telefonica")
    print("Que deseas hacer?")
    print("1- Agregar contacto")
    print("2- Mostrar contactos")
    print("3- Eliminar contactos")
    print("4- Salir")

    try:
        opcion = int(input("Opcion: "))
        if opcion == 1:
            os.system('cls')
            print("Agregar contacto")
            nombre = input("Ingrese el nombre del contacto: ")
            numero = input("Ingrese el numero del contacto: ")
            agregado = nombre + " - " + numero
            agenda.append(agregado)
            print(f"Se agrego {agregado}")
            input("Enter para continuar")
        elif opcion == 2:
            os.system('cls')
            print("Mostrar contactos")
            if len(agenda) == 0:
                print("No hay contactos registrados")
            else:
                for cont in range(0,len(agenda)):
                    print(f"{cont+1}- {agenda[cont]}")
            input("Enter para continuar")
        elif opcion == 3:
            os.system('cls')
            print("Eliminar contacto")
            if len(agenda) == 0:
                print("La agenda esta vacia")
                input("Enter para continuar")
            else:
                try:
                    indice = int(input("Ingresa el indice del contacto a eliminar: "))
                    if indice < 1 or indice > len(agenda):
                        print("Ingresa un indice correcto")
                        input("Enter para continuar")
                    else:
                        eliminado = agenda.pop(indice-1)
                        print(f"Se elimino {eliminado}")
                        input("Enter para continuar")
                except ValueError:
                    os.system('cls')
                    print("Error")
                    print("Ingresa una opcion valida")
                    input("Enter para continuar")
        elif opcion == 4:
            status = False
        else:
            os.system('cls')
            print("Error")
            print("Ingresa una opcion valida")
            input("Enter para continuar")
    except ValueError:
        os.system('cls')
        print("Error")
        print("Ingresa una opcion valida")
        input("Enter para continuar")



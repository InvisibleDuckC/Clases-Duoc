import os

status = True
gastos = []


while status:
    os.system('cls')
    print("Bienvenido al controlador de gastos")
    print("Que deseas hacer?")
    print("1- Registrar gastos")
    print("2- Mostrar gastos")
    print("3- Salir")

    try:
        opcion = int(input("Opcion: "))
        if opcion == 1:
            os.system('cls')
            print("Agregar gasto\n")
            nombre = input("Ingrese descripcion del gasto: ")
            numero = int(input("Ingrese valor del gasto: "))
            agregado = nombre + " - $" + str(numero)
            gastos.append(agregado)
            print(f"Se agrego {agregado}")
            input("Enter para continuar")

        elif opcion == 2:
            os.system('cls')
            print("Mostrar gastos\n")
            if len(gastos) == 0:
                print("No hay gastos registrados\n")
            else:
                for cont in range(0,len(gastos)):
                    print(f"{cont+1}- {gastos[cont]}")
                print()
            input("Enter para continuar")    

        elif opcion == 3:
            status = False

        else:
            os.system('cls')
            print("Error")
            print("Ingresa una opcion valida")
            input("Enter para continuar")

    except ValueError:
        os.system('cls')
        print("Error")
        print("Cometiste un error al ingresar el dato solicitado")
        input("Enter para continuar")

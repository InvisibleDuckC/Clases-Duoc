def Calcular_Iva(precio):
    valor = precio * 1.19
    return valor
    
def Descuento(precio, porc_desc):
    desc = precio * (porc_desc/100)
    return desc
    
def Calcular_Imc(peso, altura):
    imc = peso/(altura*altura)

    print("Su imc es: {}".format(round(imc,1)))

    if imc < 18.5:
        print("Usted esta bajo peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Usted esta sano")
    elif imc >= 25 and imc <= 29.9:
        print("Usted esta sobrepeso")
    elif imc >= 30 and imc <= 34.9:
        print("Usted tiene obesidad")
    elif imc >= 35:
        print("Usted tiene obesidad morbida")

status = True

while status:
    print("Que deseas hacer?")
    print("1- Calcular IVA")
    print("2- Calcular descuentos")
    print("3- Calcular IMC")
    print("4- Salir")
    try:
        user_input = int(input("Ingresa opcion: "))

        if user_input == 1:
            valor = int(input("Ingresa el valor al cual se le calculara el IVA"))
            Calcular_Iva(valor)
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            input("Enter para salir")
            status = False
    
    except:
        print("Error")
        input("Enter para continuar")

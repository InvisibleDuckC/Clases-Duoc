import os

def limpiar():
    os.system('cls')

def ejercicio1():
    numero = int(input("Ingrese un numero: "))
    lista = []

    for n in range(1,11):
        lista.append(numero*n)

    print(lista)

def suma_lista(*valor):
    num = 0
    for i in valor:
        num += i
    return num

def ejercicio2():
    lista = []
    for i in range(0,10):
        lista.append(int(input("Ingresa un numero: ")))
    print(lista)
    print(suma_lista(lista))



if __name__ == '__main__':
    limpiar()
    ejercicio2()
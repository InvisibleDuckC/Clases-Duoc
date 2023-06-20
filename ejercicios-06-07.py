import numpy as np
import random
import os

def limpiar():
    os.system('cls')

def matriz(filas,columnas):
    matriz = np.zeros((filas,columnas))
    return matriz

def randomizar_matriz(matriz, limite):
    shape = matriz.shape

    for f in range(shape[0]):
        for c in range(shape[1]):
            matriz[f][c] = random.randint(1,limite)
    
    return matriz

def ejercicio1():
    """Ejercicio 1:
Crear dos arreglos de dos dimensiones de tamaño 3 x 3, con elementos de tipo numérico entero, luego:
• Muestra la matriz 1.
• Muestra la matriz 2.
• Muestre la matriz resultante de la multiplicación de la matriz 1 y matriz 2."""

    limpiar()
    arreglo1 = randomizar_matriz(matriz(3,3),10)
    print("Arreglo 1")
    print(arreglo1)
    print("Arreglo 2")
    arreglo2 = randomizar_matriz(matriz(3,3),10)
    print(arreglo2)

    arreglo3 = arreglo1 * arreglo2
    print("Arreglo 3")
    print(arreglo3)

def ejercicio2():
    """Ejercicio 2:
Crear un arreglo de dos dimensiones de tamaño 4 y 5, con elementos aleatorios de números enteros del 0 al 100, luego:
• Mostrar por pantalla la suma de los elementos de cada fila.
• Mostrar por pantalla la suma de los elementos de cada columna.
• Mostrar por pantalla la cantidad de elementos impares.
"""
    limpiar()
    print("- Matriz random")
    algo = randomizar_matriz(matriz(4,5),100)
    print(algo)
    shape = algo.shape
    print("\n- Suma elementos por columna")
    for i in range(0,shape[0]):
        print(f"{algo[i,:]} = {algo[i,:].sum()}")
    print("\n- Suma elementos por fila")
    for i in range(0,shape[1]):
        print(f"{algo[:,i]} = {algo[:,i].sum()}")

    print("\n- Cantidad de elementos impares")

    print(f"cantidad de numeros impares: {len(algo[algo % 2 == 1])}")
    print(f"los numeros impares son: {algo[algo % 2 == 1]}")

def ejercicio3():
    """Ejercicio 3:
Crear un arreglo de dos dimensiones de tamaño 10 y 4, el cual, simula a un bus.
Se pide asignar los números de asiento en forma automática, considerando el siguiente formato:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
17 18 19 20
21 22 23 24
25 26 27 28
29 30 31 32
33 34 35 36
37 38 39 40"""
    
    limpiar()
    arreglo = np.arange(1,41).reshape(10,4)

    print(arreglo)

if __name__ == '__main__':
    ejercicio3()
            



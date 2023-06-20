import numpy as np

def clase():
    matriz = np.array([
        [0,1,2,3],
        [4,5,6,7],
        [8,9,10,11]
    ])

    print(matriz)

    print(f"matriz.size: {matriz.size}")
    shape = matriz.shape

    print("Recorremos matriz con 2 for anidados")
    for f in range(shape[0]):
        for c in range(shape[1]):
            print(matriz[f][c])


    print(f"matriz[:,2]: {matriz[:,2]}")

def matriz_zero():
    matriz = np.zeros((3,3))
    print(matriz)

def matriz_unos():
    matriz = np.ones((3,3))
    print(matriz)

def matriz_diagonal():
    matriz = np.diag((1,2,3,4,5))
    print(matriz)


if __name__ == "__main__":
    clase()
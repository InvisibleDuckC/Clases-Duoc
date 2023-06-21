import os
import math

valor_primer_p = 100
valor_p_intermedios = 245
valor_ultimo_p = 400
pisos = 25
deptoxpiso = 8
dpto_justino = 807
dpto_cerro = [0,4]
dpto_mar = [3,7]

def Limpiar():
    os.system('cls')

while True:
    Limpiar()
    print("Bienvenido al cotizador de departamentos\n")
    print(f"La cantidad de pisos es: {pisos}\n")
    try:
        piso = int(input("Ingresa el numero del piso: "))
        if 0 < piso <= pisos:
            pass
        else:
            Limpiar()
            print(f"Ingresa un piso valido\nComienza en 1 y el mas alto es {pisos}")
            input("Enter para continuar")
            continue
        pos = int(input("Ingresa el numero del departamento: "))
        if 0 <= pos < deptoxpiso:
            pass
        else:
            Limpiar()
            print("Ingresa un departamento valido") 
            print(f"Parte desde el 0 hasta el {deptoxpiso-1}")
            input("Enter para continuar")
            continue
        depto = str(piso) + "0" + str(pos)
        if int(depto) == dpto_justino:
            print("\nEste departamento es especial, ya que Justino Vivar se alojo aqui")
            print("Este depto tiene un valor de $500")
        elif piso == 1:
            print(f"El departamento {depto} tiene un valor de $100")
        elif piso == pisos:
            print(f"El departamento {depto} tiene un valor de $400")
        elif 1 < piso < (pisos-1) and pos in dpto_mar:
            print("El piso es intermedio, y tiene vista al mar")
            print(f"El departamento {depto} tiene un valor de {math.floor(245 * 1.13)}")
        elif 1 < piso < (pisos-1) and pos in dpto_cerro:
            print("El piso es intermedio, y tiene vista al cerro")
            print(f"El departamento {depto} tiene un valor de {math.floor(245 * 0.83)}")
        else:
            print(f"El departamento {depto} tiene un valor de 245")
        resp = input("[S] para salir: ")
        if resp.lower() == "s":
            break
    except:
        Limpiar()
        print("Error")
        input("Enter para continuar")

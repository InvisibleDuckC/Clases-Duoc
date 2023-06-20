def multi(*datos):
    a = 1
    for i in datos:
        a *= i

    
    return a

lista = [5,4,2,2]
f = multi(*lista)

print(lista)
print(f)
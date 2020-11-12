#!/usr/bin/python3
nums = [2,11,7,15]
target = 9

# creamos un diccionario para almacenar elementos vistos
seen = {}
# asignamos indice a cada valor que vemos
for index, value in enumerate(nums):
    wanted = target - value
    if wanted in seen:
        # visto en la posicion buscado me devuelve el indice
        # si ya ví el 2 me devuelve 0 como indice ( seen[2] = 0)
        print([seen[wanted], index]) # 
    else:
        # visto en la posicion de valor es igual a su indice
        seen[value] = index # visto = {0:2, ...} siendo wanted = value


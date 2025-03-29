

def cuadradoLista(arreglo):
    return list(map(lambda valorm: valorm**2, filter(lambda valorf: valorf > 0 and isinstance(valorf, int), arreglo)))


cuadrado_enteros = cuadradoLista([-3, 4.8, 5, 3, -3.2])
print(cuadrado_enteros)
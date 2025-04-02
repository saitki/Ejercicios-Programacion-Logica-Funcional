from functools import reduce

def main():
    dolar = 20.44
    listaejemplo = [1500, 2500, 3200, 4500, 6000, 1200, 8000]
    promedio = reduce(lambda x, y: x+y, listaejemplo, 0) / len(listaejemplo) if listaejemplo else 0
    conv_moneda_dolares = list(map(lambda x: x / dolar, listaejemplo))
    venta_mayor_dolares = list(filter(lambda x: x > 150, conv_moneda_dolares))
    suma_total = reduce(lambda x, y: x+y, venta_mayor_dolares, 0)

    print(f"El promedio de ventas en pesos mexicanos: {promedio}")
    print(f"Las ventas de la semana en dolares: {conv_moneda_dolares}")
    print(f"Las ventas en dolares mayores a 150 : {venta_mayor_dolares}")
    print(f"La suma total de las ventas en dolares mayores a 150: {suma_total}")

main()
def preparar_hotcakes():
    return "🥞"

def ordenar_hotcakes(numero_piezas):
    piezas_hotcakes = [preparar_hotcakes() for _ in range(numero_piezas)]
    return piezas_hotcakes

hotcakes_familia = ordenar_hotcakes(int(input("Ingrese el numero de integrantes en la familia: ")))

print(hotcakes_familia)
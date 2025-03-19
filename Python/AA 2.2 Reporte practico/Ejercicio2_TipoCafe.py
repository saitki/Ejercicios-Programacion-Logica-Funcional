def preparar_cafe_americano():
    return "café americano"
def preparar_cafe_olla():
    return "café Olla"

def ordenar_cafe(funcion, numero_tazas):
    tazas_cafe = [funcion() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_para_grupoA = ordenar_cafe(preparar_cafe_americano, 10)
cafe_para_grupoB = ordenar_cafe(preparar_cafe_olla, 10)

print(cafe_para_grupoA)
print(cafe_para_grupoB)

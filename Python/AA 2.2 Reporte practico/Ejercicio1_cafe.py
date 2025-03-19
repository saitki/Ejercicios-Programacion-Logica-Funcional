def preparar_cafe():
    return "café"

def ordenar_cafe(numero_tazas):
    tazas_cafe = [ preparar_cafe() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_para_grupoB = ordenar_cafe(10)

print(cafe_para_grupoB)
#print(preparar_cafe())
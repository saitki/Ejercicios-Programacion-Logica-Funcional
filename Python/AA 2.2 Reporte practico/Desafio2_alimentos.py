def preparar_pizza():
    return "🍕"
def preparar_hamburguesa():
    return "🍔"
def preparar_hotdog():
    return "🌭"

def ordenar_alimento(preparar_alimento, numero_porciones):
    porciones_alimentos = [preparar_alimento() for _ in range(numero_porciones)]
    bonus = calcular_bonus(numero_porciones)
    print(bonus)
    return porciones_alimentos

def calcular_bonus(numero_porciones):
    if(numero_porciones > 2):
        return "Coca gratis"
    else:
        return " "

grupoA = ordenar_alimento(preparar_pizza, 3)
print(grupoA)
grupoB = ordenar_alimento(preparar_hamburguesa, 2)
print(grupoB)
grupoC = ordenar_alimento(preparar_hotdog, 1)
print(grupoC)

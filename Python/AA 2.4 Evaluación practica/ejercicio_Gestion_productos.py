from functools import reduce

def main():
    listaEjemplo = ["Frijoles refritos", "Coca Cola", "Zumo de naranja", "Cafe de Olla", "Gorditas de Chicarron", "Huevos Motuleños"]
    lista_orden_alfabetico = sorted(listaEjemplo)
    cadena_ordenada = reduce(lambda x,y: x +", "+ y, lista_orden_alfabetico, "")
    cadena_ordenada = cadena_ordenada.replace(', ', "",1)
    lista_slug = list(map(lambda x: x.lower().replace(' ', "-"), lista_orden_alfabetico))
    print(f"Cadena de nombres ordenada alfabeticamente: {cadena_ordenada}")
    print(f"Lista de slugs: {lista_slug}")
main()
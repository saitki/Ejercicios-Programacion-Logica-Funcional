#Importamos funciones
from functools import reduce
import matplotlib.pyplot as plt

#Variables globales
materia = ""
LenguajeSumaTotal = 0
LenguajeSumaTotalGeneral = []
LenguajePromedioTotal = 0
LenguajePromedioTotalGeneral = 0
respuestas_mayores_lenguaje = 0
respuestas_mayores_lenguaje_general = 0
respuestas_menores_lenguaje = 0
respuestas_menores_lenguaje_general  = 0
lista_respuesta_Lenguaje = []
lista_respuesta_promedio_lenguaje_general= []

TemasSumaTotal = 0
TemasSumaTotalGeneral = []
TemasPromedioTotal = 0
TemasPromedioTotalGeneral = 0
respuestas_mayores_Temas = 0
respuestas_mayores_Temas_general = 0
respuestas_menores_Temas = 0
respuestas_menores_Temas_general  = 0
lista_respuesta_Temas = []
lista_respuesta_promedio_Temas_general= []

HerramientasSumaTotal = 0
HerramientasSumaTotalGeneral = []
HerramientasPromedioTotal = 0
HerramientasPromedioTotalGeneral = 0
respuestas_mayores_Herramientas = 0
respuestas_mayores_Herramientas_general = 0
respuestas_menores_Herramientas = 0
respuestas_menores_Herramientas_general  = 0
lista_respuesta_Herramientas = []
lista_respuesta_promedio_Herramientas_general= []

ActividadesSumaTotal = 0
ActividadesSumaTotalGeneral = []
ActividadesPromedioTotal = 0
ActividadesPromedioTotalGeneral = 0
respuestas_mayores_Actividades = 0
respuestas_mayores_Actividades_general = 0
respuestas_menores_Actividades = 0
respuestas_menores_Actividades_general  = 0
lista_respuesta_Actividades = []
lista_respuesta_promedio_Actividades_general= []

ContenidoSumaTotal = 0
ContenidoSumaTotalGeneral = []
ContenidoPromedioTotal = 0
ContenidoPromedioTotalGeneral = 0
respuestas_mayores_Contenido = 0
respuestas_mayores_Contenido_general = 0
respuestas_menores_Contenido = 0
respuestas_menores_Contenido_general  = 0
lista_respuesta_Contenido = []
lista_respuesta_promedio_Contenido_general= []




contador_usuario= 1

#Funcion orden superior como herramienta
def menu_operaciones(opr):
    #Funcion suma de 2 valores y retornar resultado
    def suma(x, y):
        return x + y
    #Funcion Conversion de str a int
    def conversion_entero(x):
        return int(x)
    #Funcion filtrar mayor, en este caso 5
    def filtrar_mayor_a_5(x):
        return x==5
    #Funcion filtrar menor, en este caso 0
    def filtrar_menor_a_0(x):
        return x == 0
    #Funcion de contar una lista y devolver el conteo en una nueva lista de los elementos contados
    def lista_contador(lista,x, valor):
        #suma desde el valor dado x
        x = x + 1
        #guarda x en la lista dada
        lista = lista + [x]
        #retorna lista si x es igual al valor dado a alcanzar, sino llamar a la misma funcion hasta llegar 
        return lista if x == valor else lista_contador(lista, x, valor)
    #Llamado del tipo de funcion
    if(opr=="suma"):
        return suma
    if(opr=="toInt"):
        return conversion_entero
    if(opr=="mayor"):
        return filtrar_mayor_a_5
    if(opr=="menor"):
        return filtrar_menor_a_0
    if(opr=="contar"):
        return lista_contador
#funcion para graficar
def grafica(lista, respuestas):
    plt.plot(lista, respuestas, label='Crecimiento', color='blue', linestyle='-', marker='o')

    # Añadir título y etiquetas
    plt.title('Ejemplo de gráfico de líneas')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()

    # Mostrar el gráfico
    plt.show()
#funcion para obtener respuestas a las preguntas de la lista dada
def obtener_puntaje_pregunta_lista(pregunta, listNueva, contador, funcion):
    #guarda el valor dato, conviertiendo el valor en un entero con la funcion dada funcion
    var = funcion(input(pregunta[contador]+"(Califica del 0 al 5): "))
    # valida si el valor dado es mayor a 5 o menor que 0, si es asi da un mensaje que ingrese valores correspondientes, sino hace otra accion
    if var>5 or var < 0:
        print("Ingrese un numero menor a 6 o mayor a -1")
    else: 
        #guarda el valor en la nueva lista
        listNueva = listNueva +  [var]
        #contador
        contador = contador + 1
    #devuelve la llamada de la misma funcion si se cumple a la condicion del if, o no cumple al mensaje dado, para que lo tenga que hacer otra vez. Sino, devuelve otra condicion, si se cumple contador es mayor o igual a la cantidad de preguntas de la lista dada, devuelve la lista, sino se llama otra vez
    return obtener_puntaje_pregunta_lista(pregunta, listNueva, contador, funcion) if var>5 or var<-1 else (listNueva if contador >= len(pregunta) else obtener_puntaje_pregunta_lista(pregunta, listNueva, contador, funcion))

#funcion main
def main(tr):
    #llamado a las Variables globales para su uso
    global lista_respuesta_Lenguaje
    global lista_respuesta_Temas
    global lista_respuesta_Herramientas
    global lista_respuesta_Actividades
    global lista_respuesta_Contenido

    global LenguajeSumaTotal
    global LenguajePromedioTotal

    global TemasSumaTotal
    global TemasPromedioTotal

    global HerramientasSumaTotal
    global HerramientasPromedioTotal

    global ActividadesSumaTotal
    global ActividadesPromedioTotal

    global ContenidoSumaTotal
    global ContenidoPromedioTotal

    global materia

    global respuestas_mayores_lenguaje
    global respuestas_mayores_lenguaje_general
    global respuestas_menores_lenguaje
    global respuestas_menores_lenguaje_general
    global LenguajeSumaTotalGeneral

    global respuestas_mayores_Temas
    global respuestas_mayores_Temas_general
    global respuestas_menores_Temas
    global respuestas_menores_Temas_general
    global TemasSumaTotalGeneral

    global respuestas_mayores_Herramientas
    global respuestas_mayores_Herramientas_general
    global respuestas_menores_Herramientas
    global respuestas_menores_Herramientas_general
    global HerramientasSumaTotalGeneral

    global respuestas_mayores_Actividades
    global respuestas_mayores_Actividades_general
    global respuestas_menores_Actividades
    global respuestas_menores_Actividades_general
    global ActividadesSumaTotalGeneral

    global respuestas_mayores_Contenido
    global respuestas_mayores_Contenido_general
    global respuestas_menores_Contenido
    global respuestas_menores_Contenido_general
    global ContenidoSumaTotalGeneral

    global contador_usuario
    global lista_respuesta_promedio_lenguaje_general
    global lista_respuesta_promedio_Temas_general
    global lista_respuesta_promedio_Herramientas_general
    global lista_respuesta_promedio_Actividades_general
    global lista_respuesta_promedio_Contenido_general

    #llamado a las funciones de la funcion de orden superior para su uso
    suma = menu_operaciones("suma")
    entero = menu_operaciones("toInt")
    mayor = menu_operaciones("mayor")
    menor = menu_operaciones("menor")
    lista_contador = menu_operaciones("contar")
    #No hay nombre de la materia, se ingresa, con tr se valida
    if(tr):
        materia = input("Ingrese una materia: ")
        #Cambia de estado a que ya hay un nombre
        tr = False
    #menu de opciones
    print(f"---- Calificacion de la materia {materia} Usuario {contador_usuario}----")
    print("1.- Lenguaje")
    print("2.- Temas")
    print("3.- Herramientas")
    print("4.- Actividades")
    print("5.- Contenido")
    print("6.- Mis resultados")
    print("7.- Terminar mi encuesta")
    print("8.- Finalizad el programa")
    opt = int(input("Ingrese una opcion: "))
    #Opcion 1 para Lenguaje
    if(opt == 1):
        #Lista vacia
        lista_respuesta_Lenguaje = []
        #Lista con preguntas
        lista_preguntas_Lenguaje = ["1.- ¿Es comprensible las expresiones que utiliza el maestro? ", 
                                    "2.- ¿Son muy complejo las expresiones? ", 
                                    "3.- ¿Es muy tecnico la expresion al sentido comun? ", 
                                    "4.- ¿Conoces las expresiones?"]
        #Operaciones
        lista_respuesta_Lenguaje = obtener_puntaje_pregunta_lista(lista_preguntas_Lenguaje, lista_respuesta_Lenguaje, 0, entero)
        respuestas_mayores_lenguaje = len(list(filter(mayor, lista_respuesta_Lenguaje)))
        respuestas_menores_lenguaje = len(list(filter(menor, lista_respuesta_Lenguaje)))
        LenguajeSumaTotal = reduce(suma, lista_respuesta_Lenguaje, 0)
        LenguajePromedioTotal = LenguajeSumaTotal / len(lista_preguntas_Lenguaje)
        #Muestra de resultados
        print("---------------------------------------------")
        print(f"Resultado suma: {LenguajeSumaTotal}")
        print(f"Resultado promedio: {LenguajePromedioTotal}")
        print(f"Resultado Mayor(5): {respuestas_mayores_lenguaje}")
        print(f"Resultado Menor(0): {respuestas_menores_lenguaje}")
    #Opcion 2 para Temas
    elif(opt == 2):
        #Listas
        lista_respuesta_Temas = []
        lista_preguntas_Temas = ["1.- ¿Los temas tratados fueron interesantes?", 
                                 "2.- ¿Los temas estaban relacionados con tu carrera?",
                                 "3.- ¿Se cubrieron todos los temas planeados en el curso?",
                                 "4.- ¿Los temas fueron explicados de manera clara?"]
        #Operaciones
        lista_respuesta_Temas = obtener_puntaje_pregunta_lista(lista_preguntas_Temas, lista_respuesta_Temas, 0, entero)
        respuestas_mayores_Temas = len(list(filter(mayor, lista_respuesta_Temas)))
        respuestas_menores_Temas = len(list(filter(menor, lista_respuesta_Temas)))
        TemasSumaTotal = reduce(suma, lista_respuesta_Temas, 0)
        TemasPromedioTotal = TemasSumaTotal / len(lista_preguntas_Temas)
        #Muestras
        print("---------------------------------------------")
        print(f"Resultado suma: {TemasSumaTotal}")
        print(f"Resultado promedio: {TemasPromedioTotal}")
        print(f"Resultado Mayor(5): {respuestas_mayores_Temas}")
        print(f"Resultado Menor(0): {respuestas_menores_Temas}")
        #Opcion 3 Herramientas 
    elif opt == 3: 
        #Lista
        lista_respuesta_Herramientas = []
        lista_preguntas_Herramientas = [
            "1.- ¿Las herramientas utilizadas ayudaron a tu aprendizaje?", 
            "2.- ¿Fue fácil acceder a las herramientas del curso?", 
            "3.- ¿Las herramientas estaban actualizadas?",
            "4.- ¿Se utilizaron herramientas digitales (software, plataformas) de forma efectiva?"]
        #Operaciones
        lista_respuesta_Herramientas = obtener_puntaje_pregunta_lista(lista_preguntas_Herramientas, lista_respuesta_Herramientas, 0, entero)
        respuestas_mayores_Herramientas = len(list(filter(mayor, lista_respuesta_Herramientas)))
        respuestas_menores_Herramientas = len(list(filter(menor, lista_respuesta_Herramientas)))
        HerramientasSumaTotal = reduce(suma, lista_respuesta_Herramientas, 0)
        HerramientasPromedioTotal = HerramientasSumaTotal / len(lista_preguntas_Herramientas)
        #Muestras
        print("---------------------------------------------")
        print(f"Resultado suma: {HerramientasSumaTotal}")
        print(f"Resultado promedio: {HerramientasPromedioTotal}")
        print(f"Resultado Mayor(5): {respuestas_mayores_Herramientas}")
        print(f"Resultado Menor(0): {respuestas_menores_Herramientas}")
        #Opcion 4 Actividades
    elif opt == 4:
        #Listas
        lista_respuesta_Actividades = []
        lista_preguntas_Actividades = [
            "1.- ¿Las actividades ayudaron a entender los temas?",
            "2.- ¿Fueron claras las instrucciones de las actividades?",
            "3.- ¿Las actividades fueron adecuadas al nivel del curso?",
            "4.- ¿Hubo suficiente variedad de actividades?"]
        #Operaciones
        lista_respuesta_Actividades = obtener_puntaje_pregunta_lista(lista_preguntas_Actividades, lista_respuesta_Actividades, 0, entero)
        respuestas_mayores_Actividades = len(list(filter(mayor, lista_respuesta_Actividades)))
        respuestas_menores_Actividades = len(list(filter(menor, lista_respuesta_Actividades)))
        ActividadesSumaTotal = reduce(suma, lista_respuesta_Actividades, 0)
        ActividadesPromedioTotal = ActividadesSumaTotal / len(lista_preguntas_Actividades)
        #Muestras
        print("---------------------------------------------")
        print(f"Resultado suma: {ActividadesSumaTotal}")
        print(f"Resultado promedio: {ActividadesPromedioTotal}")
        print(f"Resultado Mayor(5): {respuestas_mayores_Actividades}")
        print(f"Resultado Menor(0): {respuestas_menores_Actividades}")
        #Opcion 5 Contenido
    elif opt == 5:
        #Listas
        lista_respuesta_Contenido = []
        lista_preguntas_Contenido = [
            "1.- ¿El contenido fue útil para tu formación profesional?",
            "2.- ¿Estuvo bien organizado el contenido del curso?",
            "3.- ¿El contenido estaba actualizado?",
            "4.- ¿El contenido fue suficiente para comprender los temas?"
        ]
        #Operaciones
        lista_respuesta_Contenido = obtener_puntaje_pregunta_lista(lista_preguntas_Contenido, lista_respuesta_Contenido, 0, entero)
        respuestas_mayores_Contenido = len(list(filter(mayor, lista_respuesta_Contenido)))
        respuestas_menores_Contenido = len(list(filter(menor, lista_respuesta_Contenido)))
        ContenidoSumaTotal = reduce(suma, lista_respuesta_Contenido, 0)
        ContenidoPromedioTotal = ContenidoSumaTotal / len(lista_preguntas_Contenido)
        #Muestras
        print("---------------------------------------------")
        print(f"Resultado suma: {ContenidoSumaTotal}")
        print(f"Resultado promedio: {ContenidoPromedioTotal}")
        print(f"Resultado Mayor(5): {respuestas_mayores_Contenido}")
        print(f"Resultado Menor(0): {respuestas_menores_Contenido}")
        #Opcion 6 para mostrar resultados y sus graficas
    elif opt == 6:
        print("---------------------------------------------")
        if len(lista_respuesta_promedio_lenguaje_general) == 0:
            print("---- General ----")
            print("Conteste la encuesta primero")        
        else:
            print("---- General ----")
            LenguajeSumaTotalGeneral = reduce(suma,lista_respuesta_promedio_lenguaje_general,0)
            print(f"Resultado suma: {LenguajeSumaTotalGeneral}")
            LenguajePromedioTotalGeneral = reduce(suma,lista_respuesta_promedio_lenguaje_general,0) / len(lista_respuesta_promedio_lenguaje_general) if lista_respuesta_promedio_lenguaje_general else 0
            print(f"Resultado promedio: {LenguajePromedioTotalGeneral}")
            print(f"Resultado Mayor(5): {respuestas_mayores_lenguaje_general}")
            print(f"Resultado Menor(0): {respuestas_menores_lenguaje_general}")
            optL = input("¿Desea Graficar? s/n : ")
            if(optL == "s"):
                if(len(lista_respuesta_promedio_lenguaje_general) != 0):
                    lista = []
                    lista = lista_contador(lista,0, len(lista_respuesta_promedio_lenguaje_general))
                    grafica(lista, lista_respuesta_promedio_lenguaje_general)
                else:
                   print("Revuelva primero la encuesta")
        print("---- Lenguaje ----")
        print(f"Resultado suma: {LenguajeSumaTotal}")
        print(f"Resultado promedio: {LenguajePromedioTotal}")
        print(f"Resultado Mayor(5): {respuestas_mayores_lenguaje}")
        print(f"Resultado Menor(0): {respuestas_menores_lenguaje}")
        
        optL = input("¿Desea Graficar? s/n : ")
        if(optL == "s"):
            if(len(lista_respuesta_Lenguaje) != 0):
                lista = []
                lista = lista_contador(lista, 0, len(lista_respuesta_Lenguaje))
                grafica(lista, lista_respuesta_Lenguaje)
            else:
                print("Revuelva primero la encuesta")
        print("---- Temas ----")
        print(f"Resultado suma: {TemasSumaTotal}")
        print(f"Resultado promedio: {TemasPromedioTotal}")
        print(f"Resultado Mayor(5): {respuestas_mayores_Temas}")
        print(f"Resultado Menor(0): {respuestas_menores_Temas}")
        
        optL = input("¿Desea Graficar? s/n : ")
        if(optL == "s"):
            if(len(lista_respuesta_Temas) != 0):
                lista = []
                lista = lista_contador(lista, 0, len(lista_respuesta_Temas))
                grafica(lista, lista_respuesta_Temas)
            else:
                print("Revuelva primero la encuesta")
        print("---- Herramientas ----")
        print(f"Resultado suma: {HerramientasSumaTotal}")
        print(f"Resultado promedio: {HerramientasPromedioTotal}")
        print(f"Resultado Mayor(5): {respuestas_mayores_Herramientas}")
        print(f"Resultado Menor(0): {respuestas_menores_Herramientas}")
        
        optL = input("¿Desea Graficar? s/n : ")
        if(optL == "s"):
            if(len(lista_respuesta_Herramientas) != 0):
                lista = []
                lista = lista_contador(lista, 0, len(lista_respuesta_Herramientas))
                grafica(lista, lista_respuesta_Herramientas)
            else:
                print("Revuelva primero la encuesta")
        print("---- Actividades ----")
        print(f"Resultado suma: {ActividadesSumaTotal}")
        print(f"Resultado promedio: {ActividadesPromedioTotal}")
        print(f"Resultado Mayor(5): {respuestas_mayores_Actividades}")
        print(f"Resultado Menor(0): {respuestas_menores_Actividades}")
        
        optL = input("¿Desea Graficar? s/n : ")
        if(optL == "s"):
            if(len(lista_respuesta_Actividades) != 0):
                lista = []
                lista = lista_contador(lista, 0, len(lista_respuesta_Actividades))
                grafica(lista, lista_respuesta_Actividades)
            else:
                print("Revuelva primero la encuesta")
        print("---- Contenido ----")
        print(f"Resultado suma: {ContenidoSumaTotal}")
        print(f"Resultado promedio: {ContenidoPromedioTotal}")
        print(f"Resultado Mayor(5): {respuestas_mayores_Contenido}")
        print(f"Resultado Menor(0): {respuestas_menores_Contenido}")
        
        optL = input("¿Desea Graficar? s/n : ")
        if(optL == "s"):
            if(len(lista_respuesta_Contenido) != 0):
                lista = []
                lista = lista_contador(lista, 0, len(lista_respuesta_Contenido))
                grafica(lista, lista_respuesta_Contenido)
            else:
                print("Revuelva primero la encuesta")
    #Opcion 7 Guardar la encuesta para el siguiente usuario 
    elif opt == 7:
        if not lista_respuesta_Lenguaje or not lista_respuesta_Temas or not lista_respuesta_Actividades or not lista_respuesta_Contenido or not lista_respuesta_Herramientas: 
            print("Al menos un usuario debe contestar y cotestar todo")
        else:
            lista_respuesta_promedio_lenguaje_general = lista_respuesta_promedio_lenguaje_general + [LenguajePromedioTotal]
            respuestas_mayores_lenguaje_general = respuestas_mayores_lenguaje
            respuestas_menores_lenguaje_general = respuestas_menores_lenguaje

            lista_respuesta_promedio_Temas_general = lista_respuesta_promedio_Temas_general + [TemasPromedioTotal]
            respuestas_mayores_Temas_general = respuestas_mayores_Temas
            respuestas_menores_Temas_general = respuestas_menores_Temas
            
            lista_respuesta_promedio_Herramientas_general = lista_respuesta_promedio_Herramientas_general + [HerramientasPromedioTotal]
            respuestas_mayores_Herramientas_general = respuestas_mayores_Herramientas
            respuestas_menores_Herramientas_general = respuestas_menores_Herramientas

            lista_respuesta_promedio_Actividades_general = lista_respuesta_promedio_Actividades_general + [ActividadesPromedioTotal]
            respuestas_mayores_Actividades_general = respuestas_mayores_Actividades
            respuestas_menores_Actividades_general = respuestas_menores_Actividades

            lista_respuesta_promedio_Contenido_general = lista_respuesta_promedio_Contenido_general + [ContenidoPromedioTotal]
            respuestas_mayores_Contenido_general = respuestas_mayores_Contenido
            respuestas_menores_Contenido_general = respuestas_menores_Contenido

            lista_respuesta_Lenguaje = []
            respuestas_mayores_lenguaje = 0
            respuestas_menores_lenguaje = 0
            LenguajeSumaTotal = 0
            LenguajePromedioTotal = 0

            lista_respuesta_Temas = []
            respuestas_mayores_Temas = 0
            respuestas_menores_Temas = 0
            TemasSumaTotal = 0
            TemasPromedioTotal = 0

            lista_respuesta_Herramientas = []
            respuestas_mayores_Herramientas = 0
            respuestas_menores_Herramientas = 0
            HerramientasSumaTotal = 0
            HerramientasPromedioTotal = 0

            lista_respuesta_Actividades = []
            respuestas_mayores_Actividades = 0
            respuestas_menores_Actividades = 0
            ActividadesSumaTotal = 0
            ActividadesPromedioTotal = 0

            lista_respuesta_Contenido = []
            respuestas_mayores_Contenido = 0
            respuestas_menores_Contenido = 0
            ContenidoSumaTotal = 0
            ContenidoPromedioTotal = 0
            #aumento de valor para representar el usaurio
            contador_usuario = contador_usuario+1
            #muestra de los resultados listas
            print(lista_respuesta_promedio_lenguaje_general)
            print(lista_respuesta_promedio_Temas_general)
            print(lista_respuesta_promedio_Herramientas_general)
            print(lista_respuesta_promedio_Actividades_general)
            print(lista_respuesta_promedio_Contenido_general)
            #Retornar la misma funcion si la opcion es menor a 8, sino retornar valor 1 para finalizar el programa
    return main(tr) if opt<8 else 1
#Llamado a la funcion principal con valor True para la recursividad
main(True)
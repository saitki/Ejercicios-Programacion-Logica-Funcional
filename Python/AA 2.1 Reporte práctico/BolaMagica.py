
import random

pregunta = input('pregunta: ')

numero_aletaorio = random.randint(1, 9)

if numero_aletaorio == 1:
    respuesta = 'Si - definitivamente'
elif numero_aletaorio == 2:
    respuesta = 'Esta decidido'
elif numero_aletaorio == 3:
    respuesta = 'Sin duda'
elif numero_aletaorio == 4:
    respuesta = 'Respuesta confusa, intenta de nuevo'
elif numero_aletaorio == 5:
    respuesta = 'Pregunta mas tarde'
elif numero_aletaorio == 6:
    respuesta = 'Mejor no te digo'
elif numero_aletaorio == 7:
    respuesta = 'Mis fuentes dicen que no'
elif numero_aletaorio == 8:
    respuesta = 'No parece bueno'
elif numero_aletaorio == 9:
    respuesta = 'Muy dudoso'
else:
    respuesta = 'Error'
  
print('Bola magica:  ' + respuesta)


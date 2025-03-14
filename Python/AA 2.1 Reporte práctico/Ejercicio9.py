gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('===============')
print('El sombrero seleccionador 🧙‍♂️')
print('===============')

print('P1) ¿Te gusta el amanecer o el atardecer?')

print('  1) Amanecer')
print('  2) Atardecer')

respuesta = int(input('Ingresa respuesta (1-2): '))

if respuesta == 1:
    gryffindor += 1
    ravenclaw += 1
elif respuesta == 2:
    hufflepuff += 1
    slytherin +=1
else:
  print('Respuesta incorrecta.')

print('\nP2) Cuando muera, quiero que la gente me recuerde como:')

print('  1) El bueno o la buena')
print('  2) El valiente o la valiente')
print('  3) El sabio o la sabia')
print('  4) El astuto o la astuta')

respuesta = int(input('Ingresa tu respuesta (1-4): '))

if respuesta == 1:
    hufflepuff += 2
elif respuesta == 2:
    slytherin += 2
elif respuesta == 3:
    ravenclaw += 2
elif respuesta == 4:
    gryffindor += 2
else:
  print('Respuesta incorrecta.')

print('\nQ3) ¿Que tipo de instrumento complace mas tu oido?')

print('  1) El violin')
print('  2) La trompeta')
print('  3) El piano')
print('  4) El tambor')

respuesta = int(input('Ingresa tu respuesta (1-4): '))

if respuesta == 1:
    slytherin += 4
elif respuesta == 2:
    hufflepuff += 4
elif respuesta == 3:
    ravenclaw +=4
elif respuesta == 4:
    gryffindor += 4
else:
  print('Respuesta incorrecta.')

print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print('🦁 Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
    print('🦅 Ravenclaw!')
elif hufflepuff >= slytherin:
    print('🦡 Hufflepuff!')
else:
    print('🐍 Slytherin!')

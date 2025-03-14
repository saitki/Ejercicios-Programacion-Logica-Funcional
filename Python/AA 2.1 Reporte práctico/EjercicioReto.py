##Las ramas de sistemas computacionales a considerar son:
#Redes
#Bases de Datos
#Desarrollo de Software
#Programación Hardware
#Modelado 3D
#Gestión de Proyectos de Software

redes = 0
baseDeDatos = 0
desarrolloSoftware = 0
modelado3D = 0
gestionProyectos = 0
programacionHardware = 0

print('===============')
print('El sombrero seleccionador rama de sistemas computacionales')
print('===============')

print('P1) ¿Qué tipo de actividades disfrutas resolver más?')

print('  1) Optimización de la conectividad entre dispositivos')
print('  2) Organización y gestión eficiente de grandes volúmenes de información')
print('  3) Creación de aplicaciones y plataformas digitales')
print('  4) Programación y control de dispositivos electrónicos')
print('  5) Diseño y animación de modelos tridimensionales')
print('  6) Coordinación de equipos y planificación de proyectos tecnológicos')

respuesta = int(input('Ingresa respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    baseDeDatos += 1
elif respuesta == 3:
    desarrolloSoftware += 1
elif respuesta == 4:
    programacionHardware += 1
elif respuesta == 5:
    modelado3D += 1
elif respuesta == 6:
    gestionProyectos += 1
else:
    print('Respuesta incorrecta.')

print('P2) ¿Cuál de estas actividades te llama más la atención?')

print('  1) Configurar routers y switches en una red')
print('  2) Diseñar una base de datos para una empresa')
print('  3) Programar una aplicación web o móvil')
print('  4) Trabajar con microcontroladores como Arduino o ESP32')
print('  5) Crear gráficos y modelos en 3D para videojuegos o simulaciones')
print('  6) Planificar y coordinar el desarrollo de un software con un equipo')

respuesta = int(input('Ingresa respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    baseDeDatos += 1
elif respuesta == 3:
    desarrolloSoftware += 1
elif respuesta == 4:
    programacionHardware += 1
elif respuesta == 5:
    modelado3D += 1
elif respuesta == 6:
    gestionProyectos += 1
else:
    print('Respuesta incorrecta.')

print('P3) ¿Cuál de estas herramientas te gustaría aprender a usar?')

print('  1) Wireshark o Cisco Packet Tracer')
print('  2) MySQL, PostgreSQL o MongoDB')
print('  3) Python, JavaScript o Java')
print('  4) Lenguaje ensamblador o C para microcontroladores')
print('  5) Blender, Maya o Unity')
print('  6) ira, Trello o Microsoft Project')

respuesta = int(input('Ingresa respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    baseDeDatos += 1
elif respuesta == 3:
    desarrolloSoftware += 1
elif respuesta == 4:
    programacionHardware += 1
elif respuesta == 5:
    modelado3D += 1
elif respuesta == 6:
    gestionProyectos += 1
else:
    print('Respuesta incorrecta.')

print('P4) ¿En qué área te gustaría trabajar en el futuro?')

print('  1) Seguridad informática o administración de redes')
print('  2) Análisis de datos o gestión de información empresarial')
print('  3) Desarrollo de aplicaciones, videojuegos o software empresarial.')
print('  4) Ingeniería de hardware o sistemas embebidos')
print('  5) Creación de contenido digital, animación o simulaciones')
print('  6)  Gestión y liderazgo de equipos de desarrollo tecnológico.')

respuesta = int(input('Ingresa respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    baseDeDatos += 1
elif respuesta == 3:
    desarrolloSoftware += 1
elif respuesta == 4:
    programacionHardware += 1
elif respuesta == 5:
    modelado3D += 1
elif respuesta == 6:
    gestionProyectos += 1
else:
    print('Respuesta incorrecta.')

print('P5) ¿Cuál de estas afirmaciones te describe mejor?')

print('  1) Me gusta entender cómo se comunican los dispositivos y optimizar su conexión')
print('  2) Disfruto estructurar información y hacer consultas eficientes.')
print('  3) Me apasiona crear programas que resuelvan problemas')
print('  4) Me interesa el funcionamiento de los dispositivos físicos y su programación. ')
print('  5) Me encanta diseñar, modelar y animar objetos tridimensionales.')
print('  6) Me gusta organizar equipos y gestionar recursos para alcanzar objetivos.')

respuesta = int(input('Ingresa respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    baseDeDatos += 1
elif respuesta == 3:
    desarrolloSoftware += 1
elif respuesta == 4:
    programacionHardware += 1
elif respuesta == 5:
    modelado3D += 1
elif respuesta == 6:
    gestionProyectos += 1
else:
    print('Respuesta incorrecta.')

print("Redes: ", redes)
print("Base de datos: ", baseDeDatos)
print("Desarrollo de Software: ", desarrolloSoftware)
print("Programacion de Hardware: ", programacionHardware)
print("Modelado 3D: ", modelado3D)
print("Gestion de Proyectos: ", gestionProyectos)

if redes >= baseDeDatos and redes >= desarrolloSoftware and redes >= modelado3D and redes >= gestionProyectos and redes >= programacionHardware:
    print('🌐 Redes')
elif baseDeDatos >= desarrolloSoftware and baseDeDatos >= modelado3D and baseDeDatos >= gestionProyectos and baseDeDatos >= programacionHardware:
    print('🗄️ Bases de Datos')
elif desarrolloSoftware >= modelado3D and desarrolloSoftware >= gestionProyectos and desarrolloSoftware >= programacionHardware:
    print('💻 Desarrollo de Software')
elif modelado3D >= gestionProyectos and modelado3D >= programacionHardware:
    print('🎨 Modelado 3D')
elif gestionProyectos >= programacionHardware:
    print('📊 Gestión de Proyectos de Software')
else:
    print('🔧 Programación Hardware')

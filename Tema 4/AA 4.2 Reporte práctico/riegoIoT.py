# Estado de sensores
humedad_suelo = "baja"
temperatura = 35
hora = 20
pronostico_lluvia = False

# Regla: ¿Es una hora adecuada para regar?
def hora_adecuada():
    global hora
    return hora and hora < 10 or hora > 18

# Regla principal: ¿Cuándo se debe activar el sistema de riego?
def activar_riego():
    global humedad_suelo, pronostico_lluvia, hora
    return humedad_suelo == "baja" and pronostico_lluvia == False and hora_adecuada()

def estado_riego():
    if activar_riego():
        return "Activado"
    else:
        return "No activado"

# Regla para alerta de temperatura extrema
def alerta_calor():
    global temperatura
    return temperatura and temperatura >= 32

# Mensaje de recomendación
def recomendacion():
    if activar_riego() and alerta_calor():
        print("Alerta: Riego activado con temperatura alta. Considere riego nocturno o por goteo.")
    else:
        print("Sin recomendaciones especiales para el riego.")
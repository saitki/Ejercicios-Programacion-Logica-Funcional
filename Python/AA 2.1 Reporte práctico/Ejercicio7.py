import random
frases = [
    'No persigas la felicidad, creala.',
    'Todas las cosas son difíciles antes de ser faciles.',
    'El pajaro madrugador atrapa el gusano, pero el segundo raton obtiene el queso.',
    'Si comes algo y nadie te ve comerlo, no tiene calorias.',
    'Alguien en tu vida necesita una carta tuya.',
    '¡No solo pienses. Actua!',
    'Tu corazon se saltara un latido.',
    'La fortuna que buscas esta en otra galleta.'
]

def fortuna():
    abrir_galleta = random.randint(0, len(frases) - 1)
    print(frases[abrir_galleta])

fortuna()

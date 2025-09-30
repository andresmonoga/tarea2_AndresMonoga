import random

# Diccionarios de razas
razas_benevolas = {
    "Ositos": 1,
    "Príncipes": 2,
    "Enanos": 3,
    "Caris": 4,
    "Fulos": 5
}

razas_malvadas = {
    "Lolos": 2,
    "Fulanos": 2,
    "Hoggins": 2,
    "Lurcos": 3,
    "Trollis": 5
}

# Ejércitos: número de integrantes de cada raza
ejercito_bien = {
    "Ositos": 3,
    "Príncipes": 2,
    "Enanos": 1
}
ejercito_mal = {
    "Lolos": 1,
    "Hoggins": 3,
    "Trollis": 2
}

def batalla_aleatoria(ejercito_bien, ejercito_mal):
    raza_bien = random.choice(list(ejercito_bien.keys()))
    cantidad_bien = ejercito_bien[raza_bien]
    raza_mal = random.choice(list(ejercito_mal.keys()))
    cantidad_mal = ejercito_mal[raza_mal]
    valor_bien = razas_benevolas[raza_bien] * cantidad_bien
    valor_mal = razas_malvadas[raza_mal] * cantidad_mal
    resultado = ""
    if valor_bien > valor_mal:
        resultado = "¡Gana el Bien!"
    elif valor_bien < valor_mal:
        resultado = "¡Gana el Mal!"
    else:
        resultado = "¡Empate!"
    print(f"Raza bien: {raza_bien} ({cantidad_bien} miembros) - Valor: {valor_bien}")
    print(f"Raza mal: {raza_mal} ({cantidad_mal} miembros) - Valor: {valor_mal}")
    print("Resultado de batalla:", resultado)

# Para accionar varias veces:
for _ in range(5):
    print("\nNueva batalla aleatoria:")
    batalla_aleatoria(ejercito_bien, ejercito_mal)
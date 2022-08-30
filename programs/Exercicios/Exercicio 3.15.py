cigarros_fumados = int(input("Quantos cigarros você já fumou: "))
anos_fumados = int(input("Quantos anos você já fumou: "))
vida_perdida_minutos = cigarros_fumados * 10
vida_perdida_hora = vida_perdida_minutos/60
print(f"O tempo de vida perdida em minutos: {vida_perdida_minutos:1.0f} minutos")
print(f"O tempo de vida perdida em horas: {vida_perdida_hora:1.0f} horas")
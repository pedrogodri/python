distancia = float(input("Qual a distancia da viagem: "))
velociade_media = float(input("Qual a velocidade media da viagem: "))
tempo = distancia/velociade_media #Tempo em horas
tempo_minutos = tempo*60
print(f"O tempo da viagem em horas é: {tempo:5.2f}")
print(f"O tempo da viagem em minutos é: {tempo_minutos:5.2f}")
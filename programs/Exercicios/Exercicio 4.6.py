distancia = int(input("Digite a distância percorrida: "))

if distancia <= 200:
    preco = distancia*0.50
else:
    preco = distancia*0.45

print(f"O valor da sua viagem de {distancia} KM, foi R${preco:5.2f}")
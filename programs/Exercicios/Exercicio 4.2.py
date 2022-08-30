#Exercio 4.2 - Multa por velocidade
v = float(input("qual a velocidade do veículo: "))
soma_multa = float
km_mais = float

if v>80:
    km_mais = v - 80
    soma_multa = km_mais*5
    print(f"Sua velocidade de {v:5.2f}KM, gerou uma multa de R${soma_multa:5.2f}")
else:
    print("Você não foi multado")    
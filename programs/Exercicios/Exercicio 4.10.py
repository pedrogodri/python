tipo = (input("Digite o tipo do eu imovel: "))
faixa = int(input("Digite a faixa de kWh: "))

if tipo == "R":
    if faixa <= 500:
        soma = faixa*0.40
    else:
        soma = faixa*0.65
elif tipo == "C":
    if faixa > 500 and faixa <= 1000:
        soma = faixa*0.55
    else:
        soma = faixa*0.60
elif tipo == "I":
    if faixa > 100 and faixa <= 5000:
        soma = faixa*0.55
    else:
        soma = faixa*0.60

print(f"O seu imovel {tipo} deu um valor total de: R${soma}")
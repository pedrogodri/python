taxa = float(input("Digite a sua taxa de juros: "))
taxa_m = taxa/100
x = 0
while x < 24:
    depo_mes = float(input("Digite o deposito mensal: "))
    soma = 0
    soma = soma + depo_mes*taxa_m
    print(f"Ganho do juros: R${soma}")
    x += 1
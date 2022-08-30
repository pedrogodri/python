deposito = float(input("Digite o seu deposito: "))
taxa = float(input("Digite a sua taxa de juros: "))
taxa_m = taxa/100
x = 0
soma = 0
while x < 24:
    soma = soma + deposito*taxa_m
    x += 1
print(f"Ganho do juros: R${soma}")
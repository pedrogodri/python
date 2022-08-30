valor_casa = float(input("Qual o valor do imovel: "))
salario = float(input("Qual é o seu salario: "))
anos_pagar = int(input("Quantos anos para pagar o imovel: "))

#Para saber em quantos meses para pagar a casa
meses_pagar = anos_pagar*12

#Para saber a prestação mensal da casa
valor_mensal = valor_casa/meses_pagar

#Para somar mais 30% do salario
salario_mais_30 = salario*0.30
#Para pegar os 30% do salario
salario_30 = salario_mais_30 - salario

if valor_mensal < salario_30:
    print(f"Você podera comprar este imovel, o valor mensal das prestções é: R${valor_mensal:6.2f}")
else:     
    print("Você não pode comprar este imovel!")  
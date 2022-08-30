salario = float(input("Digite seu salário: R$"))

if salario>1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
    
print(f"O aumento foi de R${aumento:5.2f}")
novo_salario = salario + aumento
print(f"O novo salário é R${novo_salario}")
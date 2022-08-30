salario = float(input("digite o seu salario: "))
porcentagem = float(input("Digite a porcentagem do seu aumento: "))
aumento = porcentagem/100
valor_aumento = salario * aumento
novo_salario = salario + valor_aumento
print(f"Valor do aumento do salario: {valor_aumento:5.2f}")
print(f"Valor do novo salario: {novo_salario:5.2f}")

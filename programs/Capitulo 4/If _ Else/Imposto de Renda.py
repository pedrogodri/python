#Programa 4.3 - Calculo Imposto de renda
salario = float(input("Digite o seu salário: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f"salário R$ {salario:6.2f} Imposto a pagar: R${imposto:6.2f}")  
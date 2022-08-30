n1 = float(input("Digite um número: "))
n2 = float(input("Digite um outro número: "))
operacao = (input("Escolha uma operação matematica: "))

if operacao == "soma":
    soma = n1+n2
elif operacao == "subtração":
    soma = n1-n2
elif operacao == "multiplicação":
    soma = n1*n2
elif operacao == "divisão":
    soma = n1/n2
else:
    print("Operação invalida! Digite novamente!")
print(f"A operação escolida foi {operacao} e o resultado foi {soma:6.2f}")
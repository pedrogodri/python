num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
x = 0
vezes = 0
while x < num2:
    vezes = vezes + num1
    x += 1
print(f"A multiplicação feita em forma de soma entre {num1} x {num2} é: {vezes}")
#Programa 6.3 - Apresentação de numeros
numero = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numero[x] = int(input(f"Numero {x + 1}: "))
    x += 1
while True:
    escolhido = int(input("Que posição você quer imprimir (0 - para sair): "))
    if escolhido == 0:
        break
    print(f"Você Escolheu o numero: {numero[escolhido - 1]}")
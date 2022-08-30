print("Selecione uma das opções abaixo: \n")
print("TABELA:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")
print("5 - sair\n")
tabuada = 1
while tabuada <= 10:
    calc = int(input("Digite uma das opções: "))
    numero = 1
    while numero <= 10:
        if calc == 1:
            print(f"{tabuada} + {numero} = {tabuada + numero}")
        elif calc == 2:
            print(f"{tabuada} - {numero} = {tabuada - numero}")
        elif calc == 3:
            print(f"{tabuada} / {numero} = {tabuada / numero:5.2f}") 
        elif calc == 4:
            print(f"{tabuada} * {numero} = {tabuada * numero}") 
        elif calc == 5:
            break
        numero += 1
    tabuada += 1
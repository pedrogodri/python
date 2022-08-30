num = int(input("Digite um numero para saber sua tabuada: "))
fim_tabu = int(input("Digite p numero para o fim da tabuada: "))
x = 0
while x <= fim_tabu:
    soma = num*x
    print(f"{num} x {x} = {soma}")
    x += 1
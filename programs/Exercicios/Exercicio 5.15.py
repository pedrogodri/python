s = 0
while True:
    code = int(input("Digite o código do produto: "))
    qtd = int(input("Digite a quantidade desejada: "))
    
    if code == 0:
        break
    elif code == 1:
        s += (0.50*qtd)
    elif code == 2:
        s += (1.00*qtd)
    elif code == 3:
        s += (4.00*qtd)
    elif code == 5:
        s += (7.00*qtd)
    elif code == 9:
        s += (8.00*qtd)
    else:
        print("Código Inválido")
print(f"O valor final da compra é: R${s:5.2f}")
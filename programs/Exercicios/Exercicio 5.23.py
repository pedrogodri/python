n = int(input("Digite um quantas vezes você quer repetir: "))
i = 0

while i < n:
    primo = int(input("Digite um número para verificar: "))
    
    if primo % 2 == 1:
        print("É número primo\n")
    else:
        print("Não é número primo\n")
    i += 1
categoria = int(input("Digite a categoria do produto: "))

if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    print("Categoria inválida, digite um valor novamente!")
    preco = 0
print(f"o preço do produto é: R${preco:6.2f}")
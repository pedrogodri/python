n = int(input("Digite um número: "))
i = 0
num = n

while num > i:
    if n % 2 == 1:
        print(f"{n} é primo\n")
    else:
        print(f"{n} não é primo\n")
    i += 1
    n -= 1
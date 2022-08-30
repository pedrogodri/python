n = int(input("Digite: "))
b = 2

while abs(n-(b*b)) > 0.0001:
    p = (b+ (n/b))/2
    b = p
print(f"A raiz quadrada de {n} é aproximadamente: {b:0.2f}")
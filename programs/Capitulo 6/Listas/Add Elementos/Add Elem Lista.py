#Programa 6.6 - Adição de elemtnos à lista
l = []
while True:
    n = int(input("Digite um numero (0 para sair): "))
    if n == 0:
        break
    l.append(n)
x = 0
while x < len(l):
    print(l[x])
    x += 1
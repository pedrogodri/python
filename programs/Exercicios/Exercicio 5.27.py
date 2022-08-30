frase = str(input("Digite: ")).strip().upper()
palavras = frase.split()
juntar = "".join(palavras)
inverso = ""
print(f"Você digitou a frase: {palavras}")
for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]
print(f"O inverso de {juntar} é: {inverso}")
if inverso == juntar:
    print("Essa frase é um palídromo")
else:
    print("Essa frase não é um palídromo")
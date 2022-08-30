valor_marcadoria = float(input("Digite o preço da mercadoria: "))
percentual_desconto = float(input("Digite o  percentual de desconto da mercadoria: "))

desconto_final = (percentual_desconto/100)*valor_marcadoria
print(f"O desconto final é: {desconto_final:5.2f}")

valor_final = valor_marcadoria - desconto_final
print(f"O valor final da mercadoria é: {valor_final:5.2f}")
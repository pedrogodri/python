km_percorridos = float(input("Digite a KM percorrida do carro: "))
dias_uso = float(input("Digite os dias de uso do carro: "))
valor_km = km_percorridos*0.15
valor_dias = dias_uso*60
valor_final = valor_km + valor_dias
print(f"O preço total do carro alugado por {dias_uso:1.0f} dias de uso e {km_percorridos:5.2f}KM percorridos é: {valor_final:5.2f}")
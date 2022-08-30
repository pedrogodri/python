dia = int(input("Quantos dias: "))
horas = int(input("Quantos horas: "))
minutos = int(input("Quantos minutos: "))
segundos = int(input("Quantos segundos: "))

conv_dia = dia*86400
conv_horas = horas*3600
conv_min = minutos*60
total = conv_dia + conv_horas + conv_min + segundos
print(f"O total é: {total:5.2f}")
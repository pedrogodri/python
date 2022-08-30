s = 0
t_digi = 0

while True:
    num = int(input("Digite o número: "))
    if num == 0:
        break
    s += num
    t_digi += 1
media = s/t_digi
print(f"O total de números digitados é: {t_digi}")
print(f"A soma total entre os {t_digi} números digitados é: {s}")
print(f"A média entre os {t_digi} números digitados é: {media:5.2f}")
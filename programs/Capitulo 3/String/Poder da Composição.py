nome = "Pedro"
idade = 22
grana = 100.78
print("%s tem %d anos e R$%f no bolso." % (nome, idade, grana  ))
print("%12s tem %d anos e R$%5.2f no bolso." % (nome, idade, grana))
print("%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, grana  ))
print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, grana  ))
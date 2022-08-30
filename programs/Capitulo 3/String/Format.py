nome = "Pedro"
idade = 22
grana = 51.34
print("{} tem {} anos e R${} no bolso.".format(nome, idade, grana))
print("{:12} tem {:3} anos e R${:5.2f} no bolso.".format(nome, idade, grana))
print("{:12} tem {:03} anos e R${:5.2f} no bolso.".format(nome, idade, grana))
print("{:<12s} tem {:<3} anos e R${:5.2f} no bolso.".format(nome, idade, grana))
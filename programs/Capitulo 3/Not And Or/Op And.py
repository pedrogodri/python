a = 1
b = 2
c = 3

d = a != b and b < c #Verdadeiro
print(d)
d = a != b and b > c #Falso
print(d)
d = a > b and b < c #Falso
print(d)
d = a > b and b > c #Falso
print(d)
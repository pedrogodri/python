a = 1
b = 2
c = 3

d = a != b or b < c #Verdadeiro
print(d)
d = a != b or b > c #Falso
print(d)
d = a > b or b < c #Falso
print(d)
d = a > b or b > c #Falso
print(d)
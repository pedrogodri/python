a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a>b and b>c:
    print(f"O maior número é: {a} e o menor número é: {c}")
if a>b and c>b: 
    print(f"O maior número é: {a} e o menor número é: {b}")  
if b>a and a>c: 
    print(f"O maior número é: {b} e o menor número é: {c}")  
if b>c and c>a: 
    print(f"O maior número é: {b} e o menor número é: {a}")
if c>b and b>a: 
    print(f"O maior número é: {c} e o menor número é: {a}")    
elif c>a and a>b: 
    print(f"O maior número é: {c} e o menor número é: {b}")   
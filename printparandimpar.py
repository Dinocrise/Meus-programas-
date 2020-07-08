limite = int(input("Qual o limite? "))
numero = 0
par = 0
impar = 0
while numero != limite:
    numero += 1
    condicao = numero % 2
    if condicao == 0:
        par += 1
    else:
        impar += 1
print("par:", par)
print("impar:", impar)

numero = int(input("Digite um número inteiro: "))
referencia = numero
ref = 0
while numero != 1:
    divisao = referencia % numero
    if divisao == 0:
        ref += 1
    numero -= 1
if ref == 1:
    print("primo")
else:
    print("não primo")


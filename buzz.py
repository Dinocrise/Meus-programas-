numero = int(input("Insira um número inteiro: "))
verificacao = numero % 5
if verificacao == 0:
    print("Buzz")
else:
    print(numero)
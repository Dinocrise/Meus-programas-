numero = int(input("Insira um número inteiro: "))
verificacao = numero % 3
if verificacao == 0:
    print("Fizz")
else:
    print(numero)
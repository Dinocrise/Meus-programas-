numero = int(input("Digite um número inteiro: "))
numero = numero % 100
numero = numero - (numero % 10)
numero = numero / 10
print("O dígito das dezenas é", int(numero))

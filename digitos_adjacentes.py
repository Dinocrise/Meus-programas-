numero = int(input("Digite um número inteiro: "))
soma = 0
referencia = len(str(numero))
#123 %10 = 3
#len = 3
#123 // 10 = 12
while referencia != 0:
    soma += (numero % 10)
    numero = numero // 10
    referencia -= 1
print(soma)

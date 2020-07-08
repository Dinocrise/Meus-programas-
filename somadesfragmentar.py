import time
numero = int(input("Insira um numero inteiro para desfragmentar: "))
numero_dezenas = len(str(numero))
controle = 0
soma_numeros = 0
divisor = 10
while controle != numero_dezenas:
    soma_numeros += (numero % divisor)
    numero = (numero // divisor)
    controle += 1
time.sleep(1)
print("A soma de todos os numeros é : ", soma_numeros)

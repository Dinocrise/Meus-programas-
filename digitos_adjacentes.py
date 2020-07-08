numero = int(input("Digite um número inteiro: "))
teste_iguais = False
while numero > 0 and teste_iguais:
    ultimo_numero = numero % 10
    penultimo_numero = (numero % 10) - (ultimo_numero)
    if ultimo_numero == penultimo_numero:
        teste_iguais = True
    numero = numero // 10
if teste_iguais == True:
    print("sim")
else:
    print("não")
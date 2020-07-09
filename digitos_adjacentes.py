numero = int(input("Digite um número inteiro: "))
teste_iguais = False
while numero > 0 or teste_iguais:
    ultimo_numero = numero % 10
    numero = numero // 10
    penultimo_numero = numero % 10
    if ultimo_numero == penultimo_numero:
        teste_iguais = True
        break
    if numero < 0 :
        break
if teste_iguais :
    print("sim")
else:
    print("não")
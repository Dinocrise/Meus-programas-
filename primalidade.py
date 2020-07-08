numero = int(input("Digite o valor de n: "))
impar = 1
if numero > 0:
    while numero != 0:
        print(impar)
        impar += 2
        numero -= 1
else:
    print("Só numeros positivo please")

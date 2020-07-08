numero1 = int(input("Insira um número inteiro 1: "))
numero2 = int(input("Insira um número inteiro 2: "))
numero3 = int(input("Insira um número inteiro 3: "))
if numero1 < numero2:
    if numero2 < numero3:
        print("crescente")
    else:
        print("não está em ordem crescente")
else:
    print("não está em ordem crescente")

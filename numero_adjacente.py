numero = int(input("NUmero: "))
numero_igual = False
while numero // 10 > 0 or numero_igual:
    numero_comparar_1 = numero % 10
    numero = numero // 10
    numero_comparar_2 = numero % 10
    if numero_comparar_1 == numero_comparar_2:
        #print("È igual")
        numero_igual = True
        break
    if numero <= 0:
        break
   # else:
    #    print("nada iguais")
if numero_igual:
    print("Tem numeros iguais")
else:
    print("Não tem numeros iguais")
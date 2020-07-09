numero = int(input("Entre com o número: "))
divisor = numero
primo = 0
while divisor != 1:
    divisao = numero % divisor
    if divisao == 0:
        primo +=1
    divisor -= 1
if primo == 1:
    print ("primo")
else:
    print("não primo")

#Fatorial
def fatorial(numero):
    resultado = 1
    while numero != 0:
        resultado = resultado * numero
        numero -= 1
    return resultado

numero_n = int(input("Entre com o numero n: "))
numero_k = int(input("Entre com o numero k: "))
subtracao_numeros = numero_n - numero_k
coeficiente = (fatorial(numero_n))/((fatorial(numero_k)*(fatorial(subtracao_numeros))))
print ("O coeficiente binomial é", coeficiente)
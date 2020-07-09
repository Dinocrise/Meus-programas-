import math
import time
def delta (elemento_a, elemento_b, elemento_c):
    delta = ((elemento_b ** 2) - (4 * elemento_a * elemento_c))
    return delta, - delta
def raizes_funcao (elemento_a, elemento_b, elemento_c):
    valor_x_1 = ((-elemento_b) + (math.sqrt(delta))) / (2 * elemento_a)
    valor_x_2 = ((-elemento_b) - (math.sqrt(delta))) / (2 * elemento_a)
    return valor_x_1 valor_x_2
print(" Calcular uma função de segundo grau, na forma ( ax²-bx-c )")
elemento_a = int(input("Entre com o elemento 'a': "))
elemento_b = int(input("Entre com o elemento 'b': "))
elemento_c = int(input("Entre com o elemento 'c': "))

if delta > 0:

    if valor_x_1 < valor_x_2:
        print("as raízes da equação são", valor_x_1, "e", valor_x_2)
    else:
        print("as raízes da equação são", valor_x_2, "e", valor_x_1)
elif delta == 0:
    valor_x = (-elemento_b)/(2*elemento_a)
    print("a raiz desta equação é", valor_x)
else:
    print("esta equação não possui raízes reais")

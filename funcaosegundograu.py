import math
import time
print(" Calcular uma função de segundo grau, na forma ( ax²-bx-c )")
elemento_a = int(input("Entre com o elemento 'a': "))
elemento_b = int(input("Entre com o elemento 'b': "))
elemento_c = int(input("Entre com o elemento 'c': "))
delta = ((elemento_b**2) - (4 * elemento_a * elemento_c))
print("o valor de delta foi de", delta)
print()
time.sleep(2)
if delta > 0:
    print("DELTA É MAIOR QUE 0, TEM DOIS VALORES REAIS!")
    valor_x_1 = ((-elemento_b) + (math.sqrt(delta)))/(2*elemento_a)
    valor_x_2 = ((-elemento_b) - (math.sqrt(delta)))/(2*elemento_a)
    print("Os dois valores de x são", valor_x_1, "e", valor_x_2)
elif delta == 0:
    print("DELTA É IGUAL A 0, TEMOS UM VALOR REAL!")
    valor_x = (-elemento_b)/(2*elemento_a)
    print("O valor de x é", valor_x)
else:
    print("DELTA É MENOR QUE 0")
    print("A EQUAÇÃO REAL NÃO POSSUI VALORES REAIS!")

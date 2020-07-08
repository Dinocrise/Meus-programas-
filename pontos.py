import math
coordenada_x_1 = int(input("Primeira coordenada x: "))
coordenada_y_1 = int(input("Primeira coordenada y: "))
coordenada_x_2 = int(input("Segunda coordenada x: "))
coordenada_y_2 = int(input("Segunda coordenada y: "))
distancia = math.sqrt(((coordenada_x_1 - coordenada_x_2) ** 2)+((coordenada_y_1 - coordenada_y_2) ** 2))
if distancia < 10:
    print("perto")
else:
    print("longe")
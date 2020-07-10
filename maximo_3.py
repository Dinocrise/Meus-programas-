def maximo(numero1, numero2, numero3):
    if numero1 > numero2:
        if numero1 > numero3:
            return numero1
        else:
            return numero3
    elif numero2 > numero3:
        if numero2 > numero1:
            return numero2
        else:
            return numero1
    elif numero3 > numero1:
        if numero3 > numero2:
            return numero3
        else:
            return numero2
    elif numero1 == numero2:
        return numero1
    elif numero2 == numero3:
        return numero2
    elif numero3 == numero1:
        return numero3

def eprimo(numero):
    auxiliar = numero
    resultado = False
    if numero == 0:
        return resultado
    else:
        primo = 0
        while auxiliar != 1:
            teste = numero % auxiliar
            auxiliar -= 1
            if teste == 0:
                primo += 1
        if primo == 1:
            resultado = True
        else:
            resultado = False
        return resultado

def maior_primo(numero):
    teste = eprimo(numero)
    if teste:
        return numero
    else:
        while not teste:
            numero -= 1
            teste = eprimo(numero)
        return numero



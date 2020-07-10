def fizzbuzz(numero):
    divisao_3 = numero % 3
    divisao_5 = numero % 5
    if divisao_3 == 0:
        if divisao_5 == 0:
            resultado = ("FizzBuzz")
            return resultado
        resultado = ("Fizz")
        return resultado
    elif divisao_5 == 0:
        resultado = ("Buzz")
        return resultado
    else:
        return numero

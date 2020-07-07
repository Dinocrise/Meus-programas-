entrada = int(input("Por favor, entre com o número de segundos que deseja converter: "))
segundos = entrada % 60
minutosb = entrada // 60
horasb = entrada // 3600
dias = entrada // 86400
horas = horasb -(dias *24)
minutos = minutosb - (horasb*60)
print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")


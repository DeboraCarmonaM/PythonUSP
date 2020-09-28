segundos = input("Por favor, insira o número de segundos que deseja converter: ")

segundosInt = int(segundos)

dias = segundosInt // 86400

segundosSobram1 = segundosInt % 86400

horas = segundosSobram1 // 3600

segundosSobram2 = segundosSobram1 % 3600

minutos = segundosSobram2 // 60

segundosFinais = segundosSobram2 % 60

segundos = segundosFinais


print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos")

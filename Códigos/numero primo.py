numero = int(input("Digite um número inteiro: "))
contador = 0
i = 0

while i <= numero or contador < 2:
    i = i + 1
    x = numero % i
    if x == 0:
        contador = contador + 1

if contador <= 2:
     print("primo")

else:

     print("não primo")

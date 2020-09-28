número = int(input("Digite o número: "))

resultado = 1
contador = 1

while contador <= número:
    resultado = resultado * contador
    contador = contador + 1

print(resultado)

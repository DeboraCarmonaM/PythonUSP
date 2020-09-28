quantidade = int(input("Quantos números terá a sequência?"))
print()
x = 1
contador = 1
resultado = 1
    
while x <= quantidade:
        
    numero = int(input("Digite o número da sequência: "))
    print()

    if numero == 2:

        print("O fatorial de 2 é 2")
        
    else:
        
        while contador <= numero:
               
            resultado = resultado * contador
            contador = contador + 1

        print("O fatorial de {} é {}".format(numero, resultado))
        print()
        
    x = x+1


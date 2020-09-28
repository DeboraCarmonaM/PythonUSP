def fatorial_usuario():

    quantidade = int(input("Quantos números terá a sequência?"))
    x = 1
    
    while x <= quantidade:
        
        numero = int(input("Digite o número do sequência: "))
                     
            while numero != 1:
                
                fatorial = numero*(numero-1)
                print("O fatorial de {} é {}".format(numero, fatorial))
                numero = numero - 1

            if numero == 1:
                     
                print("O fatorial de 1 é 1")
            
        x = x+1
                         
                         
                     

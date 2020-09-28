def n_primos(numero):
    
    def éPrimo(x):
    
        fator = 2

        if x == 2:
            return True

        while x % fator != 0 and fator <= x/2:
            fator = fator + 1

        if x % fator == 0:
            return False

        else:
            return True
        
    contagem = 0
    a = 2
    
    while numero >= a:

        primo = éPrimo(numero)

        if primo == True :

            contagem = contagem + 1

        numero = numero - 1

        if numero < a:

            return contagem



            

    
    


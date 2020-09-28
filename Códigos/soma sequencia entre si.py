



sequencia = int(input("Digite a sequência de números: "))

sum = 0


while sequencia != 0:
    
    ultimoDigito = sequencia % 10
    
    sequencia = sequencia / 10
    
    sum = int( sum + ultimoDigito)
    
    
print(sum)
    
    
    

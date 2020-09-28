



def usuario_escolhe_jogada(n,m):

    i = 0
    
    while i > m or i == 0:

        
        
        i = int(input("Quantas peças você ira retirar? "))

        if i > m or i == 0:
            print("Faça uma jogada válida")

        else:
            print("Você retirou", i, "peças.")

      

def computador_escolhe_jogada(n,m):

    
    
    j = 0
   
    while n % (m + 1) != 0:
        n = n - 1
        i = j + 1

    if n % (m + 1) == 0:
         print("O computador retirou", j, "peças")



n = 5
m = 2

peca_usuario = usuario_escolhe_jogada(n,m)

print(peca_usuario)

peca_computador = computador_escolhe_jogada(n,m)

print(peca_computador)

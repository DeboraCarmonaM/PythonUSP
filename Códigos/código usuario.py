def usuario_escolhe_jogada (n,m):

    print("Agora é sua vez")
    
    jogadaUsuario = 0

    while jogadaUsuario == 0:

        jogadaUsuario = int(input("Quantas peças você ira retirar? "))

        if jogadaUsuario > m or jogadaUsuario < 1 or jogadaUsuario > n:

            jogadaUsuario = 0
            print("Faça uma jogada válida")

        if jogadaUsuario <= m or jogadaUsuario > 1:
            
            print("Você retirou : ")

    return jogadaUsuario 
            
            

        

def campeonato():
    
    x = 1
    usuario = 0
    computador = 0

    while x <= 3:
        print('\n**** Rodada {} ****'.format(x))
        vencedor = partida()

        if vencedor == 1:

            usuario = usuario = 1

        else:

            computador = computador + 1

        x = x +1

        if x > 3:
        
            print('\n**** Final do campeonato! ****\n')
            print("Placar: Você {} x {} Computador".format(usuario, computador))



def computador_escolhe_jogada(n, m):
    
    if n <= m:
        
        return n
    
    else:
        
        valor = n % (m+1)
    
    if valor > 0:
        
        return valor
    
    return m

def usuario_escolhe_jogada(n, m):
    
    jogo = 0
    
    while jogo == 0:
        
        jogo = int(input("Quantas peças você vai tirar? "))
        
        if jogo > n or jogo < 1 or jogo > m:
            
            print("\nOops! Jogada inválida! Tente de novo.\n")
            
            jogo = 0
            
    return jogo

def partida():
    
    n = int(input("Quantas peças? "))

    m = int(input("Limite de peças por jogada? "))

    computer_turn = True

    if n % (m+1) == 0:
        
        computer_turn = False
        
        print("Você começa!")
    else:
        print("Computador começa!")

    while n > 0:

        if computer_turn:
            
            jogo = computador_escolhe_jogada(n, m)
            
            computer_turn = False
            
            if(jogo == 1):
                
                print("\nO computador tirou uma peça.")
                
            else:
                print("\nO computador tirou {} peças.".format(jogo))
                
        else:
            
            jogo = usuario_escolhe_jogada(n, m)
            
            computer_turn = True
            
            if(jogo == 1):
                
                print("\nVocê tirou uma peça.")
                
            else:
                print("\nVocê tirou {} peças.".format(jogo))


        n = n - jogo

        if(n == 1):
            
            print("Agora resta apenas uma peça no tabuleiro.\n")
            
        elif(n > 1):
            
            print("Agora restam {} peças no tabuleiro.\n".format(n))

    if computer_turn:
        
        print("Fim do jogo! Você ganhou!")
        
        return 1
    
    else:
        
        print("Fim do jogo! O computador ganhou!")
        
        return 0


def main():

    tipo = 0
        
    while tipo == 0:
        
        tipo = (int(input("Bem-vindo ao jogo do NIM! Escolha: \n\n1 - para jogar uma partida isolada \n2 - para jogar um campeonato ")))
        
        if ( tipo == 1 ):
            
            print("\nVoce escolheu partida isolada!")
            
            partida()
            
            break
        
        elif ( tipo == 2):
            
            print("\nVoce escolheu um campeonato!")
            
            campeonato()
            
            break
        
        else:
            
            print("Opção inválida!")
            
            tipo = 0

main()

def main():

    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - Para jogar uma partida isolada")
    print("2 - Para jogar um capeonato")
    inicio = int(input("Digite o número correspondente a sua escolha: "))

    if inicio == 1:

        print("Você escolheu partida isolada!")
        partida()

    if inicio == 2:

        print("Você escolheu um campeonato!")
        campeonato()
        
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


def computador_escolhe_jogada(n,m):
  
    print("Agora é a vez do computador")
    
    if n <= m:
        
        return n
   
    else:

        valor = n % (m+1)

        if valor > 0:

            return valor

        return m


def partida():

    n = int(input("Quantas peças tem o jogo?"))
    m = int(input("Qual o valor máximo de peças que podem ser retiradas a cada rodada?"))

    while n > 0:

        if n % (m+1) == 0:
            
            turno_computador = False
            jogo = computador_escolhe_jogada(n,m)
            print("Computador retirou {} peças.".format(jogo))

        else:

            jogo = usuario_escolhe_jogada(n,m)
            turno_computador = True
            print("Você retirou {} peças.".format(jogo))

            
        n = n - jogo

        print("Sobraram apenas {} peças em jogo.\n".format(n))

        if turno_computador:
            print("Você ganhou!")


        else:
            print("O computador ganhou!")
            return 0
            
        


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


main()


    



  
            

        
    
            
            

    

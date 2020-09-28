def partida()

    n = int(input("Quantas peças tem o jogo?"))
    m = int(input("Qual o valor máximo de peças que podem ser retiradas a cada rodada?"))

    turno_computador = True

    if n % (m+1) == 0:
        turno_computador = False

    while n > 0:

        if turno_computador:

            jogo = computador_escolhe_jogada(n,m)
            turno_computador = False
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

def campeonato():

    computador = 0
    usuario = 0

    for_in range(3):

        vencedor = partida()

        if vencedor == 1:

            usuario = usuario + 1

        else:

            computador = computador + 1


        print("Placar: Você {} x {} Computador".format(usuario, computador))

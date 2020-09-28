def main():
    
    a = 0
    
    while a == 0:
        
        print("")
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print("")
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato 2")
        
        a = int(input())
        
        if a == 1:
            partida() 
            break
        
        elif a == 2:
            print("Voce escolheu um campeonato!")
            print("")
            campeonato() 
            break
        
        else:
            print("Escolha uma opção válida!")
            print("")
            a = 0 




def usuario_escolhe_jogada(n,m):
    
    valor_tirado = 0
    
    while valor_tirado == 0:
        
        valor_tirado = int(input("Quantas peças você vai tirar?"))
        
        if valor_tirado > n or valor_tirado > m or valor_tirado < 1 :
            
            print("")
            print("Oops! Jogada inválida! Tente de novo.")
            print("")
            
            valor_tirado = 0
            
            return valor_tirado 



def computador_escolhe_jogada(n,m):
    
    if n <= m:
        
        return n 
    else:
        
        sobrou = n % (m+1)
        
        if sobrou > 0:
            
            return sobrou
        
        return m 

def partida():
    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    y = n % (m + 1)
    
    vez_usuario = False
    vez_computador = False

    if y != 0:
        
        pc = True
        vez_computador = True
        
    if y == 0: 
        pc = False
        vez_usuario = True 
    
    while n > 0:
        
        if pc == True:
            
            if vez_computador == True:
                
                print("")
                print("Computador começa!")
                print("")
                
            vez_computador = False 
            
            valor_tirado = computador_escolhe_jogada(n,m)
            
            pc = False
            
            if valor_tirado == 1:
                
                print("O computador tirou uma peça")
            else:
                
                print("O computador tirou ",valor_tirado," peças.")
        else: 
            
            if vez_usuario == True:
                
                print("")
                print("Voce começa!")
                print("")
                
            vez_usuario = False 
            
            valor_tirado = usuario_escolhe_jogada(n,m)
            
            pc = True
            
            if valor_tirado == 1:
                
                print("Você tirou uma peça")
                
            else:
                
                print("Voce tirou",valor_tirado,"peças.")
                
        n = n - valor_tirado 
        
        if n > 0:
            
            print("Agora restam",n,"peças no tabuleiro.")
            print("")
    
    if pc == True:
        
        print("Fim do jogo! Você ganhou!")
        print("")
        
        return 1 
    else:
        
        print("Fim do jogo! O computador ganhou!")
        print("")
        
        return 0 

def campeonato():
    
    computador = 0
    usuario = 0
    
    i = 1
    
    for _ in range(3):
        
        print("**** Rodada",i,"****")
        print("")
        
        id_ganhou = partida()
        
        i = i + 1
        
        if id_ganhou == 1:
            
            usuario = usuario +1
            
        else:
            
            computador = computador + 1
            
    print("**** Final do campeonato! ****")
    
    print("Placar: Você",usuario,"X",computador,"Computador")


main()

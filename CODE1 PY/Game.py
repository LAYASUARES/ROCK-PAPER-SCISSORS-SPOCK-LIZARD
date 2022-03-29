#encoding:UTF-8
from optparse import Option
import random

while True: 
    winUser = 0
    pcWin = 0
    aleatorio = random.randrange(0, 6)
    escolhaPc = ""
    print("1)Pedra")
    print("2)Papel")
    print("3)Tesoura")
    print("4)Lagarto")
    print("5)Spock")
    print("6) Show Scores")
    print("7)Sair do Programa")
    
   
    opcao = int(input("O que você escolhe: "))
    
    if opcao == 1:
        escolhaUsuario = "pedra"
    elif opcao == 2:
        escolhaUsuario = "papel"
    elif opcao == 3:
        escolhaUsuario = "tesoura"
    elif opcao == 4:
        escolhaUsuario = "Lagarto"
    elif opcao == 5:
        escolhaUsuario = "Spock"
    elif opcao == 6:
        print ("Pontuações: ")
        print ("Usuário: ", userScore)
        print ("Pc: ", pcScore)
        print ("Porcentagem de vitórias: ", porcent(), "% " )
        continue
    elif opcao == 7: 
        print ("Nos vemos!")
        break
    else:
        print ("Valor Invalido")
        continue
        
    print("Tua escolha: ", escolhaUsuario)   
    if aleatorio == 0:
        escolhaPc = "pedra"
    elif aleatorio == 1:
        escolhaPc = "papel"
    elif aleatorio == 2:
        escolhaPc = "tesoura"
    elif aleatorio == 3:
        escolhaPc = "Lagarto"
    elif aleatorio == 4:
        escolhaPc = "Spock"
    print("PC escolheu: ", escolhaPc)
    print("...")
    
    if escolhaPc == "pedra" and escolhaUsuario == "papel":
        print("Ganhou, papel cobre pedra")
        winUser = winUser + 1
    elif escolhaPc == "pedra" and escolhaUsuario == "Spock":
        print("Ganhou, spock vaporiza pedra") 
        winUser = winUser + 1
    elif escolhaPc == "papel" and escolhaUsuario == "tesoura":
        print("Ganhou, tesoura corta papel")
        winUser = winUser + 1
    elif escolhaPc == "papel" and escolhaUsuario == "Lagarto":
        print("Ganhou, lagarto come papel")
        winUser = winUser + 1
    elif escolhaPc == "tesoura" and escolhaUsuario == "pedra":
        print("Ganhou, pedra amassa tesoura")
        winUser = winUser + 1
    elif escolhaPc == "tesoura" and escolhaUsuario == "Spock":
        print("Ganhou, Spock quebra tesoura")
        winUser = winUser + 1
    elif escolhaPc == "Lagarto" and escolhaUsuario == "pedra":
        print("Ganhou, pedra esmaga lagarto ")
        winUser = winUser + 1
    elif escolhaPc == "Lagarto" and escolhaUsuario == "tesoura":
        print("Ganhou, tesoura decapita lagarto ")
        winUser = winUser + 1
    elif escolhaPc == "Spock" and escolhaUsuario == "Lagarto":
        print("Ganhou, largato envenena Spock")
        winUser = winUser + 1
    elif escolhaPc == "Spock" and escolhaUsuario == "papel":
        print("Ganhou, papel refuta spock")
        winUser = winUser + 1
        
    if escolhaUsuario == "pedra" and escolhaPc == "papel":
        print("Perdeu, papel cobre pedra")
        pcWin = pcWin + 1
    if escolhaUsuario == "pedra" and escolhaPc == "Spock":
        print("Perdeu, spock vaporiza pedra")
        pcWin = pcWin + 1
    elif escolhaUsuario == "papel" and escolhaPc == "tesoura":
        print("Perdeu, tesoura corta papel")
        pcWin = pcWin + 1
    elif escolhaUsuario == "papel" and escolhaPc == "Lagarto":
        print("Perdeu, lagarto come papel")
        pcWin = pcWin + 1
    elif escolhaUsuario == "tesoura" and escolhaPc == "pedra":
        print("Perdeu, pedra amassa tesoura")
        pcWin = pcWin + 1
    elif escolhaUsuario == "tesoura" and escolhaPc == "Spock":
        print("Perdeu, Spock quebra tesoura")
        pcWin = pcWin + 1
    elif escolhaUsuario == "Lagarto" and escolhaPc == "pedra":
        print("Perdeu, pedra esmaga lagarto")
        pcWin = pcWin + 1
    elif escolhaUsuario == "Lagarto" and escolhaPc == "tesoura":
        print("Perdeu, tesoura decapita lagarto")
        pcWin = pcWin + 1
    elif escolhaUsuario == "Spock" and escolhaPc == "Lagarto":
        print("Perdeu, largato envenena Spock")
        pcWin = pcWin + 1
    elif escolhaUsuario == "Spock" and escolhaPc == "papel":
        print("Perdeu, papel refuta spock")
        pcWin = pcWin + 1
     
        
    elif escolhaPc == escolhaUsuario:
        print("Empate")
    again = input("Jogar novamente? s/n: ")
    if 's' in again:
        continue
    elif 'n' in again:
        print("Nos vemos!")
        break
    else:
        print("Valor Invalido")

    userScore = 0
    pcScore = 0
    totalScore = 0

    def percent():
        if totalScore > 0: 
            x = ((totalScore - pcScore) / totalScore) * 100
            return x
        elif totalScore == 0:
            x = 0
            return x

    userScore = userScore + winUser
    pcScore = pcScore + pcWin
    totalScore = userScore + pcScore

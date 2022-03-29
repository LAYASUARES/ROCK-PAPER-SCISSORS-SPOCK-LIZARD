#encoding:UTF-8
import random

while True: 
    aleatorio = random.randrange(0, 5)
    escolhaPc = ""
    print("1)Pedra")
    print("2)Papel")
    print("3)Tesoura")
    print("4)Lagarto")
    print("5)Spock")
    print("6)Sair do Programa")
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
    elif escolhaPc == "pedra" and escolhaUsuario == "Spock":
        print("Ganhou, spock vaporiza pedra") 
    elif escolhaPc == "papel" and escolhaUsuario == "tesoura":
        print("Ganhou, tesoura corta papel")
    elif escolhaPc == "papel" and escolhaUsuario == "Lagarto":
        print("Ganhou, lagarto come papel")
    elif escolhaPc == "tesoura" and escolhaUsuario == "pedra":
        print("Ganhou, pedra amassa tesoura")
    elif escolhaPc == "tesoura" and escolhaUsuario == "Spock":
        print("Ganhou, Spock quebra tesoura")
    elif escolhaPc == "Lagarto" and escolhaUsuario == "pedra":
        print("Ganhou, pedra esmaga lagarto ")
    elif escolhaPc == "Lagarto" and escolhaUsuario == "tesoura":
        print("Ganhou, tesoura decapita lagarto ")
    elif escolhaPc == "Spock" and escolhaUsuario == "Lagarto":
        print("Ganhou, largato envenena Spock")
    elif escolhaPc == "Spock" and escolhaUsuario == "papel":
        print("Ganhou, papel refuta spock")
        
    if escolhaUsuario == "pedra" and escolhaPc == "papel":
        print("Perdeu, papel cobre pedra")
    if escolhaUsuario == "pedra" and escolhaPc == "Spock":
        print("Perdeu, spock vaporiza pedra")
    elif escolhaUsuario == "papel" and escolhaPc == "tesoura":
        print("Perdeu, tesoura corta papel")]
    elif escolhaUsuario == "papel" and escolhaPc == "Lagarto":
        print("Perdeu, lagarto come papel")
    elif escolhaUsuario == "tesoura" and escolhaPc == "pedra":
        print("Perdeu, pedra amassa tesoura")
    elif escolhaUsuario == "tesoura" and escolhaPc == "Spock":
        print("Perdeu, Spock quebra tesoura")
    elif escolhaUsuario == "Lagarto" and escolhaPc == "pedra":
        print("Perdeu, pedra esmaga lagarto")
    elif escolhaUsuario == "Lagarto" and escolhaPc == "tesoura":
        print("Perdeu, tesoura decapita lagarto")
    elif escolhaUsuario == "Spock" and escolhaPc == "Lagarto":
        print("Perdeu, largato envenena Spock")
    elif escolhaUsuario == "Spock" and escolhaPc == "papel":
        print("Perdeu, papel refuta spock")
     
        
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
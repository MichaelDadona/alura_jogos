import random

# transformei em função para ser executado apenas quando chamado no index.py
def jogaradivinhacao():
    print("+++++++++++++++++++")
    print("Jogo da adivinhação")
    print("+++++++++++++++++++")
    print("")

    # Gera um numero aleatorio de 1 a 100
    numero = random.randrange(1,101)
    
    tentativas = 0
    rodada = 1
    pontos = 1000

    print("Escolha o nível de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Digite o nível: "))
    print("")

    if(nivel == 1):
        tentativas = 20

    elif(nivel == 2):
        tentativas = 10

    else:
        tentativas = 3

        

    while(rodada <= tentativas):

        print(f"Rodada {rodada} de {tentativas}")
        chutestr = input("Digite um numero: ")
        chute = int(chutestr)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um numero de 1 a 100")
            continue

        acertou = (chute == numero)
        maior   = (chute  > numero)
        menor   = (chute  < numero)

        print("Você digitou o numero ", chute)

        if(acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        
        else:
            if(maior):
                print("Você errou, chute foi maior que o numero! ")

            elif(menor):
                print("Você errou, chute foi menor que o numero!") 
            pontos = pontos - chute

        rodada = rodada +1        
    
    print("")
    print("FIM DO GAME!!!")  


# Comando exclusivo para conseguir rodar o Adivinhacao sem ser pelo index.py
if(__name__ == "__main__"):
    jogaradivinhacao()           
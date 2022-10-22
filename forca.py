import random

# transformei em função para ser executado apenas quando chamado no index.py
def jogarforca():

    mensagem_inicio()
    
    palavra_secreta = carrega_palavra_secreta()


    # letras acertadas recebe "_" para cada LETRA da palavra_secreta
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    # Enquanto não enforcou e não acertou   
    while(not enforcou and not acertou):
        chute = input("Digite uma Letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta): 
            posicao = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[posicao] = letra    
                posicao = posicao + 1
        else:
            erros = erros +1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)   
    print("Fim do Jogo!!")
    
    

def mensagem_inicio():
    print("")    
    print("+++++++++++++++++++")
    print("Jogo da forca")
    print("+++++++++++++++++++")
    print("")    

def carrega_palavra_secreta():
    # abrindo o arquivo de palavras
    arquivo = open("palavras.txt", "r")
    lista = []

    for linha in arquivo:
        linha = linha.strip()
        lista.append(linha)
  
    arquivo.close()

    # gera um random com o tamanho da palavra da LISTA (0, 6)   
    numero = random.randrange(0, len(lista))
    # a palavra secreta é o numero da minha lista (é a posição)    
    palavra_secreta = lista[numero].upper()
    # esta retornando a palavra secreta para fora do def
    return palavra_secreta
    
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")    
    
    
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")   
    
    
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()    
    
# Comando exclusivo para conseguir rodar o forca sem ser pelo index.py
# ele vai ler todo o arquivo e em seguida executar a função jogarforca()
if(__name__ == "__main__"):
    jogarforca()               


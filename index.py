import forca
import Adivinhacao

print("+++++++++++++++++++")
print("Escolha o seu jogo")
print("+++++++++++++++++++")
print("")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Escolha o jogo! "))

print("")
print("")

if(jogo == 1):
    forca.jogarforca()

else:  
    Adivinhacao.jogaradivinhacao()
import random

def jogar():
    y = int(input(" Quantos jogos ? "))

    while y > 0:
        x = random.sample(range(1,26), 15)
        x.sort(key=int)
        print(x)
        y -= 1
    
if(__name__ == "__main__"):
    while 1:
        jogar()  
    
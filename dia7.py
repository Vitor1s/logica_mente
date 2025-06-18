#adivinhe o numero 

import random

print("Bem-vimdo adivinhe o numero")

#repetir  o codigo ate o ususario acertart

while True:

    #gerar numero aleatorio
    numero_secreto = random.randint(1, 30)

    tentativas = 5

    print ("Pensei entre 1 e 30!!")
    print(f"Voce tem {tentativas}" " tentativas para acertar o numero")

   

   #valida se o usuario digitou um numero 
    while tentativas > 0:
        palpite = input("Digite seu palpite: ")

       #loop para as tentativas ateacabar 
        if not palpite.isdigit():
            print("Numero invalido, tente novamente")
            continue

        #converter palpite para inteiro
        palpite = int(palpite)

        #Ver se o numero esta dentro dos 1 a 30
        if palpite < 1 or palpite > 30:
            print("O numero esta entre 1 e 30")
            continue

        #diminuir as tentativa
        tentativas -= 1

        #validar se o palpite esta correto
        if palpite == numero_secreto:
            print(f"Parabens!Você achou o numero, sobrou algumas tentativas: {5 - tentativas}")
            break
        
        elif palpite < numero_secreto:
            print("O numero secreto é maior, tente novamente")
        else:
            print("O numero secreto é menor, tente novamente") 

            print(f"Tentativas restantes: {tentativas}")  
        break
    break
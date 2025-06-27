#Adivinhe um numero projeot basico de um joguinho para divinahr um numero otimo para treinar a logica e python em si 

import random  # Importa o módulo random para gerar números aleatórios
  
# Loop principal: repete o jogo até o jogador escolher sair
while True:
    # Gera um número aleatório entre 1 e 50 para o jogador adivinhar
    ache_onumero = random.randint(1, 50)

    tentativas = 5  # Define quantas tentativas o jogador terá

    print("O número está entre 1 e 50")
    print("Acerte o número para ganhar; para isso você tem 5 tentativas\n")

    # Loop de palpites: enquanto ainda houver tentativas
    while tentativas > 0:
        # Pede ao jogador um palpite
        palpite = input("Diga qual pode ser o número certo: ")

        # Validação 1: verifica se o palpite contém apenas dígitos
        if not palpite.isdigit():
            print("Número inválido, digite apenas números.")
            continue  # Volta ao início do loop sem descontar tentativa

        palpite = int(palpite)  # Converte a string em inteiro

        # Validação 2: garante que o palpite esteja na faixa de 1 a 50
        if palpite < 1 or palpite > 50:
            print("Lembre-se: o número está entre 1 e 50.")
            continue  # Volta ao início do loop sem descontar tentativa

        tentativas -= 1  # Desconta uma tentativa após validar o palpite

        # Verifica se o palpite é igual ao número gerado
        if palpite == ache_onumero:
            print(f"Você acertou! Ainda tinha {tentativas} tentativas sobrando.\n")
            break  # Sai do loop de palpites — jogador ganhou

        # Se não acertou, dá dica: número correto é maior ou menor
        elif palpite < ache_onumero:
            print("O número é maior.")
        else:
            print("O número é menor.")
       
        # Informa quantas tentativas ainda restam
        print(f"Tentativas restantes: {tentativas}\n")

    else:
        # Este bloco é executado se o jogador não acertou em nenhuma tentativa
        print(f"Você perdeu! O número era {ache_onumero}.\n")

    # Pergunta se o jogador quer jogar novamente
    jogar_denovo = input("Deseja jogar de novo? (s/n): ").lower()
    if jogar_denovo != 's':
        print("Obrigado por jogar! Até a próxima.")
        break  # Sai do loop principal e encerra o programa


# random.randint(1, 50)    # função do módulo random
# input("…")               # built-in que lê do teclado
# palpite.isdigit()        # método (função) de string que verifica se é dígito
# int(palpite)             # built-in que converte string em int
# print("…")               # built-in que exibe na tela
# jogar_denovo.lower()     # método de string que retorna tudo em minúsculas

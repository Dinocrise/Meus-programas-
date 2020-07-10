import random

def vez_de_quem(quem_comeca):
    quem_comeca = random.randrange(2)
    if quem_comeca == 0:
        return ("você começa")
    elif quem_comeca == 1:
        return ("Computador Começa")

print ("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

escolha = int(input(""))

if escolha == 1:
    print ("Você escolheu uma partida isolada!")


elif escolha == 2:
    print("Você escolheu um campeonato!")
    print("****Rodada 1****")
    quantidade_tabuleiro = int(input("Quantas peças? "))
    pecas_por_jogada = int(input("Limite de peças por jogada? "))
    quem_comeca = vez_de_quem("Vez de alguem")
    
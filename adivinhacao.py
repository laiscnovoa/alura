import random


def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print('Qual o nível de dificuldade?')
    nivel = int(input('(1) Fácil / (2) Médio / (3) Difícil: '))

    if nivel == 1:
        tentativa = 20
    elif nivel == 2:
        tentativa = 10
    else:
        tentativa = 5

    for rodada in range(1, tentativa + 1):
        print('Tentativa {} de {}'.format(rodada, tentativa))
        chute = int(input("Digite o seu número de 1 a 100: "))
        print("Você digitou: ", chute)

        if chute < 1 or chute > 100:
            print('Você deve escolher entre 1 e 100')
            continue
        acerto = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos

        if acerto:
            print('Você acertou e fez {} pontos'.format(pontos))
            break
        else:
            if maior:
                print('Você errou! O seu chute foi maior que o número secreto.')
                if rodada == tentativa:
                    print('O número secreto era {} e você fez {} pontos'.format(numero_secreto, pontos))
            elif menor:
                print('Voce errou! O seu chute foi menor que o número secreto')
                if rodada == tentativa:
                    print('O número secreto era {} e você fez {} pontos'.format(numero_secreto, pontos))

    print('Fim de Jogo')


if __name__ == '__main__':
    jogar()

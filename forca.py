def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_chave = 'banana'.upper()
    letras_certas = ['_' for letra in palavra_chave]

    print(letras_certas)
    acerto = False
    forca = False
    erros = 0

    while not acerto and not forca:
        chute = input('Que letra quer testar? ').strip().upper()

        if chute in palavra_chave:
            index = 0
            for letra in palavra_chave:
                if chute.upper() == letra.upper():
                    letras_certas[index] = letra
                index += 1
        else:
            erros +=1
            print(f'Errado, você ainda tem {6 - erros} tentativas')

        forca = erros == 6
        acerto = '_' not in letras_certas
        print(letras_certas)

    if acerto:
        print('Ganhou!')
    else:
        print('Perdeu!')

    print('Fim do Jogo')

if __name__ == '__main__':
    jogar()

import random

def jogar():
    imprime_mensagem_inicial()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        palpite = pede_palpite()
        if(palpite in palavra_secreta):
            marca_palpite_correto(letras_acertadas, palavra_secreta, palpite)

            acertou = "_" not in (letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        print(letras_acertadas)
        enforcou = (erros == 7)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def marca_palpite_correto(letras_acertadas, palavra_secreta, palpite):
    index = 0
    for letra in palavra_secreta:
        if (palpite == letra):
            letras_acertadas[index] = letra
        index += 1

def carrega_palavra_secreta():
    palavras = []
    arquivo = open("palavras.txt", "r")
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    indice_palavra_secreta = random.randrange(0, len(palavras))
    palavra_secreta = palavras[indice_palavra_secreta].strip().upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    # Cria uma lista contendo n caracteres do tipo "_" onde n é o tamanho da palavra passada à função.
    return ["_" for letra in palavra]

def imprime_mensagem_inicial():
    print("********************************")
    print("***Bem vindo ao jogo de forca***")
    print("********************************")

def pede_palpite():
    palpite = input("Digite uma letra que você acredita existir na palavra secreta: ")
    # A linha abaixo remove quaisquer espaços que o usuário possa ter digitado antes e/ou depois da letra.
    return palpite.strip().upper()

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
        print(" |      \     ")
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
#
# O comando if abaixo testa se o módulo adivinhacao.py foi carregado a partir de um import ou está sendo executado
# diretamente da linha de comando. A condção do comando if somente será true se o módulo estiver sendo executado
# por linha de comando. Deve-se observar que o comando abaixo não faz mais parte do corpo da função jogar().
# IMPORTANTE: esse bloco deve ser a última parte do código. Se ele for colocado acima de alguma outra função
# a função colocada abaixo ainda não estará definida e ocorrerá um erro.
#
if(__name__ == "__main__"):
    jogar()


import random

#
# Se o código presente no corpo desse arquivo Python não estiver definido dentro de uma função e o arquivo
# adivinhacao for importado por outro código, como é o caso do arquivo jogos.py, o código aqui presente
# será automaticamente executado tão logo o import seja realizado. A partir do momento em que o código estiver
# contido em uma função, a execução somente ocorrerá quando houver uma chamada explícita a adivinhacao.jogar()
#
def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    # Geração de um número aleatório entre 0.0 e 1.0. A multiplicação por 100 e o round são para tornar o número
    # aleatório em um inteiro. Mas há um problema nessa abordagem: se o número aleatório for 0.0, o inteiro gerado
    # será 0, que é inválido para o contexto do programa.
    # numero_secreto = round(random.random() * 100)
    #
    # Assim sendo, o melhor é utilizar a função randrange:
    numero_secreto = random.randrange(1,101)
    # Lembrando que o segundo parâmetro é exclusivo: 101 não faz parte da faixa aceita. O último valor aceito é 100.
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Escolha o nível de dificuldade: (1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Faça sua escolha:"))
    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5
    # Sintaxe do loop usando comando while
    # while(rodada <= total_tentativas):
    #
    # Sintaxe do loop usando comando for. O segundo argumento da função range é exclusivo. Isto é, o for será executado
    # enquanto o valor de 'rodada' for menor que o valor da variável total_tentativas. Se não fosse somando 1 ao valor
    # da variável total_tentativas a iteração ocorreria somente de 1 a 2.
    #
    for rodada in range(1, total_tentativas+1):
        # Usando String interpolation
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        # Por padrão quando se usa o input a variável que receberá o valor vindo do input será do tipo str
        chute_str = input("Digite um número entre 1 e 100: ")

        print("Você digitou o número ",chute_str)

        # Converte o valor de chute_str para uma variável do tipo int
        chute = int(chute_str)

        if(chute < 0 or chute > 100):
            print("O número informado está fora da faixa permitida")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        # Blocos de comandos if / else devem ser iniciados com : (dois-pontos) como é o caso abaixo.
        if(numero_secreto == chute):
            # O Python exige uma identação de 4 espaços para que o comando seja considerado parte integrante de uma condição
            # if ou else. Tudo aquilo que tiver que ser executado dentro do bloco corresponde ao if ou ao else deve estar
            # devidamente identado. O primeiro comando que não estiver devidamente identado será considerado como fora
            # do bloco if / else.
            #
            print("Você acertou! Você fez {} pontos".format(pontos))
            break
        else:
            print("Você errou!")
            if(maior):
                print("O número que você digitou é maior que o número secreto.")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {} pontos!".format(numero_secreto, pontos))
            elif(menor):
                print("O número que você digitou é menor que o número secreto.")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {} pontos!".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        # No caso de loop usando o comando for não se deve somar 1 ao valor da variável 'rodada'
        # rodada = rodada + 1

    # Conforme mencionado acima, a linha abaixo será executada independentemente do resultado da condiçã if /else acima.
    print("Fim do jogo")

#
# O comando if abaixo testa se o módulo adivinhacao.py foi carregado a partir de um import ou está sendo executado
# diretamente da linha de comando. A condção do comando if somente será true se o módulo estiver sendo executado
# por linha de comando. Deve-se observar que o comando abaixo não faz mais parte do corpo da função jogar().
#
if(__name__ == "__main__"):
    jogar()
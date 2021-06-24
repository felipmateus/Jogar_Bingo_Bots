
from jogador import Jogador
from random import randint
import numpy as np
import colorama
from time import sleep



    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

    # Reseta as cores para o padrao
    colorama.init(autoreset=True)


    # Funcao para imprimir cores do tabuleiro que foram acerto
    def printar_com_cores(x):
        c = colorama.Fore.GREEN if x in resultado_da_rodada else colorama.Fore.RESET
        return f'{c}{x}'


    # Definindo as cores dos prints que correspondem a funcao printar_com_cores
    np.set_printoptions(formatter={'int': printar_com_cores})


    # Funcao para imprimir na tela o vencedor do jogo
    def printar_vencedor(jogador, resultado_da_rodada):
        # Printando os resultados
        print("Resultados: ", end=' ')

        # Para cada resultado_da_rodada :
        for i in resultado_da_rodada:

            # Se o elemento do resultado_da_rodada estiver presente no tabuleiro do vencedor, entao:
            if i in jogador.cartela:

                # Pinta os elementos que correspondem com o tabuleiro do vencedor com a cor VERDE
                print(colorama.Fore.GREEN + f"{i}, ", end=' ')

            # Se o elemento do resultado_da_rodada nao estiver presente no tabuleiro do vencedor, entao:
            else:

                # Pinta os elementos que correspondem com o tabuleiro do vencedor com a cor BRANCA
                print(f"{i}, ", end=' ')

        # Printando numero de jogadas
        print(f"\nNúmero de rodadas: {rodada}")

        # Printando o tabuleiro do vencedor
        for i in jogador.cartela:
            print(i)

        # Printando o nome do vencedor em VERMELHO
        print(colorama.Fore.RED + f"{jogador.nome} fez Bingo!!!\n")


    # Pergunta ao usuario quantos jogadores irao participar
    # numero_de_jogadores=int(input("Digite o numero de jogadores: "))

    # Numero de jogadores
    numero_de_jogadores = 25

    # Instancia a classe Jogador de acordo com o numero de jogadores escolhido pelo usuario e insere na lista jogadores
    jogadores = [Jogador(f"Jogador {i + 1}") for i in range(numero_de_jogadores)]

    # Pergunta ao usuário o nome dele
    # nome_do_Jogador=input("Digite o seu nome: ")
    nome_do_Jogador = self.inp

    # bingo_ui = Ui_MainWindow()

    # nome_do_jogador = bingo_ui.inputNome.vallue

    # Instanciando usuário como Jogador
    usuario = Jogador(nome_do_Jogador)

    # Insere o usuário na lista jogadores
    jogadores.append(usuario)
    # Inicializa a lista dos resultados das jogadas vazia
    resultado_da_rodada = []

    # Define vencedor igual a falso
    vencedor = False

    # Inicializa um contador para as rodadas
    rodada = 0
    # Enquanto o atributo vencedor da Classe Bingo for falso, faça algo:
    while vencedor == False:

        # Resultado recebe um valor aleatório entre 1 e 50
        resultado = randint(1, 50)

        # Se já tiver saido o resultado, busca outro numero aleatorio entre 1 e 50
        while resultado in resultado_da_rodada:
            resultado = randint(1, 50)

        # Incrementa rodada em 1
        rodada += 1

        # Salva na lista resultado_da_rodada
        resultado_da_rodada.append(resultado)

        # Verifica se o resultado esta na cartela
        if resultado in usuario.cartela:

            # Se o resultado estiver na cartela imprime em VERDE
            print(f"\n{colorama.Fore.GREEN}Rodada {rodada}: {resultado}\n")
        else:

            # Se o resultado nao estiver na cartela imprime em VERMELHO
            print(f"\n{colorama.Fore.LIGHTRED_EX}Rodada {rodada}: {resultado}\n")

        # Printa a cartela do usuario
        for i in usuario.cartela:
            print(i)

        # Espera alguns segundos para a próxima rodada
        sleep(2.5)

        print("\n")

        # Para cada jogador na lista de jogadores, faça:
        for jogador in jogadores:

            # Se o resultado do Bingo estiver no tabuleiro do jogador, entao:
            if resultado in jogador.cartela:

                # indice_linha recebe o indice da linha do tabuleiro em que o resultado está
                indice_linha = np.where(jogador.cartela == resultado)[0][0]

                # indice_coluna recebe o indice da coluna do tabuleiro em que o resultado está
                indice_coluna = np.where(jogador.cartela == resultado)[1][0]

                """"
                    Com a saída desse resultado o jogador venceu ?

                    Devemos verificar se ele fez bingo, por tanto utilizamos o método da classe
                    Jogador para conferir se esse resultado completou a linha do Bingo.

                    Se o jogador fez bingo jogadorBingo recebe True

                    Se o jogador nao fez bingo jogadorBingo recebe False
                """
                jogador_Fez_Bingo = jogador.jogador_Fez_Bingo(resultado, indice_linha, indice_coluna)

                # Se jogador_Fez_Bingo é igual a True, entao:
                if jogador_Fez_Bingo:
                    # Imprime na tela que o jogador venceu
                    printar_vencedor(jogador, resultado_da_rodada)

                    # vencedor recebe True para sair do While
                    vencedor = True

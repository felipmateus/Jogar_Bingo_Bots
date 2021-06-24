from random import randint
from numpy import zeros


# Classe Jogador
class Jogador():

    # Inicializando a classe com os atributos nome,tabuleiro e tabuleiro_Comparacao
    def __init__(self, nome):

        # Atributo nome
        self.nome = nome

        # Definindo a dimensao da cartela como 4x4
        self.dimensao_Cartela = 4

        # Atributo cartela - É criado pela funcao cria_Cartela()
        self.cartela = self.cria_Cartela()

        # Atributo cartela_Comparacao - Matriz totalmente nula self.dimensao_Cartelaxself.dimensao_Cartela
        self.cartela_Comparacao = zeros((self.dimensao_Cartela, self.dimensao_Cartela), dtype=int)

    # Funcao responsavel por criar um cartela de Bingo para o jogador
    def cria_Cartela(self):

        # Matriz totalmente nula self.dimensao_Cartelaxself.dimensao_Cartela
        cartela_Jogador = zeros((self.dimensao_Cartela, self.dimensao_Cartela), dtype=int)

        # Para cada linha de 0-self.dimensao_Cartela
        for i in range(0, self.dimensao_Cartela):

            # Para cada coluna de 0-self.dimensao_Cartela:
            for j in range(0, self.dimensao_Cartela):

                # Gera um número aleatório entre 1 e 50
                elemento_da_Cartela = randint(1, 50)

                # Enquanto o tabuleiro possuir um elemento igual ao candidato gera outro numero aleatorio entre 1 e 50
                while elemento_da_Cartela in cartela_Jogador:
                    elemento_da_Cartela = randint(1, 50)

                # Tabuleiro criado com elementos que nao se repetem
                cartela_Jogador[i][j] = elemento_da_Cartela

        # Retorna cartela_Jogador
        return cartela_Jogador

    # Funcao que verifica se o jogador fez Bingo ou nao
    def jogador_Fez_Bingo(self, resultado_Jogada, indice_linha, indice_coluna):

        # Adiciona o elemento na posicao original do tabuleiro do jogador no tabuleiro_Comparacao
        self.cartela_Comparacao[indice_linha][indice_coluna] = resultado_Jogada

        # Se a linha do tabuleiro_Comparacao nao possuir zeros, entao:
        if 0 not in self.cartela_Comparacao[indice_linha]:
            # Retorna True - Jogador fez Bingo
            return True


0
0
0
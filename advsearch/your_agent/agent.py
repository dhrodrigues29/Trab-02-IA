import random
from typing import Tuple

from ..othello.gamestate import GameState

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

inf_positivo = float('inf')
inf_negativo = float('-inf')

profundidade = 0

def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns an Othello move
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    # Lembrar: essa função deve retornar uma JOGADA (x,y)
    #estado = state.copy()
    #valor_jogada = MAX_joga(estado, inf_positivo, inf_negativo)
    prof = 0

    jogadas = list(state.legal_moves())

    melhor_jogada = 0
    jogada_atual = (0, 0)

    for jogada in jogadas:
        estado = state.next_state(jogada).copy()
        valor_jogada = MAX_joga(estado, inf_positivo, inf_negativo, prof)
        if melhor_jogada < valor_jogada:
            melhor_jogada = valor_jogada
            jogada_atual = jogada

    return jogada_atual


def MAX_joga(state: GameState, alfa, beta, prof):
    if  prof == 5: # criterio de parada é uma função a ser criada que deve limitar a profundidade da busca, seja apenas estipulando um limite de profundidade ou usando uma tecnica mais sofisticada
        prof = 0 # reseta a profundidade para 0
        return contas_pecas_pretas(state)   #  criar função que avalia um estado
    else:
        # inicializa v com -infinito
        v = inf_negativo

        # itera a lista de possiveis movimentos no estado atual do tabuleiro
        # a lista seria do tipo [(1, 1), (2, 3), (3, 6)]
        # para cada jogada dentro dessa lista, o minimax faz seus calculos
        for movimento in list(state.legal_moves()):

            # cria um estado cujo movimento atual causaria 
            estado = state.next_state(movimento) # talvez seja mais apropriado utilizar state.copy() ao inves de state.next_state(movimento)

            # algoritmo segue conforme os slides da poda alfa-beta
            v = max(v, MIN_joga(estado, alfa, beta, prof))
            alfa = max(alfa, v)
            if alfa >= beta:
                break
        prof += 1
        return v # poderiamos também retornar alfa ao inves de v, não afetaria o funcionamento



def MIN_joga(state: GameState, alfa, beta, prof):
    if prof == 5: # criterio de parada é uma função a ser criada que deve limitar a profundidade da busca, seja apenas estipulando um limite de profundidade ou usando uma tecnica mais sofisticada
        prof = 0  # reseta a profundidade para 0
        return contas_pecas_brancas(state)   #  criar função que avalia um estado
    else:
        v = inf_positivo
        for movimento in state.legal_moves():
            estado = state.next_state(movimento)
            v = min(v, MAX_joga(estado, alfa, beta, prof))          
            beta = min(beta, v)
            if beta <= alfa:
                break
        prof += 1
        return v # poderiamos também retornar beta ao inves de v, não afetaria o funcionamento



def contas_pecas_pretas(state: GameState):

    # Cria variavel do tabuleiro usando get_board do GameState
    board = state.get_board()

    # Cria variavel de contagem de pecas brancas usando num_piece do Board para retornar o num de pecas de uma dada cor
    pecas_pretas = board.num_pieces('B')

    return pecas_pretas


def contas_pecas_brancas(state: GameState):

    # Cria variavel do tabuleiro usando get_board do GameState
    board = state.get_board()

    # Cria variavel de contagem de pecas brancas usando num_piece do Board para retornar o num de pecas de uma dada cor
    pecas_brancas = board.num_pieces('W')

    return pecas_brancas


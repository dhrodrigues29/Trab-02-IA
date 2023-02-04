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


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns an Othello move
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    # Lembrar: essa função deve retornar uma JOGADA (x,y)

    valor_jogada = MAX_joga(state, inf_positivo, inf_negativo)
    return valor_jogada


def MAX_joga(state: GameState, alfa, beta):
    if criterio_de_parada(): # criterio de parada é uma função a ser criada que deve limitar a profundidade da busca, seja apenas estipulando um limite de profundidade ou usando uma tecnica mais sofisticada
        return avalia_estado()   #  criar função que avalia um estado
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
            v = max(v, MIN_joga(estado, alfa, beta))
            alfa = max(alfa, v)
            if alfa >= beta:
                break
        return v # poderiamos também retornar alfa ao inves de v, não afetaria o funcionamento



def MIN_joga(state: GameState, alfa, beta):
    if criterio_de_parada(): # criterio de parada é uma função a ser criada que deve limitar a profundidade da busca, seja apenas estipulando um limite de profundidade ou usando uma tecnica mais sofisticada
        return avalia_estado()   #  criar função que avalia um estado
    else:
        v = inf_positivo
        for movimento in state.legal_moves():
            estado = state.next_state(movimento)
            v = min(v, MAX_joga(estado, alfa, beta))
            beta = min(beta, v)
            if beta <= alfa:
                break
        return v # poderiamos também retornar beta ao inves de v, não afetaria o funcionamento


def avalia_estado():

def criterio_de_parada():






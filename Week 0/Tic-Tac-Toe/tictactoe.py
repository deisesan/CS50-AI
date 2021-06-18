from math import inf as infinito
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def initial_state():

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

#Retorna X ou O
def player(board):

    xcount = 0
    ocount = 0

    for i in board:
        xcount += i.count(X)
        ocount += i.count(O)

    if ocount >= xcount:
        return X
    else: 
        return O

#Retorna todas as jogadas disponíveis
def actions(board):

    acoes = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                acoes.append([i, j])
        
    return acoes

#Retorna o tabuleiro que resulta ao fazer a jogada i,j
def result(board, action):

    aux = deepcopy(board)
    aux[action[0]][action[1]] = player(board)

    return aux

#Retorna o ganhador, se houver
def winner(board):

    for comparar in [X, O]:

        if board[0][0] == board[0][1] == board[0][2] == comparar:
            return comparar

        if board[1][0] == board[1][1] == board[1][2] == comparar:
            return comparar    

        if board[2][0] == board[2][1] == board[2][2] == comparar:
            return comparar

        if board[0][0] == board[1][0] == board[2][0] == comparar:
            return comparar

        if board[0][1] == board[1][1] == board[2][1] == comparar:
            return comparar   

        if board[0][2] == board[1][2] == board[2][2] == comparar:
            return comparar

        if board[0][0] == board[1][1] == board[2][2] == comparar:
            return comparar    

        if board[0][2] == board[1][1] == board[2][0] == comparar:
            return comparar

    return EMPTY                     

#Retorna Verdadeiro se o jogo acabou, Falso caso contrário
def terminal(board):

    if winner(board) != EMPTY:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True   

#Retorna 1 se X ganhou, -1 se 0 ganhou, 0 caso contrário.
def utility(board):

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1

    return 0

#Retorna a jogada ótima para o jogador atual
def minimax(board):

    if terminal(board) == True:
        return None

    if player(board) == X:

        valorMax = -infinito

        for acao in actions(board):
            valorAux = minValue(result(board, acao))

            if valorAux > valorMax:
                
                valorMax = valorAux
                retorno = acao

        return retorno

    elif player(board) == O:

        valorMin = infinito

        for acao in actions(board):
            valorAux = maxValue(result(board, acao))

            if valorAux < valorMin:
                valorMin = valorAux
                retorno = acao

        return retorno

def maxValue(board):

    if terminal(board) == True:
        return utility(board)

    valorMax = -infinito

    for acao in actions(board):
        auxiliar = result(board, acao)
        valorMax = max(valorMax, minValue(auxiliar))

    return valorMax

def minValue(board):

    if terminal(board) == True:
        return utility(board)

    valorMin = infinito

    for acao in actions(board):
        auxiliar = result(board, acao)
        valorMin = min(valorMin, maxValue(auxiliar))

    return valorMin  
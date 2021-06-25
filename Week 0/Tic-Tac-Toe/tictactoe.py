from math import inf as infinite
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

    action = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.append([i, j])
        
    return action

#Retorna o tabuleiro que resulta ao fazer a jogada i,j
def result(board, action):

    aux = deepcopy(board)
    aux[action[0]][action[1]] = player(board)

    return aux

#Retorna o ganhador, se houver
def winner(board):

    for mark in [X, O]:

        if board[0][0] == board[0][1] == board[0][2] == mark:
            return mark

        if board[1][0] == board[1][1] == board[1][2] == mark:
            return mark    

        if board[2][0] == board[2][1] == board[2][2] == mark:
            return mark

        if board[0][0] == board[1][0] == board[2][0] == mark:
            return mark

        if board[0][1] == board[1][1] == board[2][1] == mark:
            return mark   

        if board[0][2] == board[1][2] == board[2][2] == mark:
            return mark

        if board[0][0] == board[1][1] == board[2][2] == mark:
            return mark    

        if board[0][2] == board[1][1] == board[2][0] == mark:
            return mark

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

        valueMax = -infinite

        for action in actions(board):
            valueAux = minValue(result(board, action))

            if valueAux > valueMax:
                valueMax = valueAux
                res = action

        return res

    elif player(board) == O:

        valueMin = infinite

        for action in actions(board):
            valueAux = maxValue(result(board, action))

            if valueAux < valueMin:
                valueMin = valueAux
                res = action

        return res

def maxValue(board):

    if terminal(board) == True:
        return utility(board)

    valueMax = -infinite

    for action in actions(board):
        aux = result(board, action)
        valueMax = max(valueMax, minValue(aux))

    return valueMax

def minValue(board):

    if terminal(board) == True:
        return utility(board)

    valueMin = infinite

    for action in actions(board):
        aux = result(board, action)
        valueMin = min(valueMin, maxValue(aux))

    return valueMin  
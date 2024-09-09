"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #raise NotImplementedError
    now_check=board[0]+board[1]+board[2]
    contain_x=now_check.count(X)
    contain_o=now_check.count(O)
    if contain_x == contain_o :
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError
    all_action=set()
    for i in range(3) :
        for j in range(3) :
            if board[i][j] == EMPTY :
                all_action.add((i,j))
    return all_action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError
    new_board=copy.deepcopy(board)
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = player(board)
        return new_board
    else:
        raise ValueError('Please change a place.')



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    for i in range(3):
        base_sign=board[i][1]
        if base_sign != EMPTY and board[i][0] == base_sign and base_sign == board[i][2]:
            if base_sign == X :
                return X
            else:
                return O
    for i in range(3):
        base_sign=board[1][i]
        if base_sign != EMPTY and board[0][i] == base_sign and base_sign == board[2][i]:
            if base_sign == X :
                return X
            else:
                return O
    base_sign=board[1][1]
    if base_sign != EMPTY:
        if board[0][0] == base_sign and board[2][2] == base_sign :
            if base_sign == X :
                return X
            else:
                return O
        elif board[0][2] == base_sign and board[2][0] == base_sign :
            if base_sign == X :
                return X
            else:
                return O
    return None
            


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError
    if winner(board):
        return True
    if None not in board[0] and None not in board[1] and None not in board[2]:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError
    final=winner(board)
    if final == X :
        return 1
    if final == O :
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #raise NotImplementedError
    if terminal(board):
        return None
    def MAX_VALUE(board): 
        if terminal(board): 
            return utility(board) 
        v = -2
        for action in actions(board): 
            v = max(v, MIN_VALUE(result(board, action))) 
        return v
    def MIN_VALUE(board): 
        if terminal(board): 
            return utility(board) 
        v = 2
        for action in actions(board): 
            v = min(v, MAX_VALUE(result(board, action))) 
        return v
    
    if player(board)==X:
        ans=(-2,None)
        for action in actions(board):
            now_value=MIN_VALUE(result(board,action))
            if now_value > ans[0] :
                ans=(now_value,action)
            elif now_value == ans[0] :
                if random.randint(0,1):
                    ans=(now_value,action)
    else:
        ans=(2,None)
        for action in actions(board):
            now_value=MAX_VALUE(result(board,action))
            if now_value < ans[0] :
                ans=(now_value,action)
            elif now_value == ans[0] :
                if random.randint(0,1):
                    ans=(now_value,action)
    return ans[1]

def ab_minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #raise NotImplementedError
    if terminal(board):
        return None
    def ab_MAX_VALUE(board, alpha, beta): 
        if terminal(board): 
            return utility(board)
        now_max = float('-inf')
        for action in actions(board): 
            now_max = max(now_max, ab_MIN_VALUE(result(board, action), alpha, beta))
            if now_max >= beta:
                return now_max 
            alpha = max(alpha, now_max)
        return now_max
    def ab_MIN_VALUE(board, alpha, beta): 
        if terminal(board): 
            return utility(board)
        now_min = float('inf')
        for action in actions(board): 
            now_min = min(now_min, ab_MAX_VALUE(result(board, action), alpha, beta))
            if now_min <= alpha:
                return now_min 
            beta = min(beta, now_min)
        return now_min
    
    alpha, beta = float('-inf'), float('inf')
    now_action = None
    if player(board) == X:
        for action in actions(board):
            now_value=ab_MIN_VALUE(result(board, action), alpha, beta)
            if now_value > alpha:
                alpha = now_value
                now_action = action
            elif now_value == alpha:
                if random.randint(0,1):
                    now_action = action
    else:
        for action in actions(board):
            now_value=ab_MAX_VALUE(result(board, action), alpha, beta)
            if now_value < beta:
                beta = now_value
                now_action = action
            elif now_value == beta:
                if random.randint(0,1):
                    now_action = action
    return now_action
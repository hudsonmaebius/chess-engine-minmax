import chess
from copy import deepcopy
import random


scoring= {'p': -1,
          'n': -3,
          'b': -3,
          'r': -5,
          'q': -9,
          'k': 0,
          'P': 1,
          'N': 3,
          'B': 3,
          'R': 5,
          'Q': 9,
          'K': 0,
          
          }

def eval_board(BOARD):
    score = 0
    pieces = BOARD.piece_map()
    for p in pieces:
        score += scoring[str(pieces[p])]

    return score

def eval_space(BOARD):
    num_moves = len(list(BOARD.legal_moves))

    value = (num_moves/(20+num_moves))
    
    if BOARD.turn == True:
        return value
    else:
        return -value

def min_maxN(BOARD,N):

    #generate list of possible moves
    moves = list(BOARD.legal_moves)

	
    scores = []

    for move in moves:
        copy = deepcopy(BOARD)
        copy.push(move)
        
        if copy.outcome() == None:
            if N>1:
                copy_best_move = min_maxN(copy,N-1)
                copy.push(copy_best_move)

            scores.append(eval_board(copy))

        #if checkmate
        elif copy.is_checkmate():
            return move

        # if stalemate
        else:
            scores.append(-0.1)

        scores[-1] = scores[-1] + eval_space(copy)

    if BOARD.turn == True:
        best_move = moves[scores.index(max(scores))]
    else:
        best_move = moves[scores.index(min(scores))]

    return best_move
        

def min_max1(BOARD):
    return min_maxN(BOARD,1)

def min_max2(BOARD):
    return min_maxN(BOARD,2)

def min_max3(BOARD):
    return min_maxN(BOARD,3)

def min_max4(BOARD):
    return min_maxN(BOARD,4)
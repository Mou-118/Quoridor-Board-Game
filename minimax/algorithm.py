from copy import deepcopy
import pygame
from Quoridor.constant import RED,BLUE

def minimax(position, depth, max_player):
    if depth == 0 or position.winner() != None:
        return position.evaluate_position(), position
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position,1):
            evaluation = minimax(move, depth-1, False)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position,0):
            evaluation = minimax(move, depth-1, True)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move


def simulate_move( move, board,player):
    if move[0] == "move":
        row, col = move[1], move[2]
        board.move_player(player, row, col)
    else: 
        row, col,dir = move[1], move[2],move[3]
        board.place_wall(row, col,dir,BLUE)
        if(player==0):
            board.player1wall=board.player1wall+1
        else:
            board.player2wall=board.player2wall+1      
    return board


def get_all_moves(board, player):
    moves = []
    valid_moves=board.get_possible_moves(player)
    for move in valid_moves:
        temp_board = deepcopy(board)
        new_board = simulate_move( move, temp_board,player)
        moves.append(new_board)
    return moves

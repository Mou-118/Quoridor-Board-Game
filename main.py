import pygame
import math
from Quoridor.board import Board
from Quoridor.constant import  WINDOW_WIDTH,WINDOW_HEIGHT,WHITE,BLACK,RED,BLUE,BOARD_SIZE,CELL_SIZE,h,w
from minimax.algorithm import minimax

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Quoridor")
    board = Board()
    window.fill(WHITE)
    board.draw(window)
    running = True
    while running:
        if board.winner() != None:
            print("Winner Player1") if board.winner()==RED else print("AI Winner")
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x, y = board.players[board.current]
                    x1,y1 = board.players[board.opponent]
                    if(x==x1 and y1==y-1):
                        if board.can_move_to(board.players[board.opponent],x1,y1-1):
                            new_y = y- 2
                            if board.can_move_to(board.players[board.current],x,new_y):
                                board.players[board.current] = (x, new_y)
                                board.changeTurn()
                        elif board.can_move_to(board.players[board.opponent],x1+1,y1) and can_move_to(board.players[board.opponent],x1-1,y1):
                            value=input("Want to move right(r) side of opponet or left(l):")
                            if value.upper() == "R":
                                board.players[board.current] = (x+1, y-1)
                                board.changeTurn()
                            elif value.upper() == "L":
                                board.players[board.current] = (x-1, y-1)
                                board.changeTurn()
                        elif board.can_move_to(board.players[board.opponent],x1+1,y1):
                            board.players[board.current] = (x+1, y-1)
                            board.changeTurn()
                        elif board.can_move_to(board.players[board.opponent],x1-1,y1):
                            board.players[board.current] = (x-1, y-1)
                            board.changeTurn()
                    else:
                        new_y = y - 1
                        if board.can_move_to(board.players[board.current],x,new_y):
                            board.players[board.current] = (x, new_y)
                            board.changeTurn()
                elif event.key == pygame.K_DOWN:
                # Move the current player down
                    x, y = board.players[board.current]
                    x1,y1 =board.players[board.opponent]
                    if(x==x1 and y1==y+1):
                        if board.can_move_to(board.players[board.opponent],x1,y1+1):
                            new_y = y+2
                            if board.can_move_to(board.players[board.current],x,new_y):
                                board.players[board.current] = (x, new_y)
                                board.changeTurn()
                        elif board.can_move_to(board.players[board.opponent],x1+1,y1) and board.can_move_to(board.players[board.opponent],x1-1,y1):
                            value=input("Want to move right(r) side of opponet or left(l):")
                            if value.upper() == "R":
                                board.players[board.current] = (x+1, y+1)
                                board.changeTurn()
                            elif value.upper() == "L":
                                board.players[board.current] = (x-1, y+1)
                                board.changeTurn()
                        elif board.can_move_to(board.players[board.opponent],x1+1,y1):
                            board.players[board.current] = (x+1, y+1)
                            board.changeTurn()
                        elif board.can_move_to(board.players[board.opponent],x1-1,y1):
                            board.players[board.current] = (x-1, y+1)
                            board.changeTurn() 
                    else:
                        new_y = y + 1
                        if board.can_move_to(board.players[board.current],x,new_y):
                            board.players[board.current] = (x, new_y)
                            board.changeTurn()
                elif event.key == pygame.K_LEFT:
                # Move the current player to the left
                    x, y = board.players[board.current]
                    x1,y1 = board.players[board.opponent]
                    if(y==y1 and x1==x-1):
                        if board.can_move_to(board.players[board.opponent],x1-1,y1):
                            new_x = x - 2
                            if board.can_move_to(board.players[board.current],new_x,y):
                                board.players[board.current] = (new_x, y)
                                board.changeTurn()
                    #
                        elif board.can_move_to(board.players[board.opponent],x1,y1-1) and board.can_move_to(board.players[board.opponent],x1,y1+1):
                            value=input("Want to move upper(u) side of opponet or down(d):")
                            if value.upper() == "U":
                                board.players[board.current] = (x-1, y-1)
                                board.changeTurn()
                            elif value.upper() == "D":
                                board.players[board.current] = (x-1, y+1)
                                board.changeTurn()
                        elif board.can_move_to(board.players[board.opponent],x1,y1-1):
                            board.players[board.current] = (x+1, y-1)
                            board.changeTurn()
                        elif board.can_move_to(board.players[board.opponent],x1,y1+1):
                            board.players[board.current] = (x+1, y+1)
                            board.changeTurn()

                    #
                    else:
                        new_x = x - 1
                        if board.can_move_to(board.players[board.current],new_x,y):
                            board.players[board.current] = (new_x, y)
                            board.changeTurn()

                elif event.key == pygame.K_RIGHT:
                # Move the current player to the left
                    x, y = board.players[board.current]
                    x1,y1 = board.players[board.opponent]
                    if(y==y1 and x1==x+1):
                        if board.can_move_to(board.players[board.opponent],x1+1,y1):
                            new_x = x + 2
                            if board.can_move_to(board.players[board.current],new_x,y):
                                board.players[board.currentr] = (new_x, y)
                                board.changeTurn()
                    #
                        elif board.can_move_to(board.players[board.opponent],x1,y1-1) and board.can_move_to(board.players[board.opponent],x1,y1+1):
                            value=input("Want to move upper(u) side of opponet or down(d):")
                            if value.upper() == "U":
                                board.players[board.current] = (x+1, y-1)
                                board.changeTurn()
                            elif value.upper() == "D":
                                board.players[board.current] = (x+1, y+1)
                                board.changeTurn()
                        elif board.can_move_to(board.players[board.opponent],x1,y1-1):
                            board.players[board.current] = (x+1, y-1)
                            board.changeTurn()
                        elif board.can_move_to(board.players[board.opponent],x1,y1+1):
                            board.players[board.current] = (x+1, y+1)
                            board.changeTurn()
                    #
                    else:
                        new_x = x + 1
                        if board.can_move_to(board.players[board.current],new_x,y):
                            board.players[board.current] = (new_x, y)
                            board.changeTurn()

                elif event.key == pygame.K_w:
                    value = input("Enter coordinates to place wall start(x,y) and direction(H:Horizontal,V:Vertical): ")
                    x, y,d = value.split(",")
                    if d.upper() in ["H", "V"]:
                        if d.upper() == "H":
                            direction = 0
                        else:
                            direction = 1
                    row = int(x) 
                    col = int(y)
                    if board.player1wall>10:
                        print("You Placed all of your wall")
                    elif board.can_place_wall(row,col,direction):
                        board.wall.append((row,col,direction,RED))
                        board.player1wall=board.player1wall+1
                        print("You have wall:",(10-board.player1wall))
                        board.changeTurn()            
            if board.current == 1:
                value, board = minimax(board, 4,True)
                board.changeTurn()
            board.draw(window)

        pygame.display.flip()


    pygame.quit()


if __name__ == "__main__":
    main()


import pygame
from Quoridor.constant import WINDOW_WIDTH,WINDOW_HEIGHT,WHITE,BLACK,RED,BLUE,BOARD_SIZE,CELL_SIZE,h,w

cnt1=0
cnt2=0
class Board:
    def __init__(self):
        self.player1wall=0
        self.player2wall=0
        self.current=0 
        self.opponent=1
        self.players = [(0, BOARD_SIZE // 2), (BOARD_SIZE - 1, BOARD_SIZE // 2)]
        self.wall=[]
    def draw(self,window):
        window.fill(WHITE)
    # Draw horizontal lines
        for i in range(1, BOARD_SIZE):
            pygame.draw.line(window, BLACK, (0, i * CELL_SIZE), (WINDOW_WIDTH, i * CELL_SIZE))
    # Draw vertical lines
        for i in range(1, BOARD_SIZE):
            pygame.draw.line(window, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_HEIGHT))
        for i, player in enumerate(self.players):
            x = player[0]
            y = player[1]
            pygame.draw.circle(window, RED if i == 0 else BLUE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2-w//2)    
        for i, wall in enumerate(self.wall):
            row = wall[0]
            col = wall[1]
            dir = wall[2]
            color=wall[3]
            pygame.draw.rect(window, color, (row* CELL_SIZE-10, col * CELL_SIZE, w, h) if dir==1 else (row* CELL_SIZE, col* CELL_SIZE-10, h, w) )
    def is_valid_cell(self,row, col):
        return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE
    
    def evaluate_position(self):
        player_distance = (8-self.players[self.current][0]) if self.current==0 else  self.players[self.current][0]     
        opponent_distance = self.players[self.opponent][0]  if self.current==0 else 8- self.players[self.opponent][0]
        player_progress=(self.players[self.current][0]) if self.current==0 else  8-self.players[self.current][0]
        opponent_progress=8-self.players[self.opponent][0] if self.current==0 else  self.players[self.opponent][0]
        player_wall_count = self.player1wall
        opponent_wall_count = self.player2wall
        player_moves = len(self.get_possible_moves(self.current))
        opponent_moves = len(self.get_possible_moves(self.opponent))
        distance_weight = 1.0
        wall_weight = 0.5
        blocking_weight = 0.5
        progress_weight = 0.5
        position_value = (opponent_distance - player_distance) * distance_weight
        wall_value = (opponent_wall_count - player_wall_count) * wall_weight
        blocking_value = (player_moves - opponent_moves) * blocking_weight
        progress_value = (player_progress - opponent_progress) * progress_weight
        evaluation = position_value + wall_value + blocking_value + progress_value 

        return evaluation

    def winner(self):
        if self.players[0][0]==8:
            return RED
        elif self.players[1][0]==0:
            return BLUE
        return None
    def changeTurn(self):
        if self.current == 1:
            self.current = 0
            self.opponent = 1
        else:
            self.current = 1
            self.opponent = 0
    def move_player(self,player,row,col):
        self.players[player]=(row,col)
    def place_wall(self,row,col,dir,color):
        self.wall.append((row,col,dir,color))
    def can_move_to(self,players, row, col):
        if not self.is_valid_cell(row, col):
            return False
        x, y = players
        if(col== y and row == x + 1):
            for i, wall in enumerate(self.wall):
                r = wall[0]
                c = wall[1]
                d = wall[2]
                if(d==1 and r==x+1 and (c==y or c==y-1)):
                    return False
        elif(col== y and row == x - 1):
            for i, wall in enumerate(self.wall):
                r = wall[0]
                c = wall[1]
                d = wall[2]
                if(d==1 and r==x and (c==y or c==y-1)):
                    return False
        elif(row== x and col == y + 1):
            for i, wall in enumerate(self.wall):
                r = wall[0]
                c = wall[1]
                d = wall[2]
                if(d==0 and c==y+1 and (r==x or r==x-1)):
                    return False
        elif(row== x and col == y - 1):
            for i, wall in enumerate(self.wall):
                r = wall[0]
                c = wall[1]
                d = wall[2]
                if(d==0 and c==y and (r==x or r==x-1)):
                    return False
        return True
    
    def can_place_wall(self,row, col,dir):
        if not self.is_valid_cell(row, col):
            return False
        for i, wall in enumerate(self.wall):
            r = wall[0]
            c = wall[1]
            d = wall[2]
            if(dir==1 and d==1 and row==r and (col==c or col==c-1 or col==c+1)):
                return False
            elif(dir==0 and d==0 and col==c and (row==r or row==r-1 or row==r+1)):
                return False
            elif(dir==0 and d==1 and (row==r-1 and col==c+1)):
                return False
            elif(dir==1 and d==0 and (row==r+1 and col==c-1)):
                return False
        return True
    def get_possible_moves(self, player):
        moves = []
        if player==1:
            op=0
        else:
            op=1
        x, y = self.players[player]
        x1,y1 = self.players[op]
    # up
        if(x==x1 and y1==y-1):
            if self.can_move_to(self.players[op],x1,y1-1):
                new_y = y- 2
                moves.append(("move", x, new_y))
            elif self.can_move_to(self.players[op],x1+1,y1) and self.can_move_to(self.players[op],x1-1,y1):
                moves.append(("move", x+1, y-1))
                moves.append(("move", x-1, y-1))
            elif self.can_move_to(self.players[op],x1+1,y1):
                moves.append(("move", x+1, y-1))
            elif self.can_move_to(self.players[op],x1-1,y1):
                moves.append(("move", x-1, y-1))   
    # down
        elif(x==x1 and y1==y+1):
            if self.can_move_to(self.players[op],x1,y1+1):
                new_y = y+2
                moves.append(("move", x, new_y))
            elif self.can_move_to(self.players[op],x1+1,y1) and self.can_move_to(self.players[op],x1-1,y1):
                moves.append(("move", x+1, y+1))
                moves.append(("move", x-1, y+1))
            elif self.can_move_to(self.players[op],x1+1,y1):
                moves.append(("move", x+1, y+1))
            elif self.can_move_to(self.players[op],x1-1,y1):
                moves.append(("move", x-1, y+1))
    # left
        elif(y==y1 and x1==x-1):
            if self.can_move_to(self.players[op],x1-1,y1):
                new_x = x-2
                moves.append(("move", new_x, y))
            elif self.can_move_to(self.players[op],x1,y1-1) and self.can_move_to(self.players[op],x1,y1+1):
                moves.append(("move", x-1, y-1))
                moves.append(("move", x-1, y+1))
            elif self.can_move_to(self.players[op],x1,y1-1):
                moves.append(("move", x-1, y-1))
            elif self.can_move_to(self.players[op],x1-1,y1):
                moves.append(("move", x-1, y+1)) 
    # right
        elif(y==y1 and x1==x+1):
            if self.can_move_to(self.players[op],x1+1,y1):
                new_x = x+2
                moves.append(("move", new_x, y))
            elif self.can_move_to(self.players[op],x1,y1-1) and self.can_move_to(self.players[op],x1,y1+1):
                moves.append(("move", x+1, y-1))
                moves.append(("move", x+1, y+1))
            elif self.can_move_to(self.players[op],x1,y1-1):
                moves.append(("move", x+1, y-1))
            elif self.can_move_to(self.players[op],x1-1,y1):
                moves.append(("move", x+1, y+1)) 
        else:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if self.can_move_to(self.players[player], new_x, new_y):
                    moves.append(("move", new_x, new_y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x1 + dx, y1 + dy
            for dir in [0,1]:
                if self.can_place_wall(new_x,new_y,dir):
                    if(player==0 and self.player1wall<10):
                        moves.append(("wall",new_x,new_y,dir))
                    elif(player==1 and self.player2wall<10):
                        moves.append(("wall",new_x,new_y,dir))
        return moves

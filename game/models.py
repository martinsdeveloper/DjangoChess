from django.db import models
from dataclasses import dataclass, field
from matplotlib.style import available
import numpy as np


@dataclass
class ChessBoard:
    board: list[int] = field(default_factory=list)
    def zeros(self, range):
        for _ in range:
            yield -1
    def empty_board(self):
        for _ in range(8): 
            yield list(self.zeros(range(0,8)))
    def __init__(self):
        self.board = list(self.empty_board())
    @property
    def clear_board(self):
         self.board = list(self.empty_board())
    @property
    def print(self):
        for row in self.board:
            print(row)
@dataclass
class Knigt:
    moves: ChessBoard
    last_moved: int = 0
    value: int = 2
    def __init__(self,init_x = 0, init_y = 0):
        self.x = init_x
        self.y = init_y
        self.moves = ChessBoard()
    def available_moves(self):
        self.moves.clear_board
        self.moves.board[self.x][self.y] = 1
        for i in (1,-1):
            for n in (2,-2):
                self.moves.board[i+self.x][n+self.y] = 0
                self.moves.board[n+self.x][i+self.y] = 0
    def move(self,move_to_x,move_to_y,turn_no):
        self.x = move_to_x
        self.y = move_to_y
        self.last_moved = turn_no
        self.available_moves()

@dataclass
class Pawn:
    moves: ChessBoard
    last_moved: int = 0
    value: int = 1
    def __init__(self,init_x = 0, init_y = 0):
        self.x = init_x
        self.y = init_y
        self.moves = ChessBoard()
    def available_moves(self):
        self.moves.clear_board
        self.moves.board[self.x][self.y] = 1
        if (self.last_moved == 0):
            self.moves.board[self.x][1+self.y] = 0
            self.moves.board[self.x][2+self.y] = 0
        else:
            self.moves.board[self.x][1+self.y] = 0
            if (1==2):
                # implemented once teams are defined
                print("passe")
    def move(self,move_to_x,move_to_y,turn_no):
        self.x = move_to_x
        self.y = move_to_y
        self.last_moved = turn_no
        self.available_moves()

@dataclass
class Rook:
    moves: ChessBoard
    last_moved: int = 0
    value: int = 4
    def __init__(self,init_x = 0, init_y = 0):
        self.x = init_x
        self.y = init_y
        self.moves = ChessBoard()
    def available_moves(self):
        self.moves.clear_board
        for i in range(0,8):
            self.moves.board[self.x][i] = 0
        for n in range(0,8):
            self.moves.board[n][self.y] = 0
        self.moves.board[self.x][self.y] = 1
    def move(self,move_to_x,move_to_y,turn_no):
        self.x = move_to_x
        self.y = move_to_y
        self.last_moved = turn_no
        self.available_moves()

# rook = Rook()
# rook.move(0,0,0)
# rook.moves.print

@dataclass
class Bishop:
    moves: ChessBoard
    last_moved: int = 0
    value: int = 9
    def __init__(self,init_x = 0, init_y = 0):
        self.x = init_x
        self.y = init_y
        self.moves = ChessBoard()
    def available_moves(self):
        self.moves.clear_board
        for i in range(0,8):
            if (self.x+i < 8):
                if (self.y+i < 8):
                    self.moves.board[self.x+i][self.y+i] = 0
                if (self.y-i >= 0):
                    self.moves.board[self.x+i][self.y-i] = 0
            if (self.x-i >= 0):
                if (self.y+i < 8):
                    self.moves.board[self.x-i][self.y+i] = 0
                if (self.y-i >= 0):
                    self.moves.board[self.x-i][self.y-i] = 0
        self.moves.board[self.x][self.y] = 1
    def move(self,move_to_x,move_to_y,turn_no):
        self.x = move_to_x
        self.y = move_to_y
        self.last_moved = turn_no
        self.available_moves()

# bishop = Bishop()
# bishop.move(3,3,0)
# bishop.moves.print

@dataclass
class Queen:
    moves: ChessBoard
    last_moved: int = 0
    value: int = 9
    def __init__(self,init_x = 0, init_y = 0):
        self.x = init_x
        self.y = init_y
        self.moves = ChessBoard()
    def available_moves(self):
        self.moves.clear_board
        for i in range(0,8):
            if (self.x+i < 8):
                if (self.y+i < 8):
                    self.moves.board[self.x+i][self.y+i] = 0
                if (self.y-i >= 0):
                    self.moves.board[self.x+i][self.y-i] = 0
            if (self.x-i >= 0):
                if (self.y+i < 8):
                    self.moves.board[self.x-i][self.y+i] = 0
                if (self.y-i >= 0):
                    self.moves.board[self.x-i][self.y-i] = 0
        for i in range(0,8):
            self.moves.board[self.x][i] = 0
        for n in range(0,8):
            self.moves.board[n][self.y] = 0
        self.moves.board[self.x][self.y] = 1
    def move(self,move_to_x,move_to_y,turn_no):
        self.x = move_to_x
        self.y = move_to_y
        self.last_moved = turn_no
        self.available_moves()

@dataclass
class King:
    # Not done
    # other pieces are(more or less functional)
    moves: ChessBoard
    last_moved: int = 0
    value: int = 1
    def __init__(self,init_x = 0, init_y = 0):
        self.x = init_x
        self.y = init_y
        self.moves = ChessBoard()
    def available_moves(self):
        self.moves.clear_board
        if (self.last_moved == 0):
            # castling when team added
            print("castling")
        else:
            # check from team movement list if position not in danger + check if attack blocked by a teammate
            if self.x > 0 :
                if self.y - 1 >= 0 :
                    self.moves.board[self.x-1][self.y-1] = 0
                self.moves.board[self.x-1][self.y] = 0
                if self.y + 1 < 8 :
                    self.moves.board[self.x-1][self.y+1] = 0
            if self.x < 8 :
                if self.y - 1 >= 0 :
                    self.moves.board[self.x][self.y-1] = 0
                self.moves.board[self.x][self.y] = 0
                if self.y + 1 < 8 :
                    self.moves.board[self.x][self.y+1] = 0
        self.moves.board[self.x][self.y] = 1
    def move(self,move_to_x,move_to_y,turn_no):
        self.x = move_to_x
        self.y = move_to_y
        self.last_moved = turn_no
        self.available_moves()

# k = King()
# k.move(3,1,2)
# k.moves.print
# # https://www.chess.com/terms/chess-pieces
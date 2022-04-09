

from dataclasses import dataclass, field
from matplotlib.style import available
import numpy as np

@dataclass
class ChessBoard:
    moves: dict
    add_moves: dict
    board: list[int] = field(default_factory=list)
    def zeros(self, range):
        for _ in range:
            yield -1
    def empty_board(self):
        for _ in range(8): 
            yield list(self.zeros(range(1,8)))
    def __init__(self):
        self.board = list(self.empty_board())
        self.moves =  {"Pawn": [[0,1]], "Knigt": [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,-1],[-2,1]]}
        self.add_moves = {"Pawn": [[0,2]] }
    def put_in_position(self, type, x, y):
        self.board = list(self.empty_board())
        self.board[x][y] = 1
        for (xd,yd) in self.moves[type]:
            self.board[x+xd][y+yd] = 0
        return self
    def additional_moves(self, type, x, y):
        self.board = self.put_in_position(type,x,y).board
        for (xd,yd) in self.add_moves[type]:
            self.board[x+xd][y+yd] = 0
        print("additional moves")
        return self
    @property
    def print(self):
        for row in self.board:
            print(row)
@dataclass
class Knigt:
    moves: ChessBoard
    last_moved: int = 0
    value: int = 2
    x: int = 0
    y: int = 0
    def __init__(self,init_x = 0, init_y = 0):
        self.x = init_x
        self.y = init_y
    def available_moves(self):
            self.moves = ChessBoard().put_in_position(self.__class__.__name__, self.x, self.y)
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
    x: int = 0
    y: int = 0
    def __init__(self,init_x = 0, init_y = 0):
        self.x = init_x
        self.y = init_y
    def available_moves(self):
        if (self.last_moved == 0):
            self.moves = ChessBoard().additional_moves(self.__class__.__name__, self.x, self.y)
        elif (1==2):
            print("passe")
        else:
            self.moves = ChessBoard().put_in_position(self.__class__.__name__, self.x, self.y)
    def move(self,move_to_x,move_to_y,turn_no):
        self.x = move_to_x
        self.y = move_to_y
        self.last_moved = turn_no
        self.available_moves()


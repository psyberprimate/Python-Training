



class Piece:
    """Base class for chess Pieces
    """    
    def __init__(self, position : tuple):
        #position x and y or row and column
        self.position : tuple = position
        self.info = {"type" : "", "color" : "", "symbol" : ""}
    
    def get_position(self):
        return self.position
    
    def set_position(self, position : tuple):
        self.position = position
    
    def get_info(self):
        return self.info
    
    def get_type(self):
        return self.info['type']
    
    def get_color(self):
        return self.info["color"]
    
    def get_symbol(self):
        return self.info["symbol"]
    
    def _get_moves(self) -> list:
        row, column = self.get_position()
        viable_moves = []
        #print(f"starting row, column: {row, column}")
        for row2, column2 in self.TILE_MOVEMENTS:
            row_target, column_target = row + row2, column + column2
            #print(f"target row,  column: {row_target, column_target}")
            if 0 <= row_target < 8 and 0 <= column_target < 8:
                viable_moves.append((row_target, column_target))
        return viable_moves


class Pawn(Piece):
    """Class for Pawn chess piece
    """    
    def __init__(self, position : tuple, color: str):
        super().__init__(position=position)
        self.info = {"type" : "pawn", "color" : color, "symbol" : "P"}
        self.TILE_MOVEMENTS_WHITE = [(0, 1)]
        self.TILE_MOVEMENTS_BLACK = [(0, -1)]
    
    def white_or_black(self):
        return self.TILE_MOVEMENTS_WHITE \
            if self.get_color() == "W" else self.TILE_MOVEMENTS_BLACK
    
    def _get_moves(self) -> list:
        row, column = self.get_position()
        viable_moves = []
        for row2, column2 in self.white_or_black():
            row_target, column_target = row + row2, column + column2
            if 0 <= row_target < 8 and 0 <= column_target < 8:
                viable_moves.append((row_target, column_target))
        return viable_moves
        
    def check_move(self, target_tile : tuple, board_state : list) -> bool:
        viable_moves = self._get_moves()
        if target_tile in viable_moves:
            self.set_position(target_tile)
            return True
        else:
            return False
    
    def _eat_piece(self):
        pass
    
    def _check_collision(self):
        pass


class Bishop(Piece):
    """Class for Bishop chess piece
    """  
    def __init__(self, position : tuple, color: str):
        super().__init__(position=position)
        self.info = {"type" : "bishop", "color" : color, "symbol" : "B"}
        self.TILE_MOVEMENTS = [(-1, 1), (1, 1), (-1, -1), (-1, 1)]
    
    def check_move(self): 
        pass
    
    def _eat_piece(self):
        pass


class Knight(Piece):
    """Class for Knigh chess piece
    """    
    def __init__(self, position : tuple, color: str):
        super().__init__(position=position)
        self.info = {"type" : "knight", "color" : color, "symbol" : "N"}
        self.TILE_MOVEMENTS = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                               (-2, 1), (-1, 2), (1, 2), (2, 1)]
    
    def check_move(self):
        pass

    def _eat_piece(self):
        pass
    
    
class Rook(Piece):
    """Class for Rook chess piece
    """    
    def __init__(self, position : tuple, color: str):
        super().__init__(position=position)
        self.info = {"type" : "rook", "color" : color, "symbol" : "R"}
        self.TILE_MOVEMENTS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    def check_move(self):
        pass
    
    def _eat_piece(self):
        pass
    
    
class Queen(Piece):
    """Class for Queen chess piece
    """    
    def __init__(self, position : tuple, color: str):
        super().__init__(position=position)
        self.info = {"type" : "queen", "color" : color, "symbol" : "Q"}
        self.TILE_MOVEMENTS = [(-1, 1), (1, 1), (-1, -1), (-1, 1),
                               (-1, 0), (0, 1), (1, 0), (0, -1)]
    
    def check_move(self):
        pass
    
    def _eat_piece(self):
        pass


class King(Piece):
    """Class for King chess piece
    """    
    def __init__(self, position : tuple, color: str):
        super().__init__(position=position)
        self.info = {"type" : "king", "color" : color, "symbol" : "K"}
        self.TILE_MOVEMENTS = [(-1, 1), (1, 1), (-1, -1), (-1, 1),
                               (-1, 0), (0, 1), (1, 0), (0, -1)]
        
    def check_move(self):
        pass
    
    def _eat_piece(self):
        pass
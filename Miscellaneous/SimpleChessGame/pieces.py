



class Piece:
    
    def __init__(self):
        self.position : tuple = None
        self.type = None
        self.info = None
    
    def get_position(self):
        return self.position
    
    def get_type(self):
        return self.type
    
    def get_info(self):
        return self.info


class Pawn(Piece):
    
    def __init__(self, color: str):
        pass
    
    def check_move(self):
        pass


class Bishop(Piece):
    
    def __init__(self, color: str):
        pass
    
    def check_move(self):
        pass


class Knight(Piece):
    
    def __init__(self, color: str):
        pass
    
    def check_move(self):
        pass

   
class Rook(Piece):
    
    def __init__(self, color: str):
        pass
    
    def check_move(self):
        pass


class Queen(Piece):
    
    def __init__(self, color: str):
        pass
    
    def check_move(self):
        pass


class King(Piece):
    
    def __init__(self, color: str):
        pass
        
    def check_move(self):
        pass


class Piece:
    """Base class for chess Pieces
    """

    def __init__(self, position: tuple):
        # position equals: row, column == (y, x)
        self.position: tuple = position

    def get_position(self):
        return self.position

    def set_position(self, position: tuple):
        self.position = position

    def get_info(self):
        return self.info

    def get_type(self):
        return self.info['type']

    def get_color(self):
        return self.info["color"]

    def get_symbol(self):
        return self.info["symbol"]

    def get_moved(self):
        return self.info["moved"]

    def set_moved(self):
        self.info["moved"] = True

    def check_move(self, target_tile: tuple, board_state: list) -> bool:
        viable_moves = self._get_moves(board_state)
        print(f"viable moves for pawn: {viable_moves}")
        if target_tile in viable_moves:
            self.set_position(target_tile)
            return True
        else:
            return False


class Pawn(Piece):
    """Class for Pawn chess piece
    """

    def __init__(self, position: tuple, color: str):
        super().__init__(position=position)
        self.info = {"type": "pawn", "color": color,
                     "symbol": "P", "moved": False}
        self.TILE_MOVEMENTS_WHITE = [(1, 0)]
        self.TILE_MOVEMENTS_BLACK = [(-1, 0)]
        self.WHITE_attack = [(1, 1), (1, -1)]
        self.BLACK_atttack = [(-1, -1), (-1, 1)]

    def white_or_black_movement(self):
        return self.TILE_MOVEMENTS_WHITE \
            if self.get_color() == "W" else self.TILE_MOVEMENTS_BLACK

    def white_or_black_attack(self):
        return self.WHITE_attack if self.get_color() == "W" else self.BLACK_atttack

    def initial_movement(self):
        return [(2, 0)] if self.get_color() == "W" else [(-2, 0)]

    def _get_moves(self, board_state: list) -> list:

        row, column = self.get_position()
        moveset = self.white_or_black_movement().copy()
        viable_moves = []
        # check if piece has moved or not, if not append the moveset list
        if not self.get_moved():
            print("piece has not moved yet")
            moveset.extend(self.initial_movement())
            self.set_moved()
        print(f"moveset: {moveset}")
        # pawn regular movement
        for row2, column2 in moveset:
            row_target, column_target = row + row2, column + column2
            if 0 <= row_target < 8 and 0 <= column_target < 8:
                if board_state[row_target][column_target] is None:
                    viable_moves.append((row_target, column_target))
        # pawn piece capturing
        for row3, column3 in self.white_or_black_attack():
            row_target2, column_target2 = row + row3, column + column3
            print(f"row_target2, column_target2: {row_target2, column_target2}")
            if 0 <= row_target2 < 8 and 0 <= column_target2 < 8:
                if board_state[row_target2][column_target2] is not None:
                    if board_state[row_target2][column_target2].get_color() \
                        != board_state[row][column].get_color():
                            viable_moves.append((row_target2, column_target2))
        return viable_moves

    @staticmethod
    def _eat_piece(board_state: list, start_position: tuple, target_position: tuple):
        pass


class Bishop(Piece):
    """Class for Bishop chess piece
    """

    def __init__(self, position: tuple, color: str):
        super().__init__(position=position)
        self.info = {"type": "bishop", "color": color, "symbol": "B"}
        self.TILE_MOVEMENTS = [(-1, 1), (1, 1), (-1, -1), (-1, 1)]

    def _get_moves(self, board_state: list) -> list:

        row, column = self.get_position()
        viable_moves = []
        for row2, column2 in self.TILE_MOVEMENTS:
            row_target, column_target = row + row2, column + column2
            while 0 <= row_target < 8 and 0 <= column_target < 8:
                if board_state[row_target][column_target] is None:
                    viable_moves.append((row_target, column_target))
                else:
                    if board_state[row_target][column_target].get_color() \
                            != board_state[row][column].get_color():
                        viable_moves.append((row_target, column_target))
                    break
                row_target += row2
                column_target += column2
        return viable_moves


class Knight(Piece):
    """Class for Knigh chess piece
    """

    def __init__(self, position: tuple, color: str):
        super().__init__(position=position)
        self.info = {"type": "knight", "color": color, "symbol": "N"}
        self.TILE_MOVEMENTS = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                               (-2, 1), (-1, 2), (1, 2), (2, 1)]

    def _get_moves(self, board_state: list) -> list:

        row, column = self.get_position()
        viable_moves = []
        for row2, column2 in self.TILE_MOVEMENTS:
            row_target, column_target = row + row2, column + column2
            if 0 <= row_target < 8 and 0 <= column_target < 8:
                if board_state[row_target][column_target] is None:
                    viable_moves.append((row_target, column_target))
                else:
                    if board_state[row_target][column_target].get_color() \
                            != board_state[row][column].get_color():
                        viable_moves.append((row_target, column_target))
        return viable_moves


class Rook(Piece):
    """Class for Rook chess piece
    """

    def __init__(self, position: tuple, color: str):
        super().__init__(position=position)
        self.info = {"type": "rook", "color": color, "symbol": "R"}
        self.TILE_MOVEMENTS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def _get_moves(self, board_state: list) -> list:

        row, column = self.get_position()
        viable_moves = []
        for row2, column2 in self.TILE_MOVEMENTS:
            row_target, column_target = row + row2, column + column2
            while 0 <= row_target < 8 and 0 <= column_target < 8:
                if board_state[row_target][column_target] is None:
                    viable_moves.append((row_target, column_target))
                else:
                    if board_state[row_target][column_target].get_color() \
                            != board_state[row][column].get_color():
                        viable_moves.append((row_target, column_target))
                    break
                row_target += row2
                column_target += column2
        return viable_moves


class Queen(Piece):
    """Class for Queen chess piece
    """

    def __init__(self, position: tuple, color: str):
        super().__init__(position=position)
        self.info = {"type": "queen", "color": color, "symbol": "Q"}
        self.TILE_MOVEMENTS = [(-1, 1), (1, 1), (-1, -1), (-1, 1),
                               (-1, 0), (0, 1), (1, 0), (0, -1)]

    def _get_moves(self, board_state: list) -> list:

        row, column = self.get_position()
        viable_moves = []
        for row2, column2 in self.TILE_MOVEMENTS:
            row_target, column_target = row + row2, column + column2
            while 0 <= row_target < 8 and 0 <= column_target < 8:
                if board_state[row_target][column_target] is None:
                    viable_moves.append((row_target, column_target))
                else:
                    if board_state[row_target][column_target].get_color() \
                            != board_state[row][column].get_color():
                        viable_moves.append((row_target, column_target))
                    break
                row_target += row2
                column_target += column2
        return viable_moves


class King(Piece):
    """Class for King chess piece
    """

    def __init__(self, position: tuple, color: str):
        super().__init__(position=position)
        self.info = {"type": "king", "color": color, "symbol": "K"}
        self.TILE_MOVEMENTS = [(-1, 1), (1, 1), (-1, -1), (-1, 1),
                               (-1, 0), (0, 1), (1, 0), (0, -1)]

    def _get_moves(self, board_state: list) -> list:

        row, column = self.get_position()
        viable_moves = []
        for row2, column2 in self.TILE_MOVEMENTS:
            row_target, column_target = row + row2, column + column2
            if 0 <= row_target < 8 and 0 <= column_target < 8:
                if board_state[row_target][column_target] is None:
                    viable_moves.append((row_target, column_target))
                else:
                    if board_state[row_target][column_target].get_color() \
                            != board_state[row][column].get_color():
                        viable_moves.append((row_target, column_target))
                    break
                row_target += row2
                column_target += column2
        return viable_moves

    def _eat_piece(self):
        pass

import copy


class Piece:
    """Base class for chess Pieces. Contains the basics
    functions needed by other chesspiece classes.
    """

    def __init__(self, position: tuple):
        self.position: tuple = position

    def get_position(self):
        return self.position

    def set_position(self, position: tuple):
        self.position = position

    def get_info(self):
        return self.info

    def set_moved(self):
        self.info["moved"] = True

    def check_move(self, t_tile: tuple,
                   board_state: list, p_color: str) -> bool:
        """Checks if the chess move the player attemps is legal or not.

        t_tile : target tile
        board_state: chessboard list
        p_color: player color
        """

        if p_color == self.get_info()['color']:
            viable_moves = self._get_moves(board_state)
            print(f"viable moves: {viable_moves}")
            if t_tile in viable_moves:
                if not self.get_info()['moved']:
                    self.set_moved()
                if board_state[t_tile[0]][t_tile[1]] is None:
                    return True
                else:
                    if board_state[t_tile[0]][t_tile[1]].get_info()['type'] != "king":
                        self.set_position(t_tile)
                        return True
                    else:
                        print("A King can only check mated - not eaten")
                        return False
            else:
                return False
        else:
            print(f"Cannot move pieces not belonging own color")
            return False
        
    def _rook_bishop_queen_move_check(self, board_state: list):
        """Combined move checking for rook, bishop and queen. Between
        the pieces only the allowed tile movement differs, the logic for
        checking viable moves is same.
        """        
        row, col = self.get_position()
        viable_moves = []
        
        for row2, col2 in self.TILE_MOVEMENTS:
            trgt_row, trgt_col = row + row2, col + col2
            while 0 <= trgt_row < 8 and 0 <= trgt_col < 8:
                if board_state[trgt_row][trgt_col] is None:
                    viable_moves.append((trgt_row, trgt_col))
                else:
                    if board_state[trgt_row][trgt_col].get_info()['color'] \
                            != self.get_info()['color']:
                        viable_moves.append((trgt_row, trgt_col))
                    break
                trgt_row += row2
                trgt_col += col2
        return viable_moves
            


class Pawn(Piece):

    def __init__(self, position: tuple, color: str):
        super().__init__(position=position)
        self.info = {"type": "pawn", "color": color,
                     "symbol": "P", "moved": False, "en_passant": False}
        self.TILE_MOVEMENTS_WHITE = [(1, 0)]
        self.TILE_MOVEMENTS_BLACK = [(-1, 0)]
        self.WHITE_attack = [(1, 1), (1, -1)]
        self.BLACK_atttack = [(-1, -1), (-1, 1)]

    def white_or_black_movement(self):
        return self.TILE_MOVEMENTS_WHITE \
            if self.get_info()['color'] == "W" else self.TILE_MOVEMENTS_BLACK

    def white_or_black_attack(self):
        return self.WHITE_attack \
            if self.get_info()['color'] == "W" else self.BLACK_atttack

    def initial_movement(self):
        return [(2, 0)] if self.get_info()['color'] == "W" else [(-2, 0)]

    def _can_en_passant(self):
        """To be implemented
        """
        pass

    def _get_moves(self, board_state: list) -> list:
        """Pawn movement, regular and attack pattern with initial 2 step move.
        """

        row, col = self.get_position()
        viable_moves = []
        moveset = copy.copy(self.white_or_black_movement())
        # check if piece has moved or not, if not append the moveset list
        if not self.get_info()['moved']:
            moveset.extend(self.initial_movement())
        # pawn regular movement
        for row2, col2 in moveset:
            trgt_row, trgt_col = row + row2, col + col2
            if 0 <= trgt_row < 8 and 0 <= trgt_col < 8:
                if board_state[trgt_row][trgt_col] is None:
                    viable_moves.append((trgt_row, trgt_col))
                else:
                    break
        # pawn piece capturing
        for row3, col3 in self.white_or_black_attack():
            trgt_row2, trgt_col2 = row + row3, col + col3
            if 0 <= trgt_row2 < 8 and 0 <= trgt_col2 < 8:
                if board_state[trgt_row2][trgt_col2] is not None:
                    if board_state[trgt_row2][trgt_col2].get_info()['color'] \
                            != self.get_info()['color']:
                        viable_moves.append((trgt_row2, trgt_col2))
        return viable_moves


class Bishop(Piece):

    def __init__(self, position: tuple, color: str):
        super().__init__(position=position)
        self.info = {"type": "bishop", "color": color,
                     "symbol": "B", "moved": False}
        self.TILE_MOVEMENTS = [(-1, 1), (1, 1), (-1, -1), (1, -1)]

    def _get_moves(self, board_state: list) -> list:
        return self._rook_bishop_queen_move_check(board_state)


class Knight(Piece):

    def __init__(self, position: tuple, color: str):
        super().__init__(position=position)
        self.info = {"type": "knight", "color": color,
                     "symbol": "N", "moved": False}
        self.TILE_MOVEMENTS = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                               (-2, 1), (-1, 2), (1, 2), (2, 1)]

    def _get_moves(self, board_state: list) -> list:

        row, col = self.get_position()
        viable_moves = []

        for row2, col2 in self.TILE_MOVEMENTS:
            trgt_row, trgt_col = row + row2, col + col2
            if 0 <= trgt_row < 8 and 0 <= trgt_col < 8:
                if board_state[trgt_row][trgt_col] is None:
                    viable_moves.append((trgt_row, trgt_col))
                else:
                    if board_state[trgt_row][trgt_col].get_info()['color'] \
                            != self.get_info()['color']:
                        viable_moves.append((trgt_row, trgt_col))
        return viable_moves


class Rook(Piece):

    def __init__(self, position: tuple, color: str):
        super().__init__(position=position)
        self.info = {"type": "rook", "color": color,
                     "symbol": "R", "moved": False}
        self.TILE_MOVEMENTS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def _get_moves(self, board_state: list) -> list:
        return self._rook_bishop_queen_move_check(board_state)


class Queen(Piece):

    def __init__(self, position: tuple, color: str):
        super().__init__(position=position)
        self.info = {"type": "queen", "color": color,
                     "symbol": "Q", "moved": False}
        self.TILE_MOVEMENTS = [(-1, 1), (1, 1), (-1, -1), (1, -1),
                               (-1, 0), (0, 1), (1, 0), (0, -1)]

    def _get_moves(self, board_state: list) -> list:
        return self._rook_bishop_queen_move_check(board_state)


class King(Piece):
    """Class for King chess piece. Contains also methods for
    temporary chessboard for move viability checking, and
    methods for checking if king is check or checkmated.
    """

    def __init__(self, position: tuple, color: str):
        super().__init__(position=position)
        self.info = {"type": "king", "color": color,
                     "symbol": "K", "moved": False}
        self.TILE_MOVEMENTS = [(-1, 1), (1, 1), (-1, -1), (-1, 1),
                               (-1, 0), (0, 1), (1, 0), (0, -1)]
        self.check = False

    def temporary_board(self, start_position,
                        target_position, board_state) -> list[list]:

        temporary = [copy.deepcopy(row) for row in board_state]
        chesspiece = temporary[start_position[0]][start_position[1]]
        temporary[target_position[0]][target_position[1]] = chesspiece
        temporary[start_position[0]][start_position[1]] = None

        return temporary

    def _can_tower(self, board_state: list):
        """To be implemented
        """
        pass

    def _get_moves(self, board_state: list) -> list:

        row, col = self.get_position()
        viable_moves = []
        row_king, col_king = self.other_king_location(board_state)

        for row2, col2 in self.TILE_MOVEMENTS:
            trgt_row, trgt_col = row + row2, col + col2
            if 0 <= trgt_row < 8 and 0 <= trgt_col < 8:
                if abs(trgt_row - row_king) <= 1 and abs(trgt_col - col_king) <= 1:
                    continue
                if board_state[trgt_row][trgt_col] is None:
                    viable_moves.append((trgt_row, trgt_col))
                else:
                    if board_state[trgt_row][trgt_col].get_info()['color'] \
                            != self.get_info()['color']:
                        viable_moves.append((trgt_row, trgt_col))
                        break

        return viable_moves

    def other_king_location(self, board_state):
        """Gets the location of the opposing color's king
        """
        other_king = None

        for row in range(0, 8):
            for col in range(0, 8):
                chesspiece = board_state[row][col]
                if chesspiece is not None:
                    if chesspiece.get_info()['type'] == "king" \
                            and chesspiece.get_info()['color'] != self.get_info()['color']:
                        other_king = chesspiece
                        break

        return other_king.get_position()

    def is_checked(self, board_state: list) -> bool:
        """Checks if the king is threatened by opposing color pieces
        """
        king_location = self.get_position()

        for row2 in range(0, 8):
            for col2 in range(0, 8):
                chesspiece = board_state[row2][col2]
                if chesspiece is not None:
                    if chesspiece.get_info()['color'] != self.get_info()['color']:
                        if king_location in chesspiece._get_moves(board_state):
                            self.check = True
                            return True

        self.check = False
        return False

    def is_checkmate(self, board_state: list) -> bool:
        """Checks if the king is checkmated. First checks
        if king can move and then if other pieces can
        help the king.
        """
        king_moves = self._get_moves(board_state)

        for move in king_moves:
            temporary_board = self.temporary_board(
                self.get_position(), move, board_state)
            if not temporary_board[move[0]][move[1]]:
                return False

        for row in range(0, 8):
            for col in range(0, 8):
                chesspiece = board_state[row][col]
                if chesspiece is not None:
                    if chesspiece.get_info()['color'] == self.get_info()['color']:
                        viable_moves = chesspiece._get_moves(board_state)
                        for move in viable_moves:
                            temporary_board = self.temporary_board(
                                self.get_position(), move, board_state)
                            if not self.is_checked(temporary_board):
                                return False
        return True

    def is_stalemate(self, board_state: list) -> bool:
        """Checks if the game is a stalemate, i.e, the king cannot move
        but is not in check and other pieces cannot be moved either
        """
        if self.is_checked(board_state):
            return False

        if self._get_moves(board_state):
            return False

        for row in range(0, 8):
            for col in range(0, 8):
                chesspiece = board_state[row][col]
                if chesspiece is not None:
                    if chesspiece.get_info()['color'] == self.get_info()['color']:
                        if chesspiece._get_moves(board_state):
                            return False

        return True

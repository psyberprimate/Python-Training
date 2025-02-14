import pieces
from typing import Tuple, Any


class ChessBoard():

    def __init__(self):
        self.x = 8
        self.y = 8
        self.state = []
        self.move: int = 1
        self.board_state = None
        self.initial_state = {"6_0": {"type": pieces.Pawn, "color": "B"},
                              "6_1": {"type": pieces.Pawn, "color": "B"},
                              "6_2": {"type": pieces.Pawn, "color": "B"},
                              "6_3": {"type": pieces.Pawn, "color": "B"},
                              "6_4": {"type": pieces.Pawn, "color": "B"},
                              "6_5": {"type": pieces.Pawn, "color": "B"},
                              "6_6": {"type": pieces.Pawn, "color": "B"},
                              "6_7": {"type": pieces.Pawn, "color": "B"},
                              "7_0": {"type": pieces.Rook, "color": "B"},
                              "7_1": {"type": pieces.Knight, "color": "B"},
                              "7_2": {"type": pieces.Bishop, "color": "B"},
                              "7_3": {"type": pieces.Queen, "color": "B"},
                              "7_4": {"type": pieces.King, "color": "B"},
                              "7_5": {"type": pieces.Bishop, "color": "B"},
                              "7_6": {"type": pieces.Knight, "color": "B"},
                              "7_7": {"type": pieces.Rook, "color": "B"},
                              "0_0": {"type": pieces.Rook, "color": "W"},
                              "0_1": {"type": pieces.Knight, "color": "W"},
                              "0_2": {"type": pieces.Bishop, "color": "W"},
                              "0_3": {"type": pieces.Queen, "color": "W"},
                              "0_4": {"type": pieces.King, "color": "W"},
                              "0_5": {"type": pieces.Bishop, "color": "W"},
                              "0_6": {"type": pieces.Knight, "color": "W"},
                              "0_7": {"type": pieces.Rook, "color": "W"},
                              "1_0": {"type": pieces.Pawn, "color": "W"},
                              "1_1": {"type": pieces.Pawn, "color": "W"},
                              "1_2": {"type": pieces.Pawn, "color": "W"},
                              "1_3": {"type": pieces.Pawn, "color": "W"},
                              "1_4": {"type": pieces.Pawn, "color": "W"},
                              "1_5": {"type": pieces.Pawn, "color": "W"},
                              "1_6": {"type": pieces.Pawn, "color": "W"},
                              "1_7": {"type": pieces.Pawn, "color": "W"},
                              }

    def make_board(self):
        """Makes the "board" for the pieces as 2-d list
        """
        self.state = [[self.assemble_pieces((y, x))
                       for x in range(self.x)] for y in range(self.y)]

    def get_pieces(self) -> Tuple[list, list]:
        """Get the pieces each player has
        """
        white_list = []
        black_list = []
        for j in range(self.y-1, -1, -1):
            for i in range(0, self.x):
                if self.state[j][i] is not None:
                    tile = self.state[j][i].get_info()
                    if tile["color"] == "W":
                        white_list.append(tile)
                    else:
                        black_list.append(tile)
        return white_list, black_list

    def assemble_pieces(self, y_x: tuple):
        """Check piece type based on location and whether
        there is a piece in the board tile at start
        """
        comparison_key = "_".join((str(y_x[0]), str(y_x[1])))
        piece = self.initial_state[comparison_key] \
            if comparison_key in self.initial_state.keys() else None
        if piece:
            return piece["type"](position=(y_x[0], y_x[1]), color=piece["color"])
        else:
            return None

    def update_board(self, board_state: object, origin_index: tuple, target_index: tuple) -> Tuple[list, Any]:
        updated_piece = board_state[origin_index[0]][origin_index[1]]
        removed_piece = board_state[target_index[0]][target_index[1]]
        if removed_piece is not None:
            removed_info = removed_piece.get_info()
        else:
            removed_info = None
        board_state[origin_index[0]][origin_index[1]] = None
        board_state[target_index[0]][target_index[1]] = updated_piece
        return board_state, removed_info

    def print_board(self):
        self.print_line("SIMPLE CHESS", " ", "-", 39)
        self.print_line(f"Move: {self.move}", " ", ".", 39)
        self.print_line("FIGHT", " ", ".", 39)
        print()
        print("---  a   b   c   d   e   f   g   h  ---")
        for j in range(self.y-1, -1, -1):
            print(f"{j+1} |", end=" ")
            for i in range(0, self.x):
                piece = self.state[j][i]
                if piece is None:
                    print(" o ", end=" ")
                else:
                    print(
                        f"{self.state[j][i].get_symbol()}_{self.state[j][i].get_color().lower()}", end=" ")
            print(f"| {j+1}")
        print("---------------------------------------")
        print("  |  a   b   c   d   e   f   g   h  | ")
        
    def print_game_status(self):
        pass

    @staticmethod
    def print_line(title: str, sepator: str,
                   fill_char: str, txt_lenght: str = 40):
        """ Prints a line of text based on user input
        """
        def see_if_rounded(txt_lenght):
            return round(number=txt_lenght, ndigits=None) < txt_lenght or \
                round(number=txt_lenght, ndigits=None) > txt_lenght

        txt_lenght = txt_lenght
        txt_lenght -= len(title)
        odd = see_if_rounded(txt_lenght/2)
        txt_lenght = txt_lenght // 2
        base_str = ""
        if len(title) > 0:
            for _ in range(1, txt_lenght):
                base_str += fill_char
            title = sepator.join([base_str, title])
            title = sepator.join([title, base_str])
            title += fill_char if odd else ''
        else:
            title = f''.join(f'{fill_char}'*txt_lenght*2)
        print(title)


if __name__ == "__main__":
    chessboard = ChessBoard()
    chessboard.make_board()
    chessboard.print_board()

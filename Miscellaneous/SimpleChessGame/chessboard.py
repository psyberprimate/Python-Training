import pieces
from typing import Tuple, Any
import json
import os

class ChessBoard():

    def __init__(self, chesspieces):
        self.x = 8
        self.y = 8
        self.state = []
        self.move: int = 1
        self.white_king: tuple = None
        self.black_king: tuple = None
        self.initial_state = chesspieces
        
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
            if piece["type"] == pieces.King:
                if piece["color"] == "W":
                    self.white_king = y_x[0], y_x[1]
                else:
                    self.black_king = y_x[0], y_x[1]
            return piece["type"](position=(y_x[0], y_x[1]), color=piece["color"])
        else:
            return None

    def update_board(self, origin_index: tuple, target_index: tuple) -> Tuple[list, Any]:
        """Updates the board with new piece locations
        """        
        updated_piece = self.state[origin_index[0]][origin_index[1]]
        removed_piece = self.state[target_index[0]][target_index[1]]
        if removed_piece is not None:
            removed_info = removed_piece.get_info()
        else:
            removed_info = None
        self.state[origin_index[0]][origin_index[1]] = None
        self.state[target_index[0]][target_index[1]] = updated_piece
        self.state[target_index[0]][target_index[1]].set_position(target_index)
        print(f"updated piece information: {updated_piece.get_info()}")
        if self.state[target_index[0]][target_index[1]].get_type() == "king":
            if self.state[target_index[0]][target_index[1]].get_color() == "W":
                self.white_king = self.state[target_index[0]][target_index[1]].get_position()
            else:
                self.black_king = self.state[target_index[0]][target_index[1]].get_position()
        return removed_info

    def check_board_state(self):

        game_over = False

        if self.state[self.white_king[0]][self.white_king[1]].is_checked(self.state):
            print("White king is in check!")
            print("Protect the king")
            if self.state[self.white_king[0]][self.white_king[1]].is_checkmate(self.state):
                print("Checkmate! Black player wins!")
                game_over = True
        if self.state[self.black_king[0]][self.black_king[1]].is_checked(self.state):
            print("Black king is in check!")
            print("Protect the king")
            if self.state[self.black_king[0]][self.black_king[1]].is_checkmate(self.state):
                print("Checkmate! White player wins!")
                game_over = True

        if self.state[self.white_king[0]][self.white_king[1]].is_stalemate(self.state):
            print("Statemate! White player cannot move!")
            game_over = True

        if self.state[self.black_king[0]][self.black_king[1]].is_stalemate(self.state):
            print("Statemate! Black player cannot move!")
            game_over = True

        return game_over

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
    path = "/Miscellaneous/SimpleChessGame/pieces.json"
    complete_path = os.path.join(os.getcwd()+os.path.normpath(path))
    with open(complete_path, 'w') as file:
        #chessboard.initial_state
        json.dump(chessboard.initial_state.to_dict(), file)

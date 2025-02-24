import pieces
from typing import Tuple, Any
import chesspiece


class ChessBoard():

    def __init__(self, chesspieces):
        self.x = 8
        self.y = 8
        self.state = []
        self.move: int = 1
        self.w_king: tuple = None
        self.b_king: tuple = None
        self.initial_state = chesspieces

    def make_board(self):
        """Makes the "board" for the pieces as 2-d list by
        calling assemble_pieces(). The rows are represented by
        y and columns by x. The list of chess pieces and None
        values representing empty board slots gets saved in self.state
        """
        self.state = [[self.assemble_pieces((y, x))
                       for x in range(self.x)] for y in range(self.y)]

    def get_pieces(self) -> Tuple[list, list]:
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
        """Returns the chesspiece object initialized or None 
        """
        comparison_key = "_".join((str(y_x[0]), str(y_x[1])))
        piece = self.initial_state.get(comparison_key)
        if piece:
            if piece["type"] == pieces.King:
                if piece["color"] == "W":
                    self.w_king = y_x[0], y_x[1]
                else:
                    self.b_king = y_x[0], y_x[1]
            return piece["type"](position=(y_x[0], y_x[1]), color=piece["color"])
        else:
            return None

    def update_board(self, origin: tuple, target: tuple) -> Tuple[list, Any]:
        """Updates the board with new piece locations,
        keep track of position of both kings. Also, checks
        if castling can be done. 

        Returns: None or dictionary of chesspiece info
        """
        updated_piece = self.state[origin[0]][origin[1]]
        removed_piece = self.state[target[0]][target[1]]

        if removed_piece is not None:
            removed_info = removed_piece.get_info()
        else:
            removed_info = None

        self.state[origin[0]][origin[1]] = None
        self.state[target[0]][target[1]] = updated_piece
        self.state[target[0]][target[1]].set_position(target)

        if self.state[target[0]][target[1]].get_info()['type'] == "king":
            if self.state[target[0]][target[1]].get_info()['color'] == "W":
                self.w_king = self.state[target[0]][target[1]].get_position()
            else:
                self.b_king = self.state[target[0]][target[1]].get_position()

        # check for castlings
        if self.state[target[0]][target[1]].get_info()["type"] == "king":
            if self.state[target[0]][target[1]].get_info()["castle"]:
                if target[1] < 3:
                    rook_to_update = self.state[target[0]][target[1]-2]
                    self.state[target[0]][target[1]-2] = None
                    self.state[target[0]][target[1]+1] = rook_to_update
                else:
                    rook_to_update = self.state[target[0]][target[1]+1]
                    self.state[target[0]][target[1]+1] = None
                    self.state[target[0]][target[1]-1] = rook_to_update

                rook_to_update.set_moved()
                self.state[target[0]][target[1]].set_castle_off()
                rook_info = rook_to_update.get_info()
                king = self.state[target[0]][target[1]]
                king_info = king.get_info()
                print(f"Castling with: {king_info['type']} at", end=" ")
                print(
                    f"{king.to_chess_format(king_info["position"])}", end=" ")
                print(f"with {rook_info['type']} at", end=" ")

        info = updated_piece.get_info()

        print(
            f"Move: {info['type']} to {updated_piece.to_chess_format(info["position"])}")

        return removed_info

    def check_board_state(self):
        """For checking the game state. Sees if the king are checked by
        calling is_checked(), and if they are, then sees if there are
        any moves left to defend the king by calling is_checkmate().
        Also sees if the kings are in stalemate, i. e they cannot move
        but are not under threat or other pieces cannot move.

        Returns:
            True or False based on boolean
        """
        game_over = False

        if self.state[self.w_king[0]][self.w_king[1]].is_checked(self.state):
            print("White king is in check!")
            print("Protect the king")
            if self.state[self.w_king[0]][self.w_king[1]].is_checkmate(self.state):
                print("Checkmate! Black player wins!")
                game_over = True

        if self.state[self.b_king[0]][self.b_king[1]].is_checked(self.state):
            print("Black king is in check!")
            print("Protect the king")
            if self.state[self.b_king[0]][self.b_king[1]].is_checkmate(self.state):
                print("Checkmate! White player wins!")
                game_over = True

        if self.state[self.w_king[0]][self.w_king[1]].is_stalemate(self.state):
            print("Statemate! White player cannot move!")
            game_over = True

        if self.state[self.b_king[0]][self.b_king[1]].is_stalemate(self.state):
            print("Statemate! Black player cannot move!")
            game_over = True

        return game_over

    def print_board(self):
        """Simple function to print the chessboard.
        Iterates over the board.state 2d list which
        contains the chesspieces
        """
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
                    symbol = self.state[j][i].get_info()['symbol']
                    color = self.state[j][i].get_info()['color'].lower()
                    print(f"{symbol}_{color}", end=" ")
            print(f"| {j+1}")
        print("---------------------------------------")
        print("  |  a   b   c   d   e   f   g   h  | ")

    def print_game_status(self):
        pass

    @staticmethod
    def print_line(title: str, sepator: str,
                   fill_char: str, txt_lenght: str = 40):
        """ Prints a line of text based on user input

         title is title of the text.
         seperator: str (separates the space between 
         the text and filler letters).
         fill_char: str (fills the empty parts of str lenght).
         txt_lenght (lenght of the text)

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
    chessboard = ChessBoard(chesspiece.chesspieces_dummy)
    chessboard.make_board()
    chessboard.print_board()

    p_color = "W"
    p_piece = chessboard.state[chessboard.w_king[0]][chessboard.w_king[1]].get_info()['position']
    t_tile = (0, 2)
    if chessboard.state[chessboard.w_king[0]][chessboard.w_king[1]].check_move(t_tile, chessboard.state, p_color):
        print("Castling possible for white")
        chessboard.update_board(p_piece, t_tile)
    else:
        print("Castling cannot be done for white")

    p_piece = chessboard.state[chessboard.b_king[0]][chessboard.b_king[1]].get_info()['position']
    t_tile = (7, 6)
    if chessboard.state[chessboard.b_king[0]][chessboard.b_king[1]].check_move(t_tile, chessboard.state, "B"):
        print("Castling possible for black")
        chessboard.update_board(p_piece, t_tile)
    else:
        print("Castling cannot be done for black")

    chessboard.print_board()

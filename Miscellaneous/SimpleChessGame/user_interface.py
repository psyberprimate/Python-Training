import chessboard
import chesspiece

class UserInterface():

    MENU_MESSAGE = """1) Play chess.\n2) Get chess moves from previous game.\n3) Exit.
\nYour input: """

    def __init__(self):
        self.OPTIONS = {"1": self.play_chess,
                        "2": self.get_moves,
                        }

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

    def play_chess(self):

        board = chessboard.ChessBoard(chesspiece.chesspieces)
        board.make_board()
        turn_white = True
        white_player_pieces, black_player_pieces = board.get_pieces()

        while (True):
            board.print_board()
            if board.check_board_state():
                UserInterface.print_line("Game well played!", "@", "#", 39)
                break

            if turn_white:
                print(
                    "White Player. Enter your move, for example: A2 to A3. To quit write 'quit'")
                player_input = input("Starting tile, End tile: ")
            else:
                print(
                    "Black Player. Enter your move, for example: A2 to A3. To quit write 'quit'")
                player_input = input("Starting tile, End tile: ")
            if player_input.lower() == "quit":
                break
            try:
                chosen_piece, target_tile = UserInterface.parse_input(
                    player_input)
            except (IndexError, ValueError) as errors:
                print(errors)
                print(
                    "Incorrect input: Please provide commands in format: B1 to C4 (column/row)")
            else:
                player_color = "W" if turn_white else "B"
                print(chosen_piece)
                print(target_tile)
                if board.state[chosen_piece[0]][chosen_piece[1]] is not None:
                    # print(board.state[chosen_piece[0]][chosen_piece[1]].get_info())
                    # print(board.state[chosen_piece[0]]
                    #       [chosen_piece[1]].get_position())
                    if board.state[chosen_piece[0]][chosen_piece[1]].check_move(target_tile, board.state, player_color):
                        removed_piece_info = board.update_board(
                            chosen_piece, target_tile)
                        print(
                            f"Moving {board.state[target_tile[0]][target_tile[1]].get_type()}", end="")
                        print(f"to {target_tile}")
                        if removed_piece_info is not None:
                            if turn_white:
                                black_player_pieces.remove(removed_piece_info)
                                print(
                                    f"Black player loses: {removed_piece_info['type']}")
                            else:
                                white_player_pieces.remove(removed_piece_info)
                                print(
                                    f"White player loses: {removed_piece_info['type']}")
                        turn_white = not turn_white
                        board.move += 1
                    else:
                        print(
                            f"Cannot move {board.state[chosen_piece[0]][chosen_piece[1]].get_type()}", end="")
                        print(f"to {target_tile}")
                else:
                    print(f"Board index is empty - Nothing to move")
        UserInterface.print_line("Back to menu", ' ', '-', 39)

    @staticmethod
    def parse_input(input: str) -> tuple[tuple]:

        split_str = input.split()
        piece = split_str[0]
        destination = split_str[2]
        start_column = None
        start_row = int(piece[1])-1
        end_column = None
        end_row = int(destination[1])-1
        # match piece  and destination letters
        match piece[0].lower():
            case "a":
                start_column = 0
            case "b":
                start_column = 1
            case "c":
                start_column = 2
            case "d":
                start_column = 3
            case "e":
                start_column = 4
            case "f":
                start_column = 5
            case "g":
                start_column = 6
            case "h":
                start_column = 7
            case _:
                start_column = None

        match destination[0].lower():
            case "a":
                end_column = 0
            case "b":
                end_column = 1
            case "c":
                end_column = 2
            case "d":
                end_column = 3
            case "e":
                end_column = 4
            case "f":
                end_column = 5
            case "g":
                end_column = 6
            case "h":
                end_column = 7
            case _:
                end_column = None

        return ((start_row, start_column), (end_row, end_column))

    def get_moves(self):
        print("To be implemented")

    def program_flow(self):
        UserInterface.print_line("Welcome to Simple Chess!", " ", "*", 39)
        while (option := input(UserInterface.MENU_MESSAGE)) != "3":
            try:
                self.OPTIONS[option]()
            except KeyError:
                print("Please select between 1-3.")
        UserInterface.print_line("Goodbye", " ", "#", 39)


if __name__ == "__main__":
    pass

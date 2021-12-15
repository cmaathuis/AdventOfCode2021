#!/usr/bin/python3

BOARD_SIZE = 5


class Board:
    def __init__(self, board_values: str):
        self.board_values = board_values
        self.rows = []
        self.has_won = False
        self._populate_board()

    def _populate_board(self):
        self.rows = [[[int(y), False] for y in x.split()] for x in self.board_values.split("\n")]

    def check_rows(self):
        for row in self.rows:
            win = True
            for value in row:
                if value[1] == False:
                    break
            if win:
                return win
        return win

    def check_columns(self):
        for i in range(len(self.rows)):
            win = True
            for row in self.rows:
                win = row[i][1]
                if not win:
                    break
            if win:
                break
        self.has_won = win  # should return

    def check_diagonals(self):
        pass

    def check_for_win(self):
        self.check_rows()
        self.check_columns()
        self.check_diagonals()  # should return

    def mark_board(self, number: int):
        # print("Marking number: ", number)
        for row in self.rows:
            for value in row:
                if value[0] == number:
                    value[1] = True
        self.check_for_win()

    def sum_unmarked_values(self):
        sum = 0
        for row in self.rows:
            for value in row:
                if not value[1]:
                    sum += value[0]
        return sum

    def __str__(self):
        board_string = "___RESULTS_2D_ARRAY____\n"
        board_string += str(self.rows)
        board_string += "\n ______________________\n"
        board_string += "\n __________board#____________\n,"
        return board_string


def mark_boards(boards: Board, card: int):
    for board in boards:
        board.mark_board(card)
        if board.has_won:
            return board
    return None


def calc_winning_board(board: Board, card: int):
    sum = board.sum_unmarked_values()
    print(card * sum)


def format_input(input_text: str):
    boards = []
    puzzle_input = input_text.split("\n\n")
    cards = [int(x) for x in puzzle_input[0].split(",")]
    puzzle_input = puzzle_input[1:]
    for i in range(len(puzzle_input)):
        boards.append(Board(puzzle_input[i]))
    return (boards, cards)


def day4(input_text: str):
    game_input = format_input(input_text)
    board = None
    last_card = 0
    for card in game_input[1]:
        board = mark_boards(game_input[0], card)
        if board != None:
            break
        last_card = card
    if board == None:
        print("No winner!")
    else:
        calc_winning_board(board, last_card)

#!/usr/bin/python3

BOARD_SIZE = 5


class Board:
    def __init__(self, board_values: str):
        self.board_values = board_values
        self.rows = []
        self._populate_board()

    def _populate_board(self):
        self.rows = [[[int(y), False] for y in x.split()] for x in self.board_values.split("\n")]

    def check_rows(self):
        for row in self.rows:
            win = True
            for value in row:
                win = value[1]
                if not win:
                    break
            if win:
                return win
        return win

    def check_columns(self):
        for i in range(len(self.rows[0])):
            win = True
            for row in self.rows:
                win = row[i][1]
                if not win:
                    break
            if win:
                break
        return win  # should return

    def check_diagonals(self):
        pass

    def check_for_win(self):
        return self.check_rows() or self.check_columns()

    def mark_board(self, number: int):
        # print("Marking number: ", number)
        for row in self.rows:
            for value in row:
                if value[0] == number:
                    value[1] = True
        return self.check_for_win()

    def sum_unmarked_values(self):
        sum = 0
        for row in self.rows:
            for value in row:
                if not value[1]:
                    sum += value[0]
        return sum

    def __str__(self):
        board_string = "___RESULTS_2D_ARRAY____\n"
        for row in self.rows:
            board_string += f"{row}\n"
        board_string += "\n ______________________\n"
        board_string += "\n __________board#____________\n,"
        return board_string


def mark_boards(boards, card: int):
    # print(boards[0])
    winning_boards = []
    boards_to_discard = []
    for i, board in enumerate(boards):
        has_won = board.mark_board(card)
        if has_won:
            boards_to_discard.append(i)
            winning_sum = board.sum_unmarked_values()
            winning_boards.append((winning_sum, card))
    for discard in reversed(boards_to_discard):
        boards.pop(discard)
    return winning_boards


def calc_winning_board(winning_pair) -> int:
    print(f"Card: {winning_pair[1]}, Sum: {winning_pair[0]}")
    return winning_pair[1] * winning_pair[0]


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
    winning_boards = []
    for card in game_input[1]:
        new_marked_boards = mark_boards(game_input[0], card)
        if new_marked_boards:
            winning_boards += new_marked_boards
    if winning_boards == None:
        print("No winner!")
    else:
        first_win = calc_winning_board(winning_boards[0])
        last_win = calc_winning_board(winning_boards[-1])
        print(f"Value of the first winning board {first_win}")
        print(f"Value of the last winning board {last_win}")

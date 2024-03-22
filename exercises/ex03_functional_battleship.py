"""EX03 - Functional Battleship."""

__author__ = "730654117"
import random


def input_guess(grid_size: int, guess_type: str) -> int:
    """Returns user's row or column guess."""
    assert guess_type == "row" or guess_type == "column"
    # ask for guess and prompt them to try again if outside grid
    if guess_type == "row":
        row_guess: str = input("Guess a row: ")
        while int(row_guess) > grid_size or int(row_guess) < 1:
            row_guess = str(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        return int(row_guess)
    else:
        column_guess: str = input("Guess a column: ")
        while int(column_guess) > grid_size or int(column_guess) < 1:
            column_guess = str(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        return int(column_guess)


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct: bool) -> None:
    """Prints emoji grid with user's guess."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    # result box is red if correct and white if incorrect
    if correct is True:
        result_box = str(RED_BOX)
    else:
        result_box = str(WHITE_BOX)
    # add blue boxes (and result box) in row string until end of grid, print rows
    row_idx: int = 1
    while row_idx <= grid_size:
        row_string: str = str(" ")
        column_idx: int = 1
        if int(row_guess) == row_idx:
            while column_idx <= grid_size:
                if int(column_guess) == column_idx:
                    row_string += result_box
                else: 
                    row_string += BLUE_BOX
                column_idx += 1
        else:
            while column_idx <= grid_size:
                row_string += BLUE_BOX
                column_idx += 1
        print(row_string)
        row_idx += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Returns guess result(T/F)."""
    if row_guess == secret_row and column_guess == secret_column:
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Brings functions together to run the game."""
    turn_idx: int = 1
    correct: bool = False
    # tracks turns left, prints grid, gives result
    while turn_idx <= 5 and correct is False:
        print(f"=== Turn {turn_idx}/5 ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        if correct_guess(secret_row, secret_column, row_guess, column_guess):
            correct = True
            print_grid(grid_size, row_guess, column_guess, correct)
            print(f"Hit! You won in {turn_idx}/5 turns!")
        else:
            print_grid(grid_size, row_guess, column_guess, correct)
            print("Miss!")
            turn_idx += 1
    if turn_idx > 5:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))

        
"""EX02 - One Shot Battleship."""

__author__ = "730654117"
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
# ask user for input and prompt them to try again if outside grid
row_guess: str = input("Guess a row: ")
while int(row_guess) > grid_size or int(row_guess) < 1:
    row_guess = str(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
column_guess: str = input("Guess a column: ")
while int(column_guess) > grid_size or int(column_guess) < 1:
    column_guess = str(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
# result box is red if correct and white if incorrect
if int(column_guess) == secret_column and int(row_guess) == secret_row:
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
# evaluate corectness of guess, give hint if only row guess or column is correct
if int(column_guess) == secret_column and int(row_guess) == secret_row:
    print("Hit!")
elif int(row_guess) != secret_row and int(column_guess) != secret_column:
    print("Miss!")
elif int(row_guess) == secret_row and int(column_guess) != secret_column:
    print("Close! Correct row, wrong column.")
elif int(row_guess) != secret_row and int(column_guess) == secret_column:
    print("Close! Correct column, wrong row.")
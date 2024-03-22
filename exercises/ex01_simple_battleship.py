"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730654117"
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
player_1_input: str = input("Pick a secret boat location between 1 and 4: ")
boat_location: int = int(player_1_input)
if boat_location > 4:
    print(f"Error! {boat_location} too high!")
    quit()
if boat_location < 1:
    print(f"Error! {boat_location} too low!")
    quit()
player_2_input: str = input("Guess a number between 1 and 4: ")
location_guess: int = int(player_2_input)
if location_guess > 4:
    print(f"Error! {location_guess} too high!")
    quit()
if location_guess < 1:
    print(f"Error! {location_guess} too low!")
    quit()
if location_guess == 1 and location_guess != boat_location:
    print(f"{WHITE_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
if location_guess == 1 and location_guess == boat_location: 
    print(f"{RED_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
if location_guess == 2 and location_guess != boat_location:
    print(f"{BLUE_BOX}{WHITE_BOX}{BLUE_BOX}{BLUE_BOX}")
if location_guess == 2 and location_guess == boat_location: 
    print(f"{BLUE_BOX}{RED_BOX}{BLUE_BOX}{BLUE_BOX}")
if location_guess == 3 and location_guess != boat_location:
    print(f"{BLUE_BOX}{BLUE_BOX}{WHITE_BOX}{BLUE_BOX}")
if location_guess == 3 and location_guess == boat_location:
    print(f"{BLUE_BOX}{BLUE_BOX}{RED_BOX}{BLUE_BOX}")
if location_guess == 4 and location_guess != boat_location:
    print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{WHITE_BOX}")
if location_guess == 4 and location_guess == boat_location:
    print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{RED_BOX}")
if boat_location == location_guess:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")
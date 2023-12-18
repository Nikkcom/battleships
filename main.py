from screen.coordinates import print_grid, generate_machine_ships
import os
from time import *

empty = " "
hit = "x"
ship = "#"

ship_list = []

ship_coords = []

player_coords_dict = {}


def generate_cords_dictionary():
    for i in range(9):

        for x in range(9):
            co = (i + 1, x + 1)

            player_coords_dict[co] = empty


def user_input_coordinates():
    message = ""
    while True:
        os.system('cls||clear')

        # display grid
        print_grid(player_coords_dict)

        # print prompt
        print(message)
        message = ""
        print("Please enter your desired coordinate")

        user_input = input("")
        user_input = user_input.upper()

        if len(user_input) == 2:
            input_split = [x for x in user_input]
            print(input_split)
            char_input = input_split[0]
            try:
                int_input = int(input_split[1])
            except ValueError:
                message = "Write a valid coordinate please"
                continue

            if not 0 < int_input <= 9:
                continue

            if ord("A") <= ord(char_input) <= ord("I"):
                user_coord = (ord(char_input) - 64, int_input)
                print(user_coord)

                if player_coords_dict[user_coord] == hit or player_coords_dict[user_coord] == ship:
                    message = "This coordinate are already attacked"
                    continue
                elif user_coord in ship_coords:
                    player_coords_dict[user_coord] = ship
                    continue
                else:
                    player_coords_dict[user_coord] = hit
                    continue


def run():

    # Generates the list of coordinates with the character that presents an empty grid slot.
    generate_cords_dictionary()

    # Creates a list of ship objects that got a location on the grid.
    global ship_list
    ship_list = generate_machine_ships()

    print(ship_list)
    for i in ship_list:
        print(i)
        coords = i.get_coords()

        for coord in coords:
            player_coords_dict[coord] = i.char


    # Asks user for coordinate for an attack maybe?
    user_input_coordinates()


if __name__ == "__main__":
    run()

from ship import Ship


def print_grid(coord_list):
    print("    1   2   3   4   5   6   7   8   9")

    start_char = 64
    row = []
    for i in coord_list:
        row.append(coord_list[i])

        if len(row) == 9:
            print(chr(start_char + i[0]) + " | " + " | ".join(row) + " |")
            row = []


def rand_coord():
    import random
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    return num1, num2


def generate_machine_ships() -> list:
    from constants.constants import SHIPS, SHIP_CHARS
    from ship import Ship
    from ship_manager import ShipManager

    ships_list = []

    # Runs the code for every key of the SHIPS dictionary. So the code will run once for every ship in the SHIPS
    # dictionary
    for ship_name in SHIPS:
        # Creates a ship object, with both it's name and length from the SHIPS constants dictionary
        ship = Ship(ship_name, SHIPS[ship_name])
        ship.char = SHIP_CHARS[ship_name]

        # Runs the function 'place_ship', which calls the methods inside ship object to set its location to a random
        # place on the grid
        ShipManager.set_rand_location(ship)

        ships_list.append(ship)

    return ships_list


def set_rand_location(ship):
    import random
    from ship import check_overlap, get_ship_coords

    # Generates a random coordinate inside the grid
    coordinate = rand_coord()

    # Coordinate where the placement of the ship starts
    start_x = coordinate[0]
    start_y = coordinate[1]

    # Random 0-3. Inclusive of 0 and 3
    random_rotation = random.randint(0, 3)

    # Rotational values. All 4 different rotations a ship can have from a starting coordinate
    rotation_values = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # Assigning rotational values for the current ship being placed.
    rot_x, rot_y = rotation_values[random_rotation]

    ship_coordinates = get_ship_coords(start_x, start_y, rot_x, rot_y, ship.length)

    if check_overlap(ship_coordinates, Ship.occupied_coordinates):
        set_rand_location(ship)

    # Checks if the ship could fit in the grid, with its current selected random location and rotation
    if (
            start_x + rot_x * ship.length > 8
            or start_x + rot_x * ship.length < 0
            or start_y + rot_y * ship.length > 8
            or start_y + rot_y * ship.length < 0
    ):
        # Calls the function again to place the ship again, because the random location and rotation made it not fit
        set_rand_location(ship)
    else:

        ship.location = (start_x, start_y)
        ship.rotation = (rot_x, rot_y)
        Ship.occupied_coordinates.extend(ship.get_coords())

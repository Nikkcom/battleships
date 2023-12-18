class ShipManager:
    occupied_coordinates = []

    @staticmethod
    def set_rand_location(ship):
        from screen.coordinates import rand_coord
        from ship import get_ship_coords, check_overlap
        import random
        while True:
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

            if (
                    start_x + rot_x * ship.length > 8
                    or start_x + rot_x * ship.length < 0
                    or start_y + rot_y * ship.length > 8
                    or start_y + rot_y * ship.length < 0
            ):
                # Calls the function again to place the ship again, because the random location and rotation made it
                # not fit
                continue

            if not check_overlap(ship_coordinates, ShipManager.occupied_coordinates):
                ship.location = (start_x, start_y)
                ship.rotation = (rot_x, rot_y)

                ShipManager.occupied_coordinates.extend(ship_coordinates)
                break

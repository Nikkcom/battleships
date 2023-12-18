class Ship:
    occupied_coordinates = []

    def __init__(self, name, length, char="#"):
        self.name = name
        self.length = length
        self.char = char
        self.alive = True
        self.location = None
        self.rotation = None

    def __str__(self):
        return (f"(Name: {self.name}, Length: {self.length}," +
                f" Char: {self.char}, Location: {self.location}, Rotation: {self.rotation})")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, boolean):
        self.__alive = boolean

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def char(self):
        return self.__char

    @char.setter
    def char(self, char):
        self.__char = char

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation):
        self.__rotation = rotation

    def get_coords(self):
        return get_ship_coords(self.location[0], self.location[1], self.rotation[0], self.rotation[1], self.length)


def get_ship_coords(start_x, start_y, rot_x, rot_y, length):
    coordinates = []
    for i in range(length):
        x = start_x + i * rot_x
        y = start_y + i * rot_y
        coordinates.append((x, y))
    return coordinates


def check_overlap(ship_coordinates, occupied_coordinates):
    return any(coord in occupied_coordinates for coord in ship_coordinates)

from models.soldiers import Soldier


class Room:
    id: int
    max_occpiers: int
    current_residances: list[Soldier]
    current_num_of_residances: int

    def __init__(self, id, max_occpiers=8) -> None:
        self.id = id
        self.max_occpiers = max_occpiers
        self.current_residances = []
        self.current_num_of_residances = len(self.current_residances)


class Building:
    id: int
    num_of_rooms: int
    waiting_list: list[Soldier]
    rooms: list[Room]

    def __init__(self, id, room_num=10) -> None:
        self.id = id
        self.num_of_rooms = room_num
        self.waiting_list = []
        self.rooms = []
        self.gen_rooms()

    def gen_rooms(self):
        for num in range(self.num_of_rooms):
            self.rooms.append(Room(num + 1))


class Base:
    num_of_buildings: int = 2
    buildings: list[Building]

    def init_buildings(self):
        for num in range(self.num_of_buildings):
            self.buildings.append(Building(num + 1))

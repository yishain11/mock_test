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
        self.update_residence_num()

    def update_residence_num(self):
        self.current_num_of_residances = len(self.current_residances)

    def report_vacany(self):
        if self.max_occpiers == self.current_num_of_residances:
            return -1
        else:
            return self.id

    def add_soldier(self, new_soldier: Soldier):
        if self.max_occpiers == self.current_num_of_residances:
            print("sorry, max capacity")
            return False
        self.current_residances.append(new_soldier)
        self.update_residence_num()


class Building:
    id: int
    num_of_rooms: int
    waiting_list: list[Soldier]
    rooms: list[Room]
    rooms_id_vacancy: list[int]

    def __init__(self, id, room_num=10) -> None:
        self.id = id
        self.num_of_rooms = room_num
        self.waiting_list = []
        self.rooms = []
        self.gen_rooms()
        self.find_vacant_rooms()

    def gen_rooms(self):
        for num in range(self.num_of_rooms):
            self.rooms.append(Room(num + 1))

    def find_vacant_rooms(self):
        # maybe refactor later to remove rooms by id when occupied
        self.rooms_id_vacancy = []
        for room in self.rooms:
            is_vacant_id = room.report_vacany()
            if is_vacant_id > 0:
                self.rooms_id_vacancy.append(is_vacant_id)


class Base:
    num_of_buildings: int = 2
    buildings: list[Building]

    def init_buildings(self):
        for num in range(self.num_of_buildings):
            self.buildings.append(Building(num + 1))

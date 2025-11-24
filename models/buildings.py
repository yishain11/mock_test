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

    def report_vacancy_rooms(self):
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
        return True


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
            is_vacant_id = room.report_vacancy_rooms()
            if is_vacant_id > 0:
                self.rooms_id_vacancy.append(is_vacant_id)

    def report_vacancy_building(self):
        if len(self.rooms_id_vacancy) == 0:
            print(f"no rooms found in building: {self.id}")
            return False
        return self.rooms_id_vacancy

    def add_soldier_to_room(self, new_soldier: Soldier, room_id: int):
        room_list = [r for r in self.rooms if r.id == room_id]
        if len(room_list) == 0:
            print("no room found")
            return False
        room = room_list[0]
        res = room.add_soldier(new_soldier)
        if res:
            print("soldier added successfully")
            return True
        print("soldier was not added!")
        return False


class Base:
    num_of_buildings: int = 2
    buildings: list[Building]

    def init_buildings(self):
        for num in range(self.num_of_buildings):
            self.buildings.append(Building(num + 1))

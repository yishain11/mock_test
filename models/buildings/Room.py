from models.soldiers import Soldier
from models.data.building_data import Room_data


class Room:
    id: int
    max_occpiers: int
    current_residances: list[Soldier]
    room_data: Room_data

    def __init__(self, id, max_occpiers=8) -> None:
        self.id = id
        self.max_occpiers = max_occpiers
        self.current_residances = []

    def gen_room_data(self):
        self.room_data = Room_data(
            self.id,
            self.max_occpiers - self.get_residance_num(),
        )

    def get_residance_num(self):
        return len(self.current_residances)

    def report_vacancy_rooms(self):
        self.gen_room_data()
        return self.room_data

    def add_soldier(self, new_soldier: Soldier):
        if self.max_occpiers == self.get_residance_num():
            print("sorry, max capacity")
            return False
        self.current_residances.append(new_soldier)
        return True

    def get_available_beds_num(self):
        return self.max_occpiers - self.get_residance_num()

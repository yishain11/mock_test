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
            return {
                "id": self.id,
                "available_beds_num": self.max_occpiers
                - self.current_num_of_residances,
            }

    def add_soldier(self, new_soldier: Soldier):
        if self.max_occpiers == self.current_num_of_residances:
            print("sorry, max capacity")
            return False
        self.current_residances.append(new_soldier)
        self.update_residence_num()
        return True

    def get_available_beds_num(self):
        return self.max_occpiers - self.current_num_of_residances

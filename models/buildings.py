from models.soldiers import Soldier


class Room:
    max_occpiers: int
    current_residances: list[Soldier]
    current_num_of_residances: int


class Building:
    room_num: int = 8
    waiting_list: list[Soldier] = []
    rooms: list[Room]

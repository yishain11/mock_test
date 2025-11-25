from models.soldiers import Soldier
from models.buildings.Room import Room
from models.data.building_data import Room_data, Building_data


class Building:
    id: int
    num_of_rooms: int
    rooms: list[Room]
    total_available_beds: int

    def __init__(self, id, room_num=10) -> None:
        self.id = id
        self.num_of_rooms = room_num
        self.waiting_list = []
        self.rooms = []
        self.gen_rooms()
        self.update_num_of_available_beds()

    def gen_rooms(self):
        for num in range(self.num_of_rooms):
            room = Room(num)
            self.rooms.append(Room(num))

    def update_num_of_available_beds(self):
        count = 0
        for room in self.rooms:
            count += room.get_available_beds_num()
        self.total_available_beds = count

    def populate_building(self, soldier_list: list[Soldier]):
        """
        1. for each soldier loop on rooms
        2. if room have availalble beds: add soldier until no
        3. continue until no more soldiers
        """
        print(f"populating buildin: {self.id} with {len(soldier_list)} soldiers")
        soldeirs_populate_report = []  # class later
        while len(soldier_list) > 0:
            for r in self.rooms:
                print(f"populating room: {r.id} in building: {self.id}")
                while r.get_available_beds_num() > 0 and len(soldier_list) > 0:
                    print(
                        f"available beds in room {r.id}: {r.get_available_beds_num()}"
                    )
                    if len(soldier_list) > 0:
                        s = soldier_list.pop()
                        if r.add_soldier(s):
                            print(
                                f"soldier {s.first_name} {s.last_name} was added to room {r.id}"
                            )
                            s.change_status(f"housed in bulding {self.id} room: {r.id}")
                            report = {
                                "soldier_id": s.personal_num,
                                "status": s.status_hosing,
                            }
                            soldeirs_populate_report.append(report)
        print(
            f"done populating building {self.id}, populated: {len(soldeirs_populate_report)}"
        )
        return soldeirs_populate_report

    def add_soldier_to_room_by_id(self, new_soldier: Soldier, room_id: int):
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

    def find_room_by_id(self, id: int):
        for r in self.rooms:
            if r.id == id:
                return r
        print(f"no room was found! for id: {id}")
        return {}

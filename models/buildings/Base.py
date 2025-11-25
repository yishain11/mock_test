from models.soldiers import Soldier
from models.buildings.Building import Building


class Base:
    soldier_list: list[Soldier]
    num_of_buildings: int
    buildings: list[Building]
    soldier_waiting_list: list[Soldier]

    def __init__(self, soldier_list, num_of_buildings=2) -> None:
        self.buildings = []
        self.soldier_list = soldier_list
        self.soldier_waiting_list = []
        self.num_of_buildings = num_of_buildings
        self.init_buildings()

    def init_buildings(self):
        for num in range(self.num_of_buildings):
            self.buildings.append(Building(num))

    def calc_how_many_soldeirs_populate(self, num_of_soldiers):
        available_beds = 0
        for b in self.buildings:
            available_beds += b.total_available_beds
        delta = available_beds - num_of_soldiers
        if delta > 0:
            print("we can house everyone")
            return num_of_soldiers
        else:
            print(f"we can houst only {num_of_soldiers+delta}")
            return num_of_soldiers + delta

    def populate_base(self):
        # find building with vacancy
        # if we have enough beds
        soldiers_num_to_house = self.calc_how_many_soldeirs_populate(
            len(self.soldier_list)
        )
        reports = []
        print(f"we have {soldiers_num_to_house} soldier to house!")
        while soldiers_num_to_house > 0:
            for b in self.buildings:
                print(f"populating build num: {b.id}")
                b.update_num_of_available_beds()
                available_beds = b.total_available_beds
                soldiers_for_building = self.soldier_list[:available_beds]
                del self.soldier_list[:available_beds]
                building_report = b.populate_building(soldiers_for_building)
                reports += building_report
                soldiers_num_to_house = len(self.soldier_list)
        print("done populating base")
        self.soldier_waiting_list = self.soldier_list
        print(f"soldiers in wating list: {len(self.soldier_waiting_list )}")
        return {"housed_soldiers": reports, "waiting_list": self.soldier_list}

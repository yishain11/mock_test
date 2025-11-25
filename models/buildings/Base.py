from models.soldiers import Soldier
from models.buildings.Building import Building


class Base:
    num_of_buildings: int
    buildings: list[Building]

    def __init__(self, num_of_buildings=2) -> None:
        self.buildings = []
        self.num_of_buildings = num_of_buildings
        self.init_buildings()

    def init_buildings(self):
        for num in range(self.num_of_buildings):
            self.buildings.append(Building(num))

    def calc_populate_num(self, soldier_list: list[Soldier], building_data):
        total_available_beds = 0
        for b_id in building_data:
            total_available_beds += building_data[b_id]["total_available_beds_num"]
        delta = total_available_beds - len(soldier_list)
        if delta > 0:
            print("we can populate every soldier!")
        else:
            print(f"some soldier will have to wait... {delta} soldiers")
        return delta

    def get_building_vacancy_data(self):
        building_data = {}  # turn into class
        for b in self.buildings:
            if b.id not in building_data:
                building_data[b.id] = {}
            building_data[b.id] = b.report_vacancy_building()
        for b_id in building_data:
            if "total_available_beds_num" in building_data[b_id]:
                print(
                    f"bulding {b_id} has {building_data[b_id]["total_available_beds_num"]} open beds"
                )
        return building_data

    def populate_base(self, soldier_list: list[Soldier]):
        # find building with vacancy
        building_data = self.get_building_vacancy_data()
        print(building_data)
        # if yes - get building id, room id and num available
        # anounce how many soldiers can be populated
        # populate them (chagne status)
        # put others in waiting list

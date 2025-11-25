from models.soldiers import Soldier


def create_soldier_from_data(data: list[str]):
    soldiers_list = []
    for id, line in enumerate(data):
        if id == 0:
            continue
        line = line.split(",")
        personal_num = line[0]
        first_name = line[1]
        last_name = line[2]
        city = line[3]
        distance = line[4]  # validate num
        soldier = Soldier(
            personal_num, first_name, last_name, city, int(distance), "ממתין"
        )
        soldiers_list.append(soldier)
    soldiers_list.sort(key=lambda x: x.distance, reverse=True)
    return soldiers_list

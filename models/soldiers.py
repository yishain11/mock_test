class Soldier:
    personal_num: int
    first_name: str
    last_name: str
    city: str
    distance: int
    status_hosing: str

    def __init__(
        self,
        personal_num,
        first_name,
        last_name,
        city,
        distance,
        status_hosting="ממתין",
    ) -> None:
        self.personal_num = personal_num
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.distance = distance
        self.status_hosing = status_hosting

    def change_status(self, new_status):
        if new_status not in ["שובץ למגורים", "ממתין"]:
            print("wrong status, cannot change")
            return False
        self.status_hosing = new_status
        print("status changed")
        return True

    def get_distance(self):
        return self.distance

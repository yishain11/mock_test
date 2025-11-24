from fastapi import FastAPI, UploadFile
from models.buildings import Base
from models.soldiers import Soldier

app = FastAPI()


@app.post("/assignWithCSV")
async def root(file: UploadFile):
    soldiers_list = []
    content = await file.read()
    content = content.decode("UTF-8").splitlines()
    for id, line in enumerate(content):
        if id == 0:
            continue
        line = line.split(",")
        print("line", line, "len", len(line))
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
    base = Base()

    return {"message": "Hello World"}

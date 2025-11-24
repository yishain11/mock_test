from fastapi import FastAPI, UploadFile
from models.buildings import Base

app = FastAPI()


@app.post("/assignWithCSV")
async def root(file: UploadFile):
    data = []
    content = await file.read()
    content = content.decode("UTF-8").splitlines()
    for line in content:
        print("line:\n", line)
        data.append(line)
    base = Base()
    return {"message": "Hello World"}

from fastapi import FastAPI, UploadFile
from models.buildings.Base import Base
from utils.create_soldiers import create_soldier_from_data
from utils.data_proccesing import process_csv_from_req
import uvicorn

app = FastAPI()
# curl -F file=@"./data/soldiers.csv" -XPOST localhost:8000/assignWithCSV


@app.post("/assignWithCSV")
async def root(file: UploadFile):
    # todo - cleanup and breakdown
    content = await process_csv_from_req(file)
    soldiers_list = create_soldier_from_data(content)
    base = Base(soldiers_list)
    report = base.populate_base()
    report["total_housed"] = len(report["housed_soldiers"])
    report["waiting_list_num"] = len(report["waiting_list"])
    return report


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

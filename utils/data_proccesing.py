from fastapi import UploadFile


async def process_csv_from_req(file: UploadFile):
    content = await file.read()
    content = content.decode("UTF-8").splitlines()
    return content

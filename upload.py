from fastapi import APIRouter, File, UploadFile, HTTPException
from db_utils import upload_many
import json

upload_router = APIRouter()

@upload_router.get("/")
async def upload_health():
    return {"message": "upload_health is up!"}
    

# API to upload json file
@upload_router.post("/upload_json")
async def upload_json_file(file: UploadFile = File(...)):
    if file.content_type != 'application/json':
        raise HTTPException(status_code=400, detail="File type must be application/json")
    
    contents = await file.read()
    try:
        json_data = json.loads(contents)
        if len(json_data) == 0:
            raise HTTPException(status_code=400, detail="Empty file") 
        for obj in json_data:
            obj['total_rating'] = 0 # adding field which helps eliminate extra computing in get all courses sorting
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file")
    
    response = upload_many(json_data)
    if not response:
        raise HTTPException(status_code=500, detail="Some error occurred while uploading")
    
    return {"message": "JSON file received successfully", "data": json_data}
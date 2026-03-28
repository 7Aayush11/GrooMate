from fastapi import APIRouter, UploadFile, File
from app.services.ai_service import clothing_tagger

router = APIRouter()

@router.post("/ulpoad")
async def upload_clothing(file: UploadFile = File(...)):
    image_bytes = await file.read()
    tags = await clothing_tagger.tag_clothing_item(image_bytes)
    
    return{
        "filename": file.filename,
        "metadata": tags
    }
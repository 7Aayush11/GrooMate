from fastapi import APIRouter, UploadFile, File
from app.services.ai_service import clothing_tagger
from app.db.supabase_client import supabase

router = APIRouter()

@router.post("/ulpoad")
async def upload_clothing(file: UploadFile = File(...)):
    image_bytes = await file.read()
    tags = await clothing_tagger.tag_clothing_item(image_bytes)
    
    #Store in supabase
    data = {
        "user_id": "demo_user",
        "category": tags.get("category"),
        "color": tags.get("color"),
        "material": tags.get("material"),
        "pattern": tags.get("pattern"),
        "formality": tags.get("formality"),
    }
    
    response = supabase.table("wardrobe").insert(data).execute()
    
    return{
        "filename": file.filename,
        "metadata": tags,
        "db_response": response.data
    }
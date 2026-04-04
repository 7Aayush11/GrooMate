from fastapi import APIRouter, UploadFile, File, Depends
from app.services.ai_service import clothing_tagger
from app.db.supabase_client import supabase
from app.services.storage_service import storage_service
from app.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/ulpoad")
async def upload_clothing(file: UploadFile = File(...), user = Depends(get_current_user)):
    image_bytes = await file.read()
    
    image_url = await storage_service.upload_image(image_bytes, file.filename)
    
    tags = await clothing_tagger.tag_clothing_item(image_bytes)
    print(f"Extracted tags: {tags}")
    #Store in supabase
    data = {
        "user_id": user["user_id"],
        "category": tags.get("category"),
        "color": tags.get("color"),
        "material": tags.get("material"),
        "pattern": tags.get("pattern"),
        "formality": tags.get("formality"),
        "image_url": image_url
    }
    
    response = supabase.table("wardrobe").insert(data).execute()
    
    return{
        "image_url": image_url,
        "metadata": tags,
        "db_response": response.data
    }
from fastapi import APIRouter, UploadFile, File, Depends, Request
from app.services.ai_service import clothing_tagger
from app.db.supabase_client import supabase
from app.services.storage_service import storage_service
from app.dependencies.auth import get_current_user
from app.core.rate_limit import limiter

router = APIRouter()

@router.post("/upload")
@limiter.limit("5/minute")
async def upload_clothing(request: Request, file: UploadFile = File(...), user = Depends(get_current_user)):
    image_bytes = await file.read()
    user_id = user["id"]
    print(user)
    print(user_id)
    image_path = await storage_service.upload_image(image_bytes, file.filename)
    # image_path = 'test_path'
    
    tags = await clothing_tagger.tag_clothing_item(image_bytes)
    print(f"Extracted tags: {tags}")
    #Store in supabase
    data = {
        "user_id": user_id,
        "category": tags.get("category"),
        "color": tags.get("color"),
        "material": tags.get("material"),
        "pattern": tags.get("pattern"),
        "formality": tags.get("formality"),
        "image_path": image_path
    }
    
    response = supabase.table("wardrobe").insert(data).execute()
    
    return{
        "user_id": user_id,
        "image_path": image_path,
        "metadata": tags,
        "db_response": response.data
    }
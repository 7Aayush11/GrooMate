from fastapi import APIRouter, UploadFile, File, Depends, Request
from app.services.ai_service import clothing_tagger
from app.db.supabase_client import supabase
from app.services.storage_service import storage_service
from app.dependencies.auth import get_current_user
from app.core.rate_limit import limiter
from app.services.embedding_service import embedding_service

router = APIRouter()

@router.post("/upload")
# @limiter.limit("8/minute")
async def upload_clothing(request: Request, file: UploadFile = File(...), user = Depends(get_current_user)):
    image_bytes = await file.read()
    user_id = user["id"]
    print(user)
    print(user_id)
    image_path = await storage_service.upload_image(image_bytes, file.filename)
    # image_path = 'test_path'
    
    tags = await clothing_tagger.tag_clothing_item(image_bytes)
    print(f"Extracted tags: {tags}")
    description = clothing_tagger.build_fashion_description(tags)
    embedding = await embedding_service.generate_embedding(description)
    
    #Store in supabase
    data = {
        "user_id": user_id,
        "category": tags.get("category"),
        "color": tags.get("color"),
        "material": tags.get("material"),
        "pattern": tags.get("pattern"),
        "formality": tags.get("formality"),
        "image_path": image_path,
        "embedding": embedding,
        "style_aesthetic": tags.get("style_aesthetic", []),
        "fashion_identity": tags.get("fashion_identity", []),
        "occasion_vibes": tags.get("occasion_vibes", []),
        "season": tags.get("season", []),
        "color_energy": tags.get("color_energy", ""),
        "silhouette": tags.get("silhouette", ""),
        "layering_compatibility": tags.get("layering_compatibility", ""),

        "styling_notes": tags.get("styling_notes", "")
    }
    
    response = supabase.table("wardrobe").insert(data).execute()
    
    return{
        "user_id": user_id,
        "image_path": image_path,
        "metadata": tags,
        "db_response": response.data
    }
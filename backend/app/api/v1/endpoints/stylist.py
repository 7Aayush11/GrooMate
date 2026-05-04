from fastapi import APIRouter, Depends
from app.db.supabase_client import supabase
from app.services.stylist_service import stylist_service
from app.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/recommend")
async def recommend_outfit(event:str, user=Depends(get_current_user)):
    user_id = user["sub"]
    # Fetch Wardrobe
    response = supabase.table("wardrobe").select("*").eq("user_id", user_id).execute()
    print(f"Supabase response: {response}")  #Debugging line
    closet_items = response.data
    
    if not closet_items:
        return {"error": "No wardrobe data found"}
    
    suggestion = await stylist_service.generate_outfit_suggestion(
        closet_items,
        event
    )
    
    return suggestion

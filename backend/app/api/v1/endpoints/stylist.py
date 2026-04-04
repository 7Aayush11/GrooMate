from fastapi import APIRouter
from app.db.supabase_client import supabase
from app.services.stylist_service import stylist_service

router = APIRouter()

@router.post("/recommend")
async def recommend_outfit(event:str):
    
    # Fetch Wardrobe
    response = supabase.table("wardrobe").select("*").execute()
    print(f"Supabase response: {response}")  #Debugging line
    closet_items = response.data
    
    if not closet_items:
        return {"error": "No wardrobe data found"}
    
    suggestion = await stylist_service.generate_outfit_suggestion(
        closet_items,
        event
    )
    
    return suggestion

from fastapi import APIRouter, Depends, Request
from app.db.supabase_client import supabase
from app.services.stylist_service import stylist_service
from app.dependencies.auth import get_current_user
from app.core.rate_limit import limiter
from app.services.recommendation_engine import recommendation_engine
router = APIRouter()

@router.post("/recommend")
@limiter.limit("5/minute")
async def recommend_outfit(request: Request, event:str, user=Depends(get_current_user)):
    user_id = user["id"]
    # Fetch Wardrobe
    response = supabase.table("wardrobe").select("*").eq("user_id", user_id).execute()
    closet_items = response.data
    
    if not closet_items:
        return {"error": "No wardrobe data found"}
    
    #Step 1 Rule Engine
    ranked_outift = await recommendation_engine.build_oufit_candidates(closet_items, event)
    
    #Step 2 AI refinement
    ai_response = await stylist_service.refine_outfit(ranked_outift, event)
    
    return {
        "outift": ranked_outift,
        "stylist_explanation": ai_response.get("styling_explanation")
    }
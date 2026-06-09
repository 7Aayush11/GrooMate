from fastapi import APIRouter, Depends
from app.db.supabase_client import supabase
from app.dependencies.auth import get_current_user
from app.services.embedding_service import embedding_service

router = APIRouter()

@router.post("/search")
async def semantic_search(query: str, user=Depends(get_current_user)):
    
    query_embedding = await embedding_service.generate_embedding(query)
    response = supabase.rpc(
        "match_wardrobe",
        {
            "query_embedding": query_embedding,
            "match_threshold": 0.5,
            "match_count": 5
        }
    ).execute()
    
    return response.data

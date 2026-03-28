from fastapi import APIRouter
from app.api.v1.endpoints import wardrode, stylist

api_router = APIRouter()

api_router.include_router(wardrode.router, prefix ="/wardrobe", tags=["Wardrobe"])
api_router.include_router(stylist.router, prefix = "/stylist", tags=["Stylist"])

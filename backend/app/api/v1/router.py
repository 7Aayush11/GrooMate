from fastapi import APIRouter
from app.api.v1.endpoints import wardrobe, stylist, auth

api_router = APIRouter()

api_router.include_router(wardrobe.router, prefix ="/wardrobe", tags=["Wardrobe"])
api_router.include_router(stylist.router, prefix = "/stylist", tags=["Stylist"])

api_router.include_router(auth.router, prefix = "/auth", tags=["Auth"])
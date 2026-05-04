from fastapi import APIRouter
from pydantic import BaseModel
from app.services.auth_service import auth_service

router = APIRouter()

class AuthRequest(BaseModel):
    email: str
    password: str
    
@router.post("/signup")
async def signup(data: AuthRequest):
    res = await auth_service.signup(data.email, data.password)
    return res

@router.post("/login")
async def login(data: AuthRequest):
    res = await auth_service.login(data.email, data.password)
    return res

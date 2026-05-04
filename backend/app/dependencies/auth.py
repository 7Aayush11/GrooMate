from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.db.supabase_client import supabase
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    print("RAW TOKEN:", token)

    try:
        user = supabase.auth.get_user(jwt=  token)
        print("SUPABASE RESPONSE:", user)

        if not user or not user.user:
            raise HTTPException(status_code=401, detail="Invalid token")

        return user.user

    except Exception as e:
        print("AUTH ERROR:", str(e))  # 🔥 THIS IS KEY
        raise HTTPException(status_code=401, detail=str(e))
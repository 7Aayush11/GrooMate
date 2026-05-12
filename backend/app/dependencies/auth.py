from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.db.supabase_client import supabase

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    
    try:
       response = supabase.auth.get_user(token)
       
       if not response or not response.user:
           raise HTTPException(status_code=401, detail="Invalid authentication")
       
       return{
           "id": response.user.id,
           "email": response.user.email
       }
       
    except Exception as e:
        print("Auth Error:", e)
        
        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired token"
        )
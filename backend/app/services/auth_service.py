from app.db.supabase_client import supabase

class AuthService:
    async def signup(self, email: str, password: str):
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })
        
        return response
    
    async def login(self, email: str, password: str):
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        
        return response

auth_service = AuthService()
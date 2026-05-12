import uuid
from app.db.supabase_client import supabase

class StorageService:
    
    async def upload_image(self, file_bytes:bytes, filename:str) -> str:
        import uuid
        
        unique_name = f"{uuid.uuid4()}_{filename}"
        
        supabase.storage.from_("wardrobe-images").upload(
            path=unique_name,
            file=file_bytes,
            file_options={"content-type": "image/jpeg"}
        )
        
        return unique_name
    
    async def get_signed_url(self, path:str):
        response = supabase.storage.from_("wardrobe-images").create_signed_url(path,3600)
        
        return response["signedURL"]
    
storage_service = StorageService()
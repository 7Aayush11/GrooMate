import uuid
from app.db.supabase_client import supabase

class StorageService:
    async def upload_image(self, file_bytes: bytes, filename: str):
        """Uploads image to Supabase Storage (wardrobe-images bucket)"""
        
        unique_name = f"{uuid.uuid4()}_{filename}"
        
        response = supabase.storage.from_("wardrobe-images").upload(
            path = unique_name,
            file = file_bytes,
            file_options ={"content-type": "image/jpeg"}
        )
        
        if response.get("error"):
            raise Exception(response["error"])
        
        public_url = supabase.storage.from_("wardrobe-images").get_public_url(unique_name)
        
        return public_url
    
storage_service = StorageService()
        
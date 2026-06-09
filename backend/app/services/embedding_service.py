from google import genai
from app.core.config import settings
from google.genai import types

client = genai.Client(api_key=settings.GEMINI_API_KEY)

class EmbeddingService:
    
    async def generate_embedding(self, text:str):
        
        response = client.models.embed_content(
            model = 'models/gemini-embedding-2',
            contents = text,
            config=types.EmbedContentConfig(task_type = 'retrieval_document',
                                            output_dimensionality=768
            )
        )
        
        return response.embeddings[0].values

embedding_service = EmbeddingService()
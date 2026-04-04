import google.generativeai as genai
from app.core.config import settings
import json

genai.configure(api_key=settings.GEMINI_API_KEY)

class StylistService:
    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash"
        )
        
    async def generate_outfit_suggestion(self, closet_items:list, event:str):
        """
        Takes users wardrobe metadata  and event context,
        returns best outfit combination
        """
        
        system_prompt = f"""
        You are a professional fashion stylist.
        EVENT : {event}
        USER CLOSET: {json.dumps(closet_items)}
        
        Task: Select exactly 3 items that create a good outfit.
        Output STRICT JSON:{{
            "outfit": [
                {{"category": "", "color": "", "reason": ""}},
                {{"category": "", "color": "", "reason": ""}},
                {{"category": "", "color": "", "reason": ""}}            
            ]
        }}
        
        Rules:
        - Only JSON
        - No explanation outside JSON
        - No markdown formatting
        """
        
        response = self.model.generate_content(system_prompt)
        
        raw_text = response.text.strip()
        
        if raw_text.startswith("```"):
            raw_text = raw_text.split("```")[1]
            
        return json.loads(raw_text)
    
stylist_service = StylistService()
import google.generativeai as genai
from app.core.config import settings
import json

genai.configure(api_key=settings.GEMINI_API_KEY)

class StylistService:
    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash"
        )
        
    async def refine_outfit(self, outfit, event:str):
        """
        Takes users wardrobe metadata  and event context,
        returns best outfit combination
        """
        
        system_prompt = f"""
        You are a professional fashion stylist.
        EVENT : {event}
        OUTFIT: {json.dumps(outfit)}
        
        Explain breifly why this outfit works.
        Return STRICT JSON:
        {{
            "styling_explanation": "",
            "confidence": "0-100"
        }}
        
        Rules to follow:
        - Return Strict Json as specifided above. Do not include any other test outside the JSON
        - No formatiing needed, just raw text in the fields
        """
        
        response = self.model.generate_content(system_prompt)
        
        raw_text = response.text.strip()
        if raw_text.startswith("```"):
            raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text.split("json")[1]
            
        print(raw_text) #Debugging line to see raw response
        return json.loads(raw_text)
    
stylist_service = StylistService()
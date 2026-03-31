import google.generativeai as genai
from app.core.config import settings
import json

#Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)

class ClothingTagger:
    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name = "gemini-2.5-flash"
        )
    
    async def tag_clothing_item(self, image_bytes: bytes) -> dict:
        '''
        Sends image to Gemini Vision model and returns structured metadata
        '''
        system_prompt = """
        You are a fashion expert. Analyze the clothing item image and return STRICT JSON only.
        Format:{
            "category": "top/bottom/shoes/accessory",
            "color": "primary color",
            "material": "fabric type",
            "pattern": "solid/stripped/printed/etc",
            "formality": "casual/semi-formal/formal"
        }
        Rules:
         - No explanation
         - No extra text
         - Only valid JSON
         - No Markdown formatting
        """
        
        try:
            response = self.model.generate_content(
                [
                    system_prompt,{
                        "mime_type": "image/jpeg",
                        "data": image_bytes
                    }
                ]
            )
            
            #Extract JSON from response
            raw_text = response.text.strip()
            
            #Handle cases where model adds ```json``` wrappers
            if raw_text.startswith("```"):
                print("Detected code block formatting, extracting JSON...")  #Debugging line
                raw_text = raw_text.split("```")[1]
                print("Raw model response:", raw_text)  #Debugging line
                
            parsed = json.loads(raw_text)
            
            return parsed
        
        except Exception as e:
            return{
                "error": str(e),
                "raw_response": response.text if 'response' in locals() else None
            }

#Sinlgeton instance (important for performance)
clothing_tagger = ClothingTagger()
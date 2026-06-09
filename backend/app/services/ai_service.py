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
            "category": "",
            "color": "",
            "material": "",
            "pattern": "",
            "formality": "",

            "style_aesthetic": [],
            "fashion_identity": [],
            "occasion_vibes": [],
            "season": [],
            "color_energy": "",
            "silhouette": "",
            "layering_compatibility": "",

            "styling_notes": ""
        }

        Focus heavily on:
         - fashion aesthetics
         - cultural style associations
         - modern fashion language
         - vibe interpretation
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
    
    def build_fashion_description(self, tags):
        aesthetics = " ".join(tags['style_aesthetic'])
        identities = " ".join(tags['fashion_identity'])
        vibes = " ".join(tags['occasion_vibes'])
        seasons = " ".join(tags['season'])
        
        return f"""{tags['color']} {tags['material']} {tags['category']}
            Aesthetic: {aesthetics}
            Fashion Identity: {identities}
            Occasion Vibes: {vibes}
            Seasons: {seasons}
            Color Energy: {tags['color_energy']}
            Silhouette: {tags['silhouette']}
            Styling Notes:{tags['styling_notes']}"""

#Sinlgeton instance (important for performance)
clothing_tagger = ClothingTagger()
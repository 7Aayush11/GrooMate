from collections import defaultdict
from app.services.color_engine import calculate_color_score

class RecommendationEngine:
    async def build_oufit_candidates(self, closet_items, event):
        
        tops = []
        bottoms = []
        shoes = []
        
        for item in closet_items:
            
            category = item["category"]
            
            if category == "top":
                tops.append(item)
            elif category == "bottom":
                bottoms.append(item)
            elif category == "shoes":
                shoes.append(item)
            
        best_score = -1
        best_outfit = None
        
        for top in tops:
            for bottom in bottoms:
                for shoe in shoes:
                    score = 0
                    
                    score += calculate_color_score(top["color"], bottom["color"])
                    score += calculate_color_score(bottom["color"], shoe["color"])
                    
                    if(top["formality"]==bottom["formality"]==shoe["formality"]):
                        score += 15
                    
                    if score > best_score:
                        best_score = score
                        
                        best_outfit = {
                            "top": top,
                            "bottom": bottom,
                            "shoes": shoe,
                            "score": score
                        }
        return best_outfit
    
recommendation_engine = RecommendationEngine()
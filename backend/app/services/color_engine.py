COMPATIBLE_COLORS = {
    "black": ["white", "grey", "red", "blue", "beige"],
    "white": ["black", "grey", "blue"],
    "blue": ["white", "black", "grey"],
    "beige": ["black", "brown", "white"],
    "grey": ["black", "white", "blue"]
}

def calculate_color_score(color1: str, color2: str):
    if color2 in COMPATIBLE_COLORS.get(color1, []):
        return 10
    
    return 3

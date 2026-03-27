# 👔 Groomate: Your AI-Powered Digital Stylist

## Overview

**Groomate** is a smart wardrobe assistant designed to eliminate "decision fatigue." By digitizing your closet and leveraging **Gemini 1.5 Flash**, Groomate suggests the perfect outfit for any event based on the clothes you actually own.

## 🚀 Key Features
- **Wardrobe Digitizer:** Fast, AI-driven tagging of clothing items (category, color, fabric, formality) via photo upload.
- **Event-Based Recommendations:** Context-aware styling (e.g., "What should I wear to a casual outdoor wedding?").
- **"Shop the Look" Integration:** Identifies gaps in your outfit and suggests missing items to buy via web search.
- **Outfit Archive:** Save your favorite combinations in a digital lookbook.
- **Smart Search:** Filter your closet by material, weather appropriateness, or color palette.

## 🏗️ System Architecture

The project follows a **decoupled, cloud-native architecture** designed for high-performance AI inference.

### **The Tech Stack**
| Layer | Technology |
|---------|------------|
| Frontend | React Native (Expo) |
| Backend | FastAPI (Python 3.11+) |
| AI / LLM | Gemini 1.5 Flash (Vision & Reasoning) |
| Database | Supabase (PostgreSQL + pgvector) |
| Storage | Cloudinary (Image Optimization) |
| Infrastructure | Oracle Cloud (Always Free ARM Tier) |

## 🛠️ Getting Started

### **1. Prerequisites**
- **Python 3.11+**
- **Node.js & npm** (for Expo)
- **API Keys:** Google AI Studio (Gemini), Supabase, Cloudinary.

### **2. Backend Setup**
```bash
# Navigate to backend
dd backend
# Create virtual environment
python -m venv venv
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt
# Run the server
uvicorn main:app --reload
```

### **3. Frontend Setup**
```bash
dd frontend 
npm install 
npx expo start \
```

## 📅 Roadmap (14-Week Plan)
- Weeks 1-2: Discovery & Styling Logic Definition.
- Weeks 3-4: Architecture Setup (FastAPI + Supabase).
- Weeks 5-8: Core AI Engine (Gemini Vision Tagging & Outfit RAG).
- Weeks 9-11: Mobile UI Development & Wardrobe Management.
- Weeks 12-14: Beta Testing, Refinement, & Cloud Deployment.
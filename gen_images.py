#!/usr/bin/env python3
import json, base64, urllib.request, urllib.error, sys, time

API_KEY = "AIzaSyAVnyir1j5Cg0EKGChiyMeakQoCsruOha0"
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent"
OUT_DIR = "/Users/eduardorolim/Documents/Documentos Atual - MacBook Air de Eduardo/carrossel-v2-edu-99hud/output/amazon-transformer/img"

PROMPTS = {
    "01": "Cinematic portrait of a person holding a sleek smartphone with glowing screen, dark moody dramatic lighting, deep shadows, photorealistic, no text, no words, portrait orientation",
    "02": "Professional person using voice assistant smart speaker and smartphone simultaneously in modern dark home, ambient blue glow, cinematic moody lighting, photorealistic, no text, no words",
    "04": "Close-up of interconnected smartphone screens forming an ecosystem of apps and services, abstract tech concept, dark dramatic lighting, cinematic, photorealistic, no text, no words",
    "05": "Old abandoned smartphone lying on dark surface with dramatic single spotlight, melancholic failure concept, cinematic, photorealistic, no text, no words",
    "06": "Person speaking voice commands to smart home device at night, ambient warm glow, cinematic portrait, photorealistic, no text, no words",
    "07": "Hand smoothly gliding across glowing smartphone screen, frictionless motion concept, dark background with light trails, cinematic, photorealistic, no text, no words",
    "08": "Person receiving instant purchase confirmation on smartphone with one tap, dark moody lighting, e-commerce concept, cinematic portrait, photorealistic, no text, no words",
    "09": "Aerial view of massive logistics distribution center illuminated at night with glowing delivery routes, cinematic aerial photography, photorealistic, no text, no words",
    "10": "Thoughtful person staring at smartphone with concern and caution, data privacy concept, dramatic side lighting, cinematic portrait, photorealistic, no text, no words",
    "12": "Person surrounded by glowing connected subscription app icons on multiple devices, ecosystem lock-in concept, dark moody lighting, cinematic, photorealistic, no text, no words",
    "13": "Person automatically reaching for smartphone out of muscle memory habit, behavioral psychology concept, dramatic dark lighting, cinematic portrait, photorealistic, no text, no words",
    "14": "Abstract AI neural network visualization with glowing data nodes and connections on dark background, cinematic, photorealistic, no text, no words",
    "15": "Person standing in front of massive server room with blue ambient lighting from server racks, AI infrastructure concept, cinematic portrait, photorealistic, no text, no words",
    "16": "Person holding smartphone as central command device with multiple smart screens in dark background, control room concept, cinematic portrait, photorealistic, no text, no words",
    "17": "Person at digital crossroads with glowing pathway options on smartphone screen, choice and dependency concept, dark moody lighting, cinematic portrait, photorealistic, no text, no words",
    "18": "Dynamic editorial journalist or content creator in dark modern studio with glowing laptop screen, creative professional, cinematic portrait, photorealistic, no text, no words",
}

def generate_image(slide_num, prompt):
    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]}
    }).encode("utf-8")

    req = urllib.request.Request(
        ENDPOINT,
        data=payload,
        headers={
            "x-goog-api-key": API_KEY,
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
        parts = data["candidates"][0]["content"]["parts"]
        for part in parts:
            if "inlineData" in part:
                img_data = base64.b64decode(part["inlineData"]["data"])
                path = f"{OUT_DIR}/slide_{slide_num}.jpg"
                with open(path, "wb") as f:
                    f.write(img_data)
                print(f"✅ slide_{slide_num}.jpg salvo ({len(img_data)//1024}KB)")
                return True
        print(f"❌ slide_{slide_num}: sem inlineData na resposta")
        return False
    except Exception as e:
        print(f"❌ slide_{slide_num}: erro — {e}")
        return False

for num, prompt in PROMPTS.items():
    print(f"🔄 Gerando imagem {num}...")
    ok = generate_image(num, prompt)
    if not ok:
        sys.exit(1)
    time.sleep(0.5)

print("\n✅ Todas as imagens geradas!")

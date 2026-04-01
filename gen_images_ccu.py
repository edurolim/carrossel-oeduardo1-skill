#!/usr/bin/env python3
import json, base64, urllib.request, time, sys

API_KEY = "AIzaSyAVnyir1j5Cg0EKGChiyMeakQoCsruOha0"
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent"
OUT = "/Users/eduardorolim/Documents/Documentos Atual - MacBook Air de Eduardo/carrossel-v2-edu-99hud/output/claude-computer-use/img"

PROMPTS = {
    "01": "AI invisible hand controlling a computer mouse on a dark desk, glowing cursor moving autonomously, dramatic cinematic light beams, no human visible, photorealistic, no text, no words, portrait orientation",
    "02": "Holographic AI interface controlling a laptop screen with multiple apps opening simultaneously, dark moody atmosphere, electric blue glow, cinematic, photorealistic, no text, no words",
    "03": "Computer screen showing multiple apps open simultaneously with automated workflow arrows connecting them, dark dramatic studio lighting, cinematic, photorealistic, no text, no words",
    "04": "Glowing permission dialog floating in dark cyberspace, AI requesting access to apps, dramatic neon authorization concept, cinematic, photorealistic, no text, no words",
    "05": "Spreadsheet filling itself automatically with glowing data streams, robotic automation concept, dark dramatic background, cinematic, photorealistic, no text, no words",
    "06": "Stock market trading floor with massive red numbers crashing on screens, enterprise software sector collapse visualization, dark dramatic cinematic, photorealistic, no text, no words",
    "07": "Industrial robot arm being replaced by a sleek glowing AI interface, RPA disruption concept, dramatic contrast between old and new, cinematic, photorealistic, no text, no words",
    "08": "Professional person turning away from computer screen towards a window with bright future, attention redistribution concept, dark-to-light gradient, cinematic portrait, photorealistic, no text, no words",
    "09": "Person typing a comment on a glowing smartphone in dark room with anticipation, community engagement and call to action concept, dramatic moody lighting, cinematic portrait, photorealistic, no text, no words",
}

def gen(num, prompt):
    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]}
    }).encode()
    req = urllib.request.Request(ENDPOINT, data=payload,
        headers={"x-goog-api-key": API_KEY, "Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read())
        for part in data["candidates"][0]["content"]["parts"]:
            if "inlineData" in part:
                img = base64.b64decode(part["inlineData"]["data"])
                with open(f"{OUT}/slide_{num}.jpg", "wb") as f: f.write(img)
                print(f"✅ slide_{num}.jpg ({len(img)//1024}KB)")
                return True
        print(f"❌ slide_{num}: sem imagem"); return False
    except Exception as e:
        print(f"❌ slide_{num}: {e}"); return False

for num, prompt in PROMPTS.items():
    print(f"🔄 {num}...")
    if not gen(num, prompt): sys.exit(1)
    time.sleep(0.5)

print("\n✅ Todas prontas!")

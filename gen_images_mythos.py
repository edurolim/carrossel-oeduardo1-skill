#!/usr/bin/env python3
import json, base64, urllib.request, time, sys, os

def load_dotenv(path=".env"):
    if not os.path.exists(path):
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())

load_dotenv()

API_KEY = os.environ["OPENAI_API_KEY"]
ENDPOINT = "https://api.openai.com/v1/images/generations"
MODEL = "gpt-image-1"
SIZE = "1024x1536"
QUALITY = "high"
OUT_DIR = "/Users/eduardorolim/Documents/Documentos Atual - MacBook Air de Eduardo/carrossel-v2-edu-99hud/output/claude-mythos/img"

PROMPTS = {
    "01": "Mysterious glowing AI neural network orb with dark cinematic background, deep shadows, electric blue and purple energy, powerful and secretive atmosphere, photorealistic, no text, no words, portrait orientation",
    "02": "Digital data breach concept, thousands of glowing files cascading through dark cyberspace, exposed documents floating in dark void, ominous red warning glow, cinematic, photorealistic, no text, no words",
    "03": "Sealed classified document being dramatically revealed with light burst, mysterious capybara silhouette in shadows, dramatic revelation concept, dark cinematic, photorealistic, no text, no words",
    "04": "Ascending hierarchy of glowing AI model tiers represented as luminous crystals, fourth tier emerging above the others with golden light, dark dramatic background, cinematic, photorealistic, no text, no words",
    "05": "Restricted powerful AI behind glowing containment barriers, warning symbols in dark dramatic scene, dangerous energy barely contained, cinematic portrait, photorealistic, no text, no words",
    "06": "Corporate enterprise boardroom with AI holographic interface displaying business charts, executives silhouetted against glowing screens, dark dramatic lighting, cinematic, photorealistic, no text, no words",
    "07": "Developer hands typing on keyboard with glowing API code streams flowing in dark background, automation pipelines visualized as light trails, cinematic moody, photorealistic, no text, no words",
    "08": "High-speed market race visualization, business figures accelerating past competitors, glowing finish line ahead, dark dramatic cinematic, photorealistic, no text, no words",
    "09": "Person looking at glowing smartphone screen in dark room with sense of urgency and forward momentum, sharing and saving concept, dramatic moody lighting, cinematic portrait, photorealistic, no text, no words",
}

def generate(num, prompt):
    payload = json.dumps({
        "model": MODEL, "prompt": prompt, "size": SIZE, "quality": QUALITY, "n": 1
    }).encode()
    req = urllib.request.Request(ENDPOINT, data=payload,
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.loads(r.read())
        img = base64.b64decode(data["data"][0]["b64_json"])
        path = f"{OUT_DIR}/slide_{num}.jpg"
        with open(path, "wb") as f: f.write(img)
        print(f"✅ slide_{num}.jpg ({len(img)//1024}KB)")
        return True
    except Exception as e:
        print(f"❌ slide_{num}: {e}"); return False

for num, prompt in PROMPTS.items():
    print(f"🔄 Gerando {num}...")
    if not generate(num, prompt): sys.exit(1)
    time.sleep(0.5)

print("\n✅ Todas as imagens geradas!")

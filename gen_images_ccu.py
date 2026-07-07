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
        "model": MODEL, "prompt": prompt, "size": SIZE, "quality": QUALITY, "n": 1
    }).encode()
    req = urllib.request.Request(ENDPOINT, data=payload,
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.loads(r.read())
        img = base64.b64decode(data["data"][0]["b64_json"])
        with open(f"{OUT}/slide_{num}.jpg", "wb") as f: f.write(img)
        print(f"✅ slide_{num}.jpg ({len(img)//1024}KB)")
        return True
    except Exception as e:
        print(f"❌ slide_{num}: {e}"); return False

for num, prompt in PROMPTS.items():
    print(f"🔄 {num}...")
    if not gen(num, prompt): sys.exit(1)
    time.sleep(0.5)

print("\n✅ Todas prontas!")

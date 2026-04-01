#!/usr/bin/env python3
import json, base64, urllib.request, sys, time

API_KEY = "AIzaSyAVnyir1j5Cg0EKGChiyMeakQoCsruOha0"
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image-preview:generateContent"
OUT_DIR = "/Users/eduardorolim/Documents/Documentos Atual - MacBook Air de Eduardo/carrossel-v2-edu-99hud/output/openai-ipo/img"

PROMPTS = {
    "01": "Extreme close-up portrait of a 52-year-old Wall Street executive, tie loosened, jaw clenched, eyes fixed off-camera with disbelief mixed with awe at something massive, harsh single overhead light, deep shadows carving his face, sweat catching the light, cinematic, photorealistic, 35mm film grain, high contrast, no text, no words, portrait orientation",
    "02": "Low-angle shot of a single person standing at the center of a massive empty trading floor in complete darkness, one workstation glowing blue-white illuminating only their silhouette, hundreds of dark screens stretching into shadows behind, about to execute something historic, cinematic noir, photorealistic, no text, no words",
    "03": "Bird's eye aerial view of a single glowing office window in an enormous dark corporate skyscraper at night, one light on among hundreds of dark windows, lone operator concept, cinematic aerial, deep blacks, photorealistic, no text, no words",
    "04": "Low angle shot looking up at a glass skyscraper under explosive rapid construction, scaffolding and cranes against a dark stormy sky, relentless upward momentum, workers as tiny silhouettes against metal and light, cinematic dramatic, photorealistic, no text, no words",
    "05": "Single tiny human figure standing at the absolute summit of an enormous mountain at dawn, vast golden and violet sky filling 80 percent of the frame, scale of one person against something unprecedented, epic silhouette, cinematic wide shot, photorealistic, no text, no words",
    "06": "Close-up of a hand mid-gesture pulling back a thick curtain, revealing only darkness behind a brightly lit facade, split second of revelation, dramatic theatrical side lighting, shallow depth of field on the hand, cinematic, photorealistic, no text, no words",
    "07": "Extreme macro close-up of a single match burning intensely, dark background, warm flame light casting dancing shadows on a surface below, beautiful and brief destruction, metaphor for spending faster than earning, cinematic, photorealistic, no text, no words",
    "08": "Extreme close-up portrait of a person's face, one eye perfectly in focus catching a single beam of harsh directional light, jaw set hard, skin texture visible, expression of absolute unwavering resolve and obsession, no softness, cinematic, photorealistic, 50mm lens, high contrast, no text, no words",
    "09": "Person with open upturned hands receiving a cascade of falling golden coins and warm light streaming from directly above in complete darkness, receiving value from unseen benefactor, dramatic upward chiaroscuro lighting, cinematic, photorealistic, no text, no words",
    "10": "Macro close-up of an old brass scale tipping dramatically, one side crashing down while other lifts, sharp dramatic overhead light creating deep shadows, irreversible balance shift, cinematic, photorealistic, no text, no words",
    "11": "Over-the-shoulder shot of a person hunched at a desk examining a document with large numbers, cold fluorescent office light at night, tension in their shoulders, hand pressed flat on the paper, realization of a cost they did not expect, cinematic, photorealistic, no text, no words",
    "12": "Aerial bird's eye drone shot of tens of thousands of people filling a massive city plaza, overwhelming scale from directly above, tiny figures as far as the eye can see, the immensity of $852 billion in human terms, cinematic drone photography, photorealistic, no text, no words",
    "13": "Low-angle dramatic shot looking up at a single glass tower dwarfing an entire row of classic industrial factory buildings in its shadow, new economy crushing old economy in scale, dramatic stormy sky, cinematic, photorealistic, no text, no words",
    "14": "Silhouette of massive oil derricks against a blazing golden desert sunset sky, old world industrial power at peak, the benchmark that is about to be surpassed, epic wide cinematic shot, photorealistic, no text, no words",
    "15": "Two runners side by side in a dark tunnel sprinting toward a blinding white light ahead, neck and neck, motion blur on legs and arms, race completely open, cinematic, photorealistic, no text, no words",
    "16": "Person standing motionless at a dark crossroads, two glowing diverging paths ahead casting different colored light on their face, mid-decision stillness, Dutch angle, dramatic backlight, cinematic, photorealistic, no text, no words",
    "17": "Extreme macro close-up of a single thread under extreme tension holding an enormous dark weight above black abyss, thread fraying and about to snap, single point of failure concept, dramatic top spotlight on the thread, cinematic, photorealistic, no text, no words",
    "18": "Person standing confidently in the center of a semicircle of multiple glowing screens, arms relaxed at sides, slight controlled smile of someone who made the right bet, warm mixed light from screens illuminating them from all sides, commanding and protected position, cinematic portrait, photorealistic, no text, no words",
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
        with urllib.request.urlopen(req, timeout=90) as resp:
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
        print(json.dumps(data, indent=2)[:500])
        return False
    except Exception as e:
        print(f"❌ slide_{slide_num}: erro — {e}")
        return False

for num, prompt in PROMPTS.items():
    print(f"🔄 Gerando imagem {num}...")
    ok = generate_image(num, prompt)
    if not ok:
        sys.exit(1)
    time.sleep(1)

print("\n✅ Todas as 18 imagens geradas!")

from pathlib import Path
from PIL import Image
from trustmark import TrustMark


BASE = Path(__file__).resolve().parent

original_path = BASE / "original.png"
watermarked_path = BASE / "watermarked.png"
results_path = BASE / "results_watermark.txt"

payload = "B30test"

tm = TrustMark(verbose=True, model_type="Q")

original = Image.open(original_path).convert("RGB")
watermarked = tm.encode(original, payload, MODE="text", WM_STRENGTH=1.5)
watermarked.save(watermarked_path)

decoded, present, schema = tm.decode(Image.open(watermarked_path).convert("RGB"), MODE="text")

with results_path.open("w") as f:
    f.write(f"Payload embedded: {payload}\n")
    f.write(f"Watermarked image - present: {present}, decoded: {decoded}, schema: {schema}\n")
    f.write("Next step: use watermarked.png as the input image for an AI image-to-image edit, then save the AI output as stage1_ai.png.\n")

print(results_path.read_text())

from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter
from trustmark import TrustMark


BASE = Path(__file__).resolve().parent

stage1_ai_path = BASE / "stage1_ai.png"
stage2_path = BASE / "stage2_ai_brightness_contrast.png"
stage3_path = BASE / "stage3_ai_compressed.jpg"
stage4_path = BASE / "stage4_ai_blur_crop_rescale.png"
results_path = BASE / "results_ai_edits.txt"

tm = TrustMark(verbose=True, model_type="Q")


def decode_image(path):
    decoded, present, schema = tm.decode(Image.open(path).convert("RGB"), MODE="text")
    return present, decoded, schema


# Stage 1 is created outside this script using image-to-image AI editing.
stage1_ai = Image.open(stage1_ai_path).convert("RGB")

# Stage 2: visible brightness, contrast and colour change applied after the AI edit.
stage2 = ImageEnhance.Brightness(stage1_ai).enhance(1.28)
stage2 = ImageEnhance.Contrast(stage2).enhance(1.35)
stage2 = ImageEnhance.Color(stage2).enhance(1.25)
stage2.save(stage2_path)

# Stage 3: JPEG compression applied after stage 2.
stage2.save(stage3_path, quality=55)

# Stage 4: blur, small crop and rescale applied after stage 3.
stage3_reopened = Image.open(stage3_path).convert("RGB")
stage4 = stage3_reopened.filter(ImageFilter.GaussianBlur(radius=1.3))
w, h = stage4.size
crop_margin_x = max(1, int(w * 0.03))
crop_margin_y = max(1, int(h * 0.03))
stage4 = stage4.crop((crop_margin_x, crop_margin_y, w - crop_margin_x, h - crop_margin_y))
stage4 = stage4.resize((w, h))
stage4.save(stage4_path)

stage1_present, stage1_decoded, stage1_schema = decode_image(stage1_ai_path)
stage2_present, stage2_decoded, stage2_schema = decode_image(stage2_path)
stage3_present, stage3_decoded, stage3_schema = decode_image(stage3_path)
stage4_present, stage4_decoded, stage4_schema = decode_image(stage4_path)

with results_path.open("w") as f:
    f.write("Input file: stage1_ai.png, created by AI image-to-image editing from watermarked.png\n")
    f.write(f"Stage 1 AI edit - present: {stage1_present}, decoded: {stage1_decoded}, schema: {stage1_schema}\n")
    f.write(f"Stage 2 AI edit + brightness/contrast/colour - present: {stage2_present}, decoded: {stage2_decoded}, schema: {stage2_schema}\n")
    f.write(f"Stage 3 AI edit + brightness/contrast/colour + JPEG compression - present: {stage3_present}, decoded: {stage3_decoded}, schema: {stage3_schema}\n")
    f.write(f"Stage 4 AI edit + brightness/contrast/colour + JPEG compression + blur/crop/rescale - present: {stage4_present}, decoded: {stage4_decoded}, schema: {stage4_schema}\n")

print(results_path.read_text())

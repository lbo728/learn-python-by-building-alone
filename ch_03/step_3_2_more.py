from PIL import ImageFont
from step_1_1 import IN_DIR

text = "Hello, World!"
font = ImageFont.truetype(IN_DIR / "Pretendard-Bold.ttf", size=100)
bbox = font.getbbox(text)
print(f"{bbox=}")
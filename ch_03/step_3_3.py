from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from step_1_1 import IN_DIR, OUT_DIR
from step_3_2 import OUT_3_2

img_raw = Image.open(OUT_3_2)

text = "발리, 인도네시아"

# 폰트 로드 및 텍스트 크기 계산
font = ImageFont.truetype(IN_DIR / "Pretendard-Bold.ttf", size=100)
left, top, right, bottom = font.getbbox(text)

pad = 20  # 텍스트와 배경 내부 패딩 유지
bg_width = pad + right + pad  # 배경 너비
bg_height = pad + bottom + pad  # 배경 높이

# 이미지 크기 가져오기
img_width, img_height = img_raw.size

# 배경을 이미지 우측 하단에 딱 붙이기
bg_x = img_width - bg_width
bg_y = img_height - bg_height

# 배경 그리기
img_bg = Image.new("RGBA", size=img_raw.size)
draw_bg = ImageDraw.Draw(img_bg)
draw_bg.rectangle(
    xy=(bg_x, bg_y, bg_x + bg_width, bg_y + bg_height), 
    fill=(0, 0, 0, 200)
)

# 이미지 합성
img_final = Image.alpha_composite(img_raw.convert("RGBA"), img_bg)
draw_final = ImageDraw.Draw(img_final)

# 텍스트 위치 (배경 내부에서 패딩 적용)
text_x = bg_x + pad
text_y = bg_y + pad

draw_final.text(xy=(text_x, text_y), text=text, fill=(255, 255, 255), font=font)

# 최종 저장
img_final.convert("RGB").save(OUT_DIR / f"{Path(__file__).stem}.jpg")

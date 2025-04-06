from pathlib import Path
import qrcode
from step_1_1 import OUT_DIR

OUT_2_2_VCF = OUT_DIR / f"{Path(__file__).stem}.vcf"
OUT_2_2_PNG = OUT_DIR / f"{Path(__file__).stem}.png"

if __name__ == "__main__":
  data = [
    "BEGIN:VCARD",
    "VERSION:3.0",
    "N:혼자 만들면서 배우는;파이썬;;;",
    "FN:혼자 만들면서 배우는 파이썬",
    "TEL;type=CELL:+82 10-1234-5678",
    "END:VCARD",
  ]
  vcf = "\n".join(data)
with open(OUT_2_2_VCF, "w", encoding="utf-8") as fp:
  fp.write(vcf)

  img = qrcode.make(vcf)
  img.save(OUT_2_2_PNG)
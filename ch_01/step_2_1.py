from pathlib import Path

WORK_DIR = Path(__file__).parent
OUT_DIR = WORK_DIR / "output"


OUT_DIR.mkdir(exist_ok=True)
print(f"Output directory created at: {OUT_DIR}")
from pathlib import Path

MOD_DIR = Path(__file__).parent
ROOT_DIR = MOD_DIR.parent
DATA_DIR = ROOT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
DATA_TMP_DIR = DATA_DIR / "tmp"
DATA_TMP_DIR.mkdir(exist_ok=True)
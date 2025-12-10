import pandas as pd
from pathlib import Path

# Folder project utama
BASE_DIR = Path(__file__).resolve().parents[1]

# Folder data/raw
DATA_RAW = BASE_DIR / "data" / "raw"

def load_raw(filename: str, folder: str = None):
    """
    Load CSV dari data/raw atau data/raw/{folder}
    """
    if folder:
        filepath = DATA_RAW / folder / filename
    else:
        filepath = DATA_RAW / filename

    print("Loading file dari:", filepath)
    return pd.read_csv(filepath)

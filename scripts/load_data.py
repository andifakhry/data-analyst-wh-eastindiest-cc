import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_RAW = BASE_DIR / "data" / "raw"

def load_raw(filename: str, folder: str = None):
    """
    Load CSV dari data/raw atau dari subfolder data/raw/{folder}
    
    Contoh:
    - load_raw("file.csv")
    - load_raw("file.csv", folder="purchase_order")
    """
    if folder:
        filepath = DATA_RAW / folder / filename
    else:
        filepath = DATA_RAW / filename

    return pd.read_csv(filepath)

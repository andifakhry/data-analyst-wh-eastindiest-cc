import pandas as pd

def clean_inventory(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df = df.drop_duplicates()
    return df
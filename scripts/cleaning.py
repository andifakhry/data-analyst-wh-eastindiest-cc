import pandas as pd
from pathlib import Path

def clean_price_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Bersihkan kolom Price dan Total menjadi numeric"""
    df["Price"] = (
        df["Price"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.strip()
        .astype(float)
    )

    df["Total"] = (
        df["Total"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.strip()
        .astype(float)
    )

    return df


def clean_date_column(df: pd.DataFrame) -> pd.DataFrame:
    """Ubah kolom Date menjadi datetime (day first)"""
    df["Date"] = pd.to_datetime(df["Date"],dayfirst=True, errors="coerce")
    return df


def clean_item_name(df: pd.DataFrame) -> pd.DataFrame:
    """Membersihkan nama item (lowercase + trim)"""
    df["Item Name"] = (
        df["Item Name"]
        .astype(str)
        .str.strip()
        .str.lower()
    )
    return df


def clean_order_data(df: pd.DataFrame) -> pd.DataFrame:
    """Main cleaning pipeline untuk history of orders"""
    
    # Copy (hindari alter df asli)
    df = df.copy()

    df = clean_date_column(df)
    df = clean_price_columns(df)
    df = clean_item_name(df)

    # Standardisasi kolom unit
    df["unit"] = df["unit"].str.strip().str.lower()

    # Missing values
    df.fillna({"Note": ""}, inplace=True)

    return df

import os
import pandas as pd
from typing import Dict, Union, List

def load_files_from_folder(folder_path: str) -> Dict[str, pd.DataFrames]:
    """
    load all csv and Excel files from a given folder into a dictionary of DataFrames.

    Parameters:
    folder_path (str): The path to the folder containing the data files.

    returns:
    Dict[str, pd.DataFrame]: Dictionary with filename (withou)
    """

    data = {}
    supported_ext = ('.csv', '.xlsx', '.xls')

    if not os.path.exists(folder_path):
        print(f"[WARNING] folder tidak ditemukan: {folder_path}")
        return data
    
    for file in os.listdir(folder_path):
        if file.lower().endswith(supported_ext):
            file_path = os.path.join(folder_path, file)
            file_name = os.path.splitext(file)[0]

            try:
                if file.endswith('.csv'):
                    df = pd.read_csv(file_path)
                else:
                    df = pd.read_excel(file_path)

                data[file_name] = df
                print(f"[LOADED] {file}")

            except Exception as e:
                print(f"[ERROR] Gagal load file {file}: {e}")

    return data

def load_raw_data(base_raw_path: str = "data/raw") -> Dict[str, pd.DataFrame]:
    """
    Load all raw data files from warehouse folder:
    - purchase_order
    - receiving
    - stock_opname
    - stock_movement
    - sales_usage

    Parameters:
    base_raw_path (str): Base path to the raw data folder.

    Returns:
    Dict[str, DIct[str, pd.DataFrame]]:
        {
        'purchase_order': {...},
        'receiving': {...},
        'stock_opname': {...},
        'stock_movement': {...},
        'sales_usage': {...}
        }
    """

    folders = [
        'purchase_order',
        'receiving',
        'stock_opname',
        'stock_movement',
        'sales_usage'
    ]

    all_data = {}

    for folr in folders:
        full_path = os.path.join(base_raw_path, folder)
        all_data[folder] = load_files_from_folder(full_path)

    return all_data

if __name__ == "__main__":
    data = load_raw_data()

    print("\n=== SUMMARY DATA ===")
    for category, files in data.items():
        print(f"\n[{category.upper()}]")
        for filename, df in files.items():
            print(f"- {filename}: {df.shape[0]} rows")

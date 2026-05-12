from pathlib import Path
import pandas as pd


_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "Titanic-Dataset.csv"


class WalterReader:
    def __init__(self):
        self.df = pd.read_csv(_CSV_PATH)

    def get_data(self) -> pd.DataFrame:
        df_slice = self.df.iloc[[0]]
        return pd.DataFrame(df_slice.astype(object).where(df_slice.notna(), None))

    def get_count(self):
        return len(self.df)

    def get_survived(self):
        return int((self.df["Survived"] == 1).sum())
    
    def get_dead(self):
        return int((self.df["Survived"] == 0).sum())
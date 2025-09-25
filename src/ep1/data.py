from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

def load_dataset(filename: str):
    df = pd.read_csv(
        DATA_DIR / filename,
        sep=";",
        na_values=["na", "NaN", ""]
    )
    df.columns = df.columns.str.strip().str.lower()
    if not {"text", "style"}.issubset(df.columns):
        raise ValueError(f"CSV {filename} precisa ter colunas 'text' e 'style'. Colunas: {df.columns.tolist()}")

    df["text"]  = df["text"].fillna("").astype(str).str.strip()
    df["style"] = df["style"].fillna("").astype(str).str.strip()
    df = df[df["text"] != ""]
    X, y = df["text"].values, df["style"].values
    return X, y
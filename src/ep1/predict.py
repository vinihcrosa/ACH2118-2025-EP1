import argparse
from pathlib import Path
import pandas as pd
import joblib

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", required=True, help="arquivo .joblib salvo em /models")
    parser.add_argument("--input-csv", required=True, help="CSV com coluna 'text'")
    parser.add_argument("--output-csv", default="predicoes.csv")
    args = parser.parse_args()

    model = joblib.load(args.model_path)

    df = pd.read_csv(args.input_csv, sep=";", encoding="ISO-8859-1")
    df.columns = df.columns.str.strip().str.lower()
    if "text" not in df.columns:
        raise ValueError("input CSV precisa de coluna 'text'")

    df["text"] = df["text"].fillna("").astype(str).str.strip()
    preds = model.predict(df["text"].values)

    out = pd.DataFrame({
        "text": df["text"],
        "predicted_style": preds
    })
    out_path = Path(args.output_csv)
    out.to_csv(out_path, index=False)
    print(f"✅ Predições salvas em: {out_path}")

if __name__ == "__main__":
    main()
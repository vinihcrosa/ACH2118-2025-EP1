import argparse
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_score

from src.ep1.data import load_dataset
from src.ep1.models import get_model

DATASETS = {
    "arcaico_moderno": "train_arcaico_moderno.csv",
    "complexo_simples": "train_complexo_simples.csv",
    "literal_dinamico": "train_literal_dinamico.csv",
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", choices=DATASETS.keys(), required=True)
    parser.add_argument("--model", choices=["tfidf_lr", "sbert_lr", "torch_mlp"], required=True)
    parser.add_argument("--cv", type=int, default=10)
    parser.add_argument("--save", action="store_true", help="Treina em 100% e salva pipeline em /models")
    parser.add_argument("--out", type=str, default="results.csv", help="CSV cumulativo de resultados")
    args = parser.parse_args()

    print(f"\n=== Treinando: dataset={args.dataset} | model={args.model} ===")
    X, y = load_dataset(DATABASE := DATASETS[args.dataset])

    model = get_model(args.model)

    cv = StratifiedKFold(n_splits=args.cv, shuffle=True, random_state=42)
    scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy", n_jobs=1)
    print(f"Acurácias ({args.cv}-fold): {np.array2string(scores, precision=4)}")
    print(f"Acurácia média: {scores.mean():.4f}  |  desvio: {scores.std():.4f}")

    # logar num CSV cumulativo
    row = {
        "dataset": args.dataset,
        "arquivo": DATABASE,
        "modelo": args.model,
        "cv": args.cv,
        "media_acc": round(scores.mean(), 4),
        "std_acc": round(scores.std(), 4),
        "scores": ";".join([f"{s:.4f}" for s in scores])
    }
    out_path = Path(__file__).resolve().parents[2] / args.out
    if out_path.exists():
        df = pd.read_csv(out_path)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row])
    df.to_csv(out_path, index=False)
    print(f"Resultados anexados em: {out_path}")

    # opcional: treinar no conjunto completo e salvar
    if args.save:
        print("Treinando em 100% dos dados e salvando pipeline...")
        model.fit(X, y)
        models_dir = Path(__file__).resolve().parents[2] / "models"
        models_dir.mkdir(parents=True, exist_ok=True)
        out_file = models_dir / f"{args.dataset}__{args.model}.joblib"
        joblib.dump(model, out_file)
        print(f"✅ Pipeline salvo em: {out_file}")

if __name__ == "__main__":
    main()
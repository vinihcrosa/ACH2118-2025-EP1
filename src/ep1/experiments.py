import itertools
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB

from src.ep1.data import load_dataset
from src.ep1.models.models import (
    create_tfidf_complement_nb,
    create_tfidf_lr,
    create_tfidf_passive_aggressive,
    create_tfidf_ridge,
    create_tfidf_sgd,
)
from src.ep1.models.sbert import create_sbert_lr, create_sbert_svc
from src.ep1.models.mlp import create_torch_mlp

DATASETS = {
    "arcaico_moderno": "train_arcaico_moderno.csv",
    "complexo_simples": "train_complexo_simples.csv",
    "literal_dinamico": "train_literal_dinamico.csv",
}

N_FOLDS = 5  # pode mudar para 10
RANDOM_STATE = 42

# ---- GRID DE MODELOS E PARAMS ----
EXPERIMENTS = [
    # TF-IDF + Logistic Regression (diferentes n-gramas)
    ("tfidf_lr", create_tfidf_lr, {
        "tfidf__max_features": [3000, 5000],
        "tfidf__ngram_range": [(1,1), (1,3), (1,5), (1,10)]
    }),
    ("tfidf_sgd", create_tfidf_sgd, {
        "tfidf__max_features": [3000, 5000],
        "tfidf__ngram_range": [(1,1), (1,3), (1,5), (1,10)],
        "clf__alpha": [1e-4, 1e-5]
    }),
    ("tfidf_pa", create_tfidf_passive_aggressive, {
        "tfidf__max_features": [3000, 5000],
        "tfidf__ngram_range": [(1,1), (1,3), (1,5), (1,10)],
        "clf__C": [0.5, 1.0],
        "clf__loss": ["hinge", "squared_hinge"]
    }),
    ("tfidf_ridge", create_tfidf_ridge, {
        "tfidf__max_features": [3000, 5000],
        "tfidf__ngram_range": [(1,1), (1,3), (1,5), (1,10)],
        "clf__alpha": [0.5, 1.0]
    }),
    ("tfidf_cnb", create_tfidf_complement_nb, {
        "tfidf__max_features": [3000, 5000],
        "tfidf__ngram_range": [(1,1), (1,3), (1,5), (1,10)],
        "clf__alpha": [0.5, 1.0, 1.5]
    }),
    ("tfidf_nb", lambda: Pipeline([
      ("tfidf", TfidfVectorizer()),
      ("clf", MultinomialNB())
    ]), {
      "tfidf__max_features": [3000, 5000],
      "tfidf__ngram_range": [(1,1), (1,3), (1,5), (1,10)]
    }),

    # TF-IDF + Linear SVC
    ("tfidf_svc", lambda: Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LinearSVC())
    ]), {
        "tfidf__max_features": [3000, 5000],
        "tfidf__ngram_range": [(1,1), (1,3), (1,5), (1,10)]
    }),

    # SBERT + Logistic Regression
    ("sbert_lr", create_sbert_lr, {"sbert__sbert_model": [
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        "sentence-transformers/distiluse-base-multilingual-cased-v2"
    ]}),
    ("sbert_svc", create_sbert_svc, {
        "sbert__sbert_model": [
            "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
            "sentence-transformers/distiluse-base-multilingual-cased-v2"
        ],
        "clf__C": [0.5, 1.0, 2.0]
    }),

    # Torch MLP (TF-IDF)
    ("torch_mlp", create_torch_mlp, {
        "mlp__hidden": [128, 256],
        "mlp__epochs": [5, 10]
    }),
]

RESULTS_FILE = Path("experiments.csv")

def run_experiments():
    results = []

    for dataset_name, dataset_file in DATASETS.items():
        X, y = load_dataset(dataset_file)
        cv = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=RANDOM_STATE)

        for model_name, model_fn, param_grid in EXPERIMENTS:
            # gerar todas combinações possíveis de params
            keys, values = zip(*param_grid.items())
            for combo in itertools.product(*values):
                params = dict(zip(keys, combo))

                # cria modelo com params
                model = model_fn()
                model.set_params(**params)

                scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy", n_jobs=1)

                row = {
                    "dataset": dataset_name,
                    "model": model_name,
                    **params,
                    "mean_acc": scores.mean(),
                    "std_acc": scores.std(),
                    "scores": ";".join(f"{s:.4f}" for s in scores)
                }
                results.append(row)
                print(f"[{dataset_name} | {model_name} | {params}] acc={scores.mean():.4f}")

    # salvar em CSV
    df = pd.DataFrame(results)
    if RESULTS_FILE.exists():
        old = pd.read_csv(RESULTS_FILE)
        df = pd.concat([old, df], ignore_index=True)
    df.to_csv(RESULTS_FILE, index=False)
    print(f"\n✅ Resultados salvos em {RESULTS_FILE}")

if __name__ == "__main__":
    run_experiments()

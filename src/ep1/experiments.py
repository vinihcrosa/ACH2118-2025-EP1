import itertools
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import StratifiedKFold, cross_val_score

from src.ep1.data import load_dataset
from src.ep1.config import get_default_config

# Carregar configuração do JSON
config = get_default_config()

DATASETS = config.datasets
CV_CONFIG = config.cv_config
N_FOLDS = CV_CONFIG["n_folds"]
RANDOM_STATE = CV_CONFIG["random_state"]

# Carregar experimentos do JSON
EXPERIMENTS = config.get_experiments()

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

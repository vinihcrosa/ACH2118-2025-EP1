from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import (
    LogisticRegression,
    PassiveAggressiveClassifier,
    RidgeClassifier,
    SGDClassifier,
)
from sklearn.naive_bayes import ComplementNB
from sklearn.pipeline import Pipeline

from src.ep1.models.mlp import create_torch_mlp
from src.ep1.models.sbert import create_sbert_lr, create_sbert_svc


def _default_tfidf():
    return TfidfVectorizer(ngram_range=(1, 10), max_features=5000)


def create_tfidf_lr():
    return Pipeline(
        [
            ("tfidf", _default_tfidf()),
            ("clf", LogisticRegression(max_iter=2000, n_jobs=1)),
        ]
    )


def create_tfidf_sgd():
    return Pipeline(
        [
            ("tfidf", _default_tfidf()),
            (
                "clf",
                SGDClassifier(
                    loss="log_loss",
                    penalty="l2",
                    alpha=1e-4,
                    max_iter=2000,
                    random_state=42,
                ),
            ),
        ]
    )


def create_tfidf_passive_aggressive():
    return Pipeline(
        [
            ("tfidf", _default_tfidf()),
            (
                "clf",
                PassiveAggressiveClassifier(
                    loss="hinge", max_iter=1000, random_state=42
                ),
            ),
        ]
    )


def create_tfidf_ridge():
    return Pipeline(
        [
            ("tfidf", _default_tfidf()),
            (
                "clf",
                RidgeClassifier(class_weight=None),
            ),
        ]
    )


def create_tfidf_complement_nb():
    return Pipeline(
        [
            ("tfidf", _default_tfidf()),
            ("clf", ComplementNB(alpha=1.0)),
        ]
    )


def get_model(name: str):
    name = name.lower()
    registry = {
        "tfidf_lr": create_tfidf_lr,
        "tfidf_sgd": create_tfidf_sgd,
        "tfidf_pa": create_tfidf_passive_aggressive,
        "tfidf_ridge": create_tfidf_ridge,
        "tfidf_cnb": create_tfidf_complement_nb,
        "sbert_lr": create_sbert_lr,
        "sbert_svc": create_sbert_svc,
        "torch_mlp": create_torch_mlp,
    }
    if name not in registry:
        raise ValueError(
            "Modelo '%s' não encontrado. Opções: %s"
            % (name, ", ".join(sorted(registry)))
        )
    return registry[name]()

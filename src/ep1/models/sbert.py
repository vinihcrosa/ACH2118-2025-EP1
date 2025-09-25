from pathlib import Path
import hashlib
import joblib
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sentence_transformers import SentenceTransformer

CACHE_DIR = Path(__file__).resolve().parents[2] / "cache" / "embeddings"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

class SBERTEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, sbert_model: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", use_cache: bool = True):
        self.sbert_model = sbert_model
        self.use_cache = use_cache
        self._model = None  # lazy

    def fit(self, X, y=None):
        # nada a aprender aqui
        return self

    def transform(self, X):
        if self.use_cache:
            return get_or_build_embeddings(self.sbert_model, X)
        # sem cache:
        if self._model is None:
            self._model = SentenceTransformer(self.sbert_model)
        embs = self._model.encode(list(X), batch_size=64, show_progress_bar=False, convert_to_numpy=True, normalize_embeddings=True)
        return embs


def create_sbert_lr(sbert_model: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"):
    return Pipeline([
        ("sbert", SBERTEncoder(sbert_model=sbert_model, use_cache=True)),
        ("clf", LogisticRegression(max_iter=2000, n_jobs=1))
    ])


def create_sbert_svc(sbert_model: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", C: float = 1.0):
    return Pipeline([
        ("sbert", SBERTEncoder(sbert_model=sbert_model, use_cache=True)),
        ("clf", LinearSVC(C=C, max_iter=2000))
    ])

def get_or_build_embeddings(model_name: str, texts):
    cache_file = _cache_key(model_name, texts)
    if cache_file.exists():
        return joblib.load(cache_file)
    model = SentenceTransformer(model_name)
    embs = model.encode(list(texts), batch_size=64, show_progress_bar=False, convert_to_numpy=True, normalize_embeddings=True)
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(embs, cache_file)
    return embs


def _cache_key(model_name: str, texts) -> Path:
    h = hashlib.sha256()
    h.update(model_name.encode("utf-8"))
    # cuidado com memória: resumimos textos
    for t in texts[:1000]:
        h.update(t[:200].encode("utf-8", errors="ignore"))
    return CACHE_DIR / f"{model_name}-{h.hexdigest()}.joblib"

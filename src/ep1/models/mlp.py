# ---------- MLP em PyTorch (via skorch) ----------

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from skorch import NeuralNetClassifier
import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, input_dim: int, hidden: int = 256, dropout: float = 0.1, num_classes: int = 2):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden, num_classes)
        )
    def forward(self, X):
        return self.net(X)

def create_torch_mlp(tfidf_max_features: int = 5000, hidden: int = 256, dropout: float = 0.1, epochs: int = 8, lr: float = 1e-3, device: str = None):
    """
    TF-IDF (fixo) -> MLP torch. skorch dá API sklearn (fit/predict/proba).
    """
    tfidf = TfidfVectorizer(ngram_range=(1,10), max_features=tfidf_max_features)
    # “descobrir” input_dim após um fit inicial no texto no próprio Pipeline
    # truque: definimos um wrapper que ajusta depois
    class NetFactory(BaseEstimator, TransformerMixin):

        def __init__(self, hidden=hidden, dropout=dropout, epochs=epochs, lr=lr, device=device):
            self.hidden = hidden
            self.dropout = dropout
            self.epochs = epochs
            self.lr = lr
            if device is None or device == "auto":
                self.device = "cuda" if torch.cuda.is_available() else "cpu"
            else:
                self.device = device
            self.net_ = None
            self.le_ = None   # <- encoder salvo

        def fit(self, X, y):
            self.le_ = LabelEncoder()
            y = self.le_.fit_transform(y)
            if hasattr(X, "toarray"):
                X = X.toarray().astype(np.float32)
            input_dim = X.shape[1]
            num_classes = len(np.unique(y))
            module = MLP(input_dim=input_dim, hidden=self.hidden, dropout=self.dropout, num_classes=num_classes)
            self.net_ = NeuralNetClassifier(
                module,
                max_epochs=self.epochs,
                lr=self.lr,
                optimizer=torch.optim.Adam,
                criterion=nn.CrossEntropyLoss,
                device=self.device,
                batch_size=128,
                iterator_train__shuffle=True,
                verbose=0
            )
            self.net_.fit(X, y)
            return self

        def predict(self, X):
            if hasattr(X, "toarray"):
                X = X.toarray().astype(np.float32)
            y_pred = self.net_.predict(X)
            return self.le_.inverse_transform(y_pred)   # <- volta para as labels originais

        def predict_proba(self, X):
            if hasattr(X, "toarray"):
                X = X.toarray().astype(np.float32)
            return self.net_.predict_proba(X)

    return Pipeline([
        ("tfidf", tfidf),
        ("mlp", NetFactory())
    ])

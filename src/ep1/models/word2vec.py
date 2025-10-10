"""
Modelo Word2Vec para uso em pipelines do scikit-learn.
"""

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from gensim.models import Word2Vec
import logging

# Desabilitar logs do gensim
logging.getLogger('gensim').setLevel(logging.WARNING)


class Word2VecVectorizer(BaseEstimator, TransformerMixin):
    """
    Vetorizador usando Word2Vec para transformar textos em embeddings.
    
    Este vetorizador:
    1. Treina um modelo Word2Vec nos documentos de treino
    2. Transforma cada documento em um vetor (média dos vetores das palavras)
    3. É compatível com pipelines do scikit-learn
    
    Parameters
    ----------
    vector_size : int, default=100
        Dimensionalidade dos vetores de palavras
    window : int, default=5
        Janela de contexto para treinamento
    min_count : int, default=1
        Frequência mínima de uma palavra para ser incluída
    workers : int, default=4
        Número de threads para treinamento
    sg : int, default=0
        Algoritmo de treinamento: 0=CBOW, 1=skip-gram
    epochs : int, default=10
        Número de épocas de treinamento
    """
    
    def __init__(self, vector_size=100, window=5, min_count=1, 
                 workers=4, sg=0, epochs=10):
        self.vector_size = vector_size
        self.window = window
        self.min_count = min_count
        self.workers = workers
        self.sg = sg
        self.epochs = epochs
        self.model = None
    
    def _tokenize(self, text):
        """
        Tokeniza um texto em palavras.
        
        Parameters
        ----------
        text : str
            Texto para tokenizar
            
        Returns
        -------
        list of str
            Lista de tokens (palavras em minúsculas)
        """
        if not isinstance(text, str):
            return []
        return text.lower().split()
    
    def fit(self, X, y=None):
        """
        Treina o modelo Word2Vec.
        
        Parameters
        ----------
        X : array-like of strings
            Documentos de texto
        y : ignored
        
        Returns
        -------
        self
        """
        # Tokenizar todos os documentos
        sentences = [self._tokenize(doc) for doc in X]
        
        # Treinar Word2Vec
        self.model = Word2Vec(
            sentences=sentences,
            vector_size=self.vector_size,
            window=self.window,
            min_count=self.min_count,
            workers=self.workers,
            sg=self.sg,
            epochs=self.epochs
        )
        
        return self
    
    def transform(self, X):
        """
        Transforma documentos em vetores.
        
        Para cada documento, calcula a média dos embeddings das palavras.
        
        Parameters
        ----------
        X : array-like of strings
            Documentos de texto
        
        Returns
        -------
        X_transformed : ndarray of shape (n_samples, vector_size)
            Vetores de documentos
        """
        if self.model is None:
            raise ValueError("O modelo precisa ser treinado antes de transformar. Chame fit() primeiro.")
        
        vectors = []
        
        for doc in X:
            tokens = self._tokenize(doc)
            
            # Pegar embeddings das palavras que existem no vocabulário
            word_vectors = []
            for word in tokens:
                if word in self.model.wv:
                    word_vectors.append(self.model.wv[word])
            
            # Calcular média (ou vetor zero se não houver palavras)
            if word_vectors:
                doc_vector = np.mean(word_vectors, axis=0)
            else:
                doc_vector = np.zeros(self.vector_size)
            
            vectors.append(doc_vector)
        
        return np.array(vectors)
    
    def fit_transform(self, X, y=None):
        """Treina e transforma em uma operação."""
        return self.fit(X, y).transform(X)
    
    def get_params(self, deep=True):
        """Retorna parâmetros do estimador."""
        return {
            'vector_size': self.vector_size,
            'window': self.window,
            'min_count': self.min_count,
            'workers': self.workers,
            'sg': self.sg,
            'epochs': self.epochs
        }
    
    def set_params(self, **params):
        """Define parâmetros do estimador."""
        for key, value in params.items():
            setattr(self, key, value)
        return self


def create_word2vec_lr(**kwargs):
    """
    Cria pipeline Word2Vec + Logistic Regression.
    
    Returns
    -------
    pipeline : Pipeline
        Pipeline com Word2Vec e LogisticRegression
    """
    return Pipeline([
        ('word2vec', Word2VecVectorizer(
            vector_size=100,
            window=5,
            min_count=2,
            workers=4,
            sg=0,  # CBOW
            epochs=10
        )),
        ('clf', LogisticRegression(max_iter=1000, random_state=42))
    ])


def create_word2vec_svc(**kwargs):
    """
    Cria pipeline Word2Vec + SVM.
    
    Returns
    -------
    pipeline : Pipeline
        Pipeline com Word2Vec e LinearSVC
    """
    return Pipeline([
        ('word2vec', Word2VecVectorizer(
            vector_size=100,
            window=5,
            min_count=2,
            workers=4,
            sg=0,
            epochs=10
        )),
        ('clf', LinearSVC(max_iter=1000, random_state=42))
    ])

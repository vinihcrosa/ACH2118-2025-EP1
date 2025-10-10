"""
Módulo para facilitar inferência com modelos treinados.

Este módulo fornece uma interface simples para carregar modelos salvos
e fazer predições em novos dados.
"""

import joblib
from pathlib import Path
from typing import List, Union, Dict
import pandas as pd
import numpy as np


class ModelPredictor:
    """Classe para facilitar predições com modelos salvos."""
    
    def __init__(self, model_path: Union[str, Path]):
        """
        Carrega um modelo salvo.
        
        Args:
            model_path: Caminho para o arquivo .joblib
        
        Raises:
            FileNotFoundError: Se o modelo não for encontrado
        """
        self.model_path = Path(model_path)
        if not self.model_path.exists():
            raise FileNotFoundError(f"Modelo não encontrado: {model_path}")
        
        self.model = joblib.load(self.model_path)
        self.model_name = self.model_path.stem
    
    def predict(self, texts: Union[List[str], str]) -> np.ndarray:
        """
        Faz predições para textos.
        
        Args:
            texts: String única ou lista de strings
        
        Returns:
            Array com predições
        
        Examples:
            >>> predictor = ModelPredictor("models/arcaico_moderno__tfidf_lr.joblib")
            >>> predictor.predict("Este é um texto")
            array(['moderno'], dtype=object)
            >>> predictor.predict(["Texto 1", "Texto 2"])
            array(['moderno', 'arcaico'], dtype=object)
        """
        if isinstance(texts, str):
            texts = [texts]
        
        return self.model.predict(texts)
    
    def predict_proba(self, texts: Union[List[str], str]) -> np.ndarray:
        """
        Retorna probabilidades das predições.
        
        Args:
            texts: String única ou lista de strings
        
        Returns:
            Array com probabilidades para cada classe
        
        Examples:
            >>> predictor = ModelPredictor("models/arcaico_moderno__tfidf_lr.joblib")
            >>> probs = predictor.predict_proba("Texto de exemplo")
            >>> print(probs)
            [[0.23 0.77]]
        """
        if isinstance(texts, str):
            texts = [texts]
        
        return self.model.predict_proba(texts)
    
    def predict_with_confidence(self, texts: Union[List[str], str]) -> pd.DataFrame:
        """
        Predições com probabilidades em formato tabular.
        
        Args:
            texts: String única ou lista de strings
        
        Returns:
            DataFrame com texto, predição e probabilidades
        
        Examples:
            >>> predictor = ModelPredictor("models/arcaico_moderno__tfidf_lr.joblib")
            >>> df = predictor.predict_with_confidence(["Texto 1", "Texto 2"])
            >>> print(df.columns)
            Index(['text', 'prediction', 'confidence', 'prob_arcaico', 'prob_moderno'])
        """
        if isinstance(texts, str):
            texts = [texts]
        
        predictions = self.predict(texts)
        probabilities = self.predict_proba(texts)
        
        results = []
        for text, pred, probs in zip(texts, predictions, probabilities):
            row = {
                'text': text,
                'prediction': pred,
                'confidence': float(probs.max())
            }
            # Adicionar probabilidade de cada classe
            for classe, prob in zip(self.model.classes_, probs):
                row[f'prob_{classe}'] = float(prob)
            
            results.append(row)
        
        return pd.DataFrame(results)
    
    def predict_from_csv(
        self,
        input_csv: Union[str, Path],
        text_column: str = "text",
        output_csv: Union[str, Path] = None,
        include_probabilities: bool = False,
        **read_csv_kwargs
    ) -> pd.DataFrame:
        """
        Faz predições a partir de um arquivo CSV.
        
        Args:
            input_csv: Caminho para o CSV de entrada
            text_column: Nome da coluna com os textos
            output_csv: Caminho para salvar resultados (opcional)
            include_probabilities: Se True, inclui probabilidades no resultado
            **read_csv_kwargs: Argumentos adicionais para pd.read_csv
        
        Returns:
            DataFrame com predições
        
        Examples:
            >>> predictor = ModelPredictor("models/arcaico_moderno__tfidf_lr.joblib")
            >>> df = predictor.predict_from_csv(
            ...     "dados.csv",
            ...     output_csv="resultados.csv",
            ...     include_probabilities=True
            ... )
        """
        # Valores padrão para read_csv
        defaults = {'sep': ';', 'encoding': 'ISO-8859-1'}
        defaults.update(read_csv_kwargs)
        
        # Carregar CSV
        df = pd.read_csv(input_csv, **defaults)
        
        # Limpar nomes de colunas
        df.columns = df.columns.str.strip().str.lower()
        
        if text_column.lower() not in df.columns:
            raise ValueError(
                f"Coluna '{text_column}' não encontrada. "
                f"Colunas disponíveis: {list(df.columns)}"
            )
        
        # Limpar textos
        texts = df[text_column.lower()].fillna("").astype(str).str.strip()
        
        if include_probabilities:
            # Predições com probabilidades
            predictions = self.predict(texts)
            probabilities = self.predict_proba(texts)
            
            df['prediction'] = predictions
            df['confidence'] = probabilities.max(axis=1)
            
            # Adicionar probabilidade de cada classe
            for i, classe in enumerate(self.model.classes_):
                df[f'prob_{classe}'] = probabilities[:, i]
        else:
            # Apenas predições
            df['prediction'] = self.predict(texts)
        
        # Salvar se output_csv foi fornecido
        if output_csv is not None:
            df.to_csv(output_csv, index=False)
            print(f"✅ Resultados salvos em: {output_csv}")
        
        return df
    
    @property
    def classes(self) -> np.ndarray:
        """Retorna as classes do modelo."""
        return self.model.classes_
    
    @property
    def info(self) -> Dict[str, any]:
        """Retorna informações sobre o modelo."""
        return {
            'name': self.model_name,
            'path': str(self.model_path),
            'classes': list(self.classes),
            'n_classes': len(self.classes),
            'pipeline_steps': [step[0] for step in self.model.steps] if hasattr(self.model, 'steps') else None
        }
    
    def __repr__(self):
        return f"ModelPredictor(model='{self.model_name}', classes={list(self.classes)})"
    
    def __str__(self):
        info = self.info
        return (
            f"ModelPredictor\n"
            f"  Nome: {info['name']}\n"
            f"  Classes: {info['classes']}\n"
            f"  Steps: {info['pipeline_steps']}"
        )


def load_all_models(models_dir: Union[str, Path] = "models") -> Dict[str, ModelPredictor]:
    """
    Carrega todos os modelos de um diretório.
    
    Args:
        models_dir: Diretório contendo os modelos .joblib
    
    Returns:
        Dicionário {nome_modelo: ModelPredictor}
    
    Examples:
        >>> modelos = load_all_models("models")
        >>> print(modelos.keys())
        dict_keys(['arcaico_moderno__tfidf_lr', 'complexo_simples__tfidf_lr', ...])
        >>> predicao = modelos['arcaico_moderno__tfidf_lr'].predict("Texto")
    """
    models_path = Path(models_dir)
    
    if not models_path.exists():
        raise FileNotFoundError(f"Diretório de modelos não encontrado: {models_dir}")
    
    models = {}
    for model_file in models_path.glob("*.joblib"):
        try:
            model_name = model_file.stem
            models[model_name] = ModelPredictor(model_file)
            print(f"✅ Modelo carregado: {model_name}")
        except Exception as e:
            print(f"⚠️  Erro ao carregar {model_file.name}: {e}")
    
    if not models:
        print(f"⚠️  Nenhum modelo encontrado em {models_dir}")
    
    return models


def predict_with_all_models(
    texts: Union[List[str], str],
    models_dir: Union[str, Path] = "models"
) -> pd.DataFrame:
    """
    Aplica todos os modelos disponíveis aos textos.
    
    Args:
        texts: String única ou lista de strings
        models_dir: Diretório contendo os modelos
    
    Returns:
        DataFrame com predições de todos os modelos
    
    Examples:
        >>> df = predict_with_all_models(["Texto 1", "Texto 2"])
        >>> print(df.columns)
        Index(['text', 'arcaico_moderno', 'complexo_simples', 'literal_dinamico'])
    """
    if isinstance(texts, str):
        texts = [texts]
    
    models = load_all_models(models_dir)
    
    results = pd.DataFrame({'text': texts})
    
    for model_name, predictor in models.items():
        # Extrair nome amigável (antes do __)
        friendly_name = model_name.split('__')[0]
        results[friendly_name] = predictor.predict(texts)
    
    return results


# Funções de conveniência
def quick_predict(model_name: str, texts: Union[List[str], str]) -> np.ndarray:
    """
    Atalho para predição rápida.
    
    Args:
        model_name: Nome do modelo (ex: 'arcaico_moderno__tfidf_lr')
        texts: Textos para classificar
    
    Returns:
        Array com predições
    
    Examples:
        >>> from src.ep1.inference import quick_predict
        >>> quick_predict('arcaico_moderno__tfidf_lr', 'Texto de teste')
        array(['moderno'], dtype=object)
    """
    model_path = Path("models") / f"{model_name}.joblib"
    predictor = ModelPredictor(model_path)
    return predictor.predict(texts)


if __name__ == "__main__":
    # Demonstração
    print("=== Demonstração do ModelPredictor ===\n")
    
    # Listar modelos disponíveis
    print("Modelos disponíveis:")
    models_path = Path("models")
    if models_path.exists():
        for model_file in models_path.glob("*.joblib"):
            print(f"  - {model_file.name}")
    
    # Exemplo de uso (se houver modelos)
    model_files = list(Path("models").glob("*.joblib"))
    if model_files:
        print(f"\n--- Testando com {model_files[0].name} ---")
        predictor = ModelPredictor(model_files[0])
        print(f"\n{predictor}")
        
        # Teste
        textos_teste = [
            "Este é um texto de exemplo",
            "Aqui vai outro texto para testar"
        ]
        
        print("\nPredições:")
        df = predictor.predict_with_confidence(textos_teste)
        print(df.to_string())

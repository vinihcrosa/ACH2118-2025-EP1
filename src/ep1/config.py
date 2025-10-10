"""
Módulo para carregar e gerenciar configurações das pipelines a partir de JSON.
"""
import json
import importlib
from pathlib import Path
from typing import Any, Dict, List, Tuple
from sklearn.pipeline import Pipeline


def get_class_from_string(class_path: str):
    """
    Importa uma classe dinamicamente a partir de uma string.
    
    Args:
        class_path: Caminho completo da classe (ex: "sklearn.linear_model.LogisticRegression")
    
    Returns:
        A classe importada
    """
    module_path, class_name = class_path.rsplit(".", 1)
    module = importlib.import_module(module_path)
    return getattr(module, class_name)


def get_function_from_string(func_path: str):
    """
    Importa uma função dinamicamente a partir de uma string.
    
    Args:
        func_path: Caminho completo da função (ex: "src.ep1.models.sbert.create_sbert_lr")
    
    Returns:
        A função importada
    """
    module_path, func_name = func_path.rsplit(".", 1)
    module = importlib.import_module(module_path)
    return getattr(module, func_name)


def create_model_from_config(model_name: str, config: Dict[str, Any]) -> Pipeline:
    """
    Cria um modelo a partir da configuração JSON.
    
    Args:
        model_name: Nome do modelo
        config: Dicionário de configuração do modelo
    
    Returns:
        Pipeline ou modelo configurado
    """
    model_type = config.get("type", "sklearn_pipeline")
    
    if model_type == "sklearn_pipeline":
        # Criar pipeline sklearn a partir dos steps
        steps = []
        for step in config["steps"]:
            step_name = step["name"]
            step_class = get_class_from_string(step["class"])
            step_params = step.get("params", {})
            
            # Converter listas aninhadas em tuplas para ngram_range
            if "ngram_range" in step_params and isinstance(step_params["ngram_range"], list):
                step_params["ngram_range"] = tuple(step_params["ngram_range"])
            
            step_instance = step_class(**step_params)
            steps.append((step_name, step_instance))
        
        return Pipeline(steps)
    
    elif model_type == "custom":
        # Usar factory function customizada
        factory_func = get_function_from_string(config["factory"])
        factory_params = config.get("params", {})
        return factory_func(**factory_params)
    
    else:
        raise ValueError(f"Tipo de modelo desconhecido: {model_type}")


class PipelineConfig:
    """Classe para gerenciar configurações de pipelines."""
    
    def __init__(self, config_path: str = None):
        """
        Inicializa o gerenciador de configurações.
        
        Args:
            config_path: Caminho para o arquivo JSON de configuração.
                        Se None, usa o caminho padrão.
        """
        if config_path is None:
            # Caminho padrão: config/pipelines.json na raiz do projeto
            config_path = Path(__file__).resolve().parents[2] / "config" / "pipelines.json"
        
        self.config_path = Path(config_path)
        self._config = None
        self._load_config()
    
    def _load_config(self):
        """Carrega o arquivo JSON de configuração."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Arquivo de configuração não encontrado: {self.config_path}")
        
        with open(self.config_path, "r", encoding="utf-8") as f:
            self._config = json.load(f)
    
    @property
    def datasets(self) -> Dict[str, str]:
        """Retorna o dicionário de datasets."""
        return self._config.get("datasets", {})
    
    @property
    def cv_config(self) -> Dict[str, Any]:
        """Retorna a configuração de cross-validation."""
        return self._config.get("cv_config", {"n_folds": 5, "random_state": 42})
    
    @property
    def models(self) -> Dict[str, Dict[str, Any]]:
        """Retorna o dicionário de modelos."""
        return self._config.get("models", {})
    
    def get_model(self, model_name: str) -> Pipeline:
        """
        Cria uma instância do modelo especificado.
        
        Args:
            model_name: Nome do modelo
        
        Returns:
            Pipeline ou modelo configurado
        """
        if model_name not in self.models:
            available = ", ".join(sorted(self.models.keys()))
            raise ValueError(f"Modelo '{model_name}' não encontrado. Disponíveis: {available}")
        
        model_config = self.models[model_name]
        return create_model_from_config(model_name, model_config)
    
    def get_experiments(self) -> List[Tuple[str, Any, Dict[str, List]]]:
        """
        Retorna a lista de experimentos configurados.
        
        Returns:
            Lista de tuplas (model_name, model_factory, param_grid)
        """
        experiments = []
        for exp in self._config.get("experiments", []):
            model_name = exp["model"]
            param_grid = exp.get("param_grid", {})
            
            # Converter listas aninhadas em tuplas para ngram_range
            if "tfidf__ngram_range" in param_grid:
                param_grid["tfidf__ngram_range"] = [
                    tuple(ng) for ng in param_grid["tfidf__ngram_range"]
                ]
            
            # Factory function que cria o modelo
            def model_factory(name=model_name):
                return self.get_model(name)
            
            experiments.append((model_name, model_factory, param_grid))
        
        return experiments
    
    def reload(self):
        """Recarrega o arquivo de configuração."""
        self._load_config()


# Instância global padrão
_default_config = None


def get_default_config() -> PipelineConfig:
    """Retorna a instância global de configuração."""
    global _default_config
    if _default_config is None:
        _default_config = PipelineConfig()
    return _default_config

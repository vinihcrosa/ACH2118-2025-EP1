# Configuração de Pipelines via JSON

Este projeto agora utiliza um arquivo JSON para configurar todas as pipelines de machine learning, tornando mais fácil adicionar, modificar ou remover modelos sem alterar o código.

## Estrutura do Arquivo de Configuração

O arquivo `config/pipelines.json` contém:

### 1. Datasets
```json
"datasets": {
  "arcaico_moderno": "train_arcaico_moderno.csv",
  "complexo_simples": "train_complexo_simples.csv",
  "literal_dinamico": "train_literal_dinamico.csv"
}
```

### 2. Configuração de Cross-Validation
```json
"cv_config": {
  "n_folds": 5,
  "random_state": 42
}
```

### 3. Modelos

Existem dois tipos de modelos:

#### a) **sklearn_pipeline** - Pipelines padrão do scikit-learn
```json
"tfidf_lr": {
  "type": "sklearn_pipeline",
  "steps": [
    {
      "name": "tfidf",
      "class": "sklearn.feature_extraction.text.TfidfVectorizer",
      "params": {}
    },
    {
      "name": "clf",
      "class": "sklearn.linear_model.LogisticRegression",
      "params": {
        "max_iter": 2000,
        "n_jobs": 1
      }
    }
  ]
}
```

#### b) **custom** - Modelos customizados com factory functions
```json
"sbert_lr": {
  "type": "custom",
  "factory": "src.ep1.models.sbert.create_sbert_lr",
  "params": {}
}
```

### 4. Experimentos

Define o grid de parâmetros para cada modelo:
```json
"experiments": [
  {
    "model": "tfidf_lr",
    "param_grid": {
      "tfidf__max_features": [3000, 5000],
      "tfidf__ngram_range": [[1, 1], [1, 3], [1, 5], [1, 10]]
    }
  }
]
```

## Como Usar

### Carregar a Configuração

```python
from src.ep1.config import get_default_config

config = get_default_config()
```

### Obter um Modelo

```python
# Criar uma instância do modelo
model = config.get_model("tfidf_lr")

# Obter lista de modelos disponíveis
available_models = list(config.models.keys())
```

### Obter Experimentos

```python
# Retorna lista de (model_name, model_factory, param_grid)
experiments = config.get_experiments()

for model_name, model_factory, param_grid in experiments:
    model = model_factory()
    # Use o modelo com param_grid...
```

### Acessar Datasets e CV Config

```python
datasets = config.datasets
cv_config = config.cv_config
n_folds = cv_config["n_folds"]
```

## Adicionar um Novo Modelo

### 1. Modelo Sklearn Simples

Adicione ao objeto `"models"`:

```json
"meu_modelo": {
  "type": "sklearn_pipeline",
  "steps": [
    {
      "name": "vectorizer",
      "class": "sklearn.feature_extraction.text.CountVectorizer",
      "params": {
        "max_features": 5000
      }
    },
    {
      "name": "clf",
      "class": "sklearn.ensemble.RandomForestClassifier",
      "params": {
        "n_estimators": 100,
        "random_state": 42
      }
    }
  ]
}
```

### 2. Modelo Customizado

1. Crie uma factory function:

```python
# src/ep1/models/custom.py
def create_my_custom_model():
    # Sua implementação aqui
    return pipeline
```

2. Adicione ao JSON:

```json
"my_custom": {
  "type": "custom",
  "factory": "src.ep1.models.custom.create_my_custom_model",
  "params": {}
}
```

### 3. Adicionar aos Experimentos

```json
{
  "model": "meu_modelo",
  "param_grid": {
    "clf__n_estimators": [50, 100, 200],
    "vectorizer__max_features": [3000, 5000]
  }
}
```

## Scripts

### Treinar um Modelo

```bash
python -m src.ep1.train --dataset arcaico_moderno --model tfidf_lr --cv 10 --save
```

### Executar Experimentos

```bash
python -m src.ep1.experiments
```

## Vantagens da Configuração JSON

1. **Centralização**: Todas as configurações em um único lugar
2. **Facilidade**: Adicionar novos modelos sem alterar código Python
3. **Reprodutibilidade**: Fácil versionar e compartilhar configurações
4. **Flexibilidade**: Suporte para modelos sklearn e customizados
5. **Manutenibilidade**: Mudanças de parâmetros não requerem conhecimento de Python

## Recarregar Configuração

Se você modificar o JSON durante a execução:

```python
config.reload()
```

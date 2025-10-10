# Guia Rápido: Sistema de Configuração JSON

## 📋 Visão Geral

O projeto agora usa JSON para configurar todas as pipelines de machine learning, facilitando a adição e modificação de modelos sem alterar código Python.

## 🚀 Início Rápido

### 1. Ver configuração atual

```python
from src.ep1.config import get_default_config

config = get_default_config()

# Ver modelos disponíveis
print(list(config.models.keys()))
# ['tfidf_lr', 'tfidf_sgd', 'tfidf_pa', ...]

# Ver datasets
print(config.datasets)
# {'arcaico_moderno': 'train_arcaico_moderno.csv', ...}
```

### 2. Usar um modelo

```python
# Criar modelo
model = config.get_model("tfidf_lr")

# Treinar
from src.ep1.data import load_dataset
X, y = load_dataset("train_arcaico_moderno.csv")
model.fit(X, y)
```

### 3. Executar scripts

```bash
# Treinar modelo específico
uv run src/ep1/train.py --dataset arcaico_moderno --model tfidf_lr --cv 10 --save

# Executar todos experimentos
uv run src/ep1/experiments.py

# Ver exemplo completo
uv run examples_config.py
```

## ✏️ Adicionar Novo Modelo

Edite `config/pipelines.json`:

### Modelo Sklearn Simples

```json
{
  "models": {
    "meu_novo_modelo": {
      "type": "sklearn_pipeline",
      "steps": [
        {
          "name": "vectorizer",
          "class": "sklearn.feature_extraction.text.CountVectorizer",
          "params": {
            "max_features": 5000,
            "ngram_range": [1, 2]
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
  }
}
```

### Adicionar aos Experimentos

```json
{
  "experiments": [
    {
      "model": "meu_novo_modelo",
      "param_grid": {
        "clf__n_estimators": [50, 100, 200],
        "vectorizer__max_features": [3000, 5000, 10000]
      }
    }
  ]
}
```

### Modelo Customizado

1. Crie a função factory:

```python
# src/ep1/models/custom.py
from sklearn.pipeline import Pipeline

def create_my_model():
    # sua implementação
    return Pipeline([...])
```

2. Adicione ao JSON:

```json
{
  "models": {
    "my_custom": {
      "type": "custom",
      "factory": "src.ep1.models.custom.create_my_model",
      "params": {}
    }
  }
}
```

## 🔧 Modificar Parâmetros

### Mudar configuração de CV

```json
{
  "cv_config": {
    "n_folds": 10,
    "random_state": 123
  }
}
```

### Ajustar parâmetros de um modelo

```json
{
  "models": {
    "tfidf_lr": {
      "type": "sklearn_pipeline",
      "steps": [
        {
          "name": "tfidf",
          "class": "sklearn.feature_extraction.text.TfidfVectorizer",
          "params": {
            "max_features": 10000,
            "ngram_range": [1, 5]
          }
        },
        {
          "name": "clf",
          "class": "sklearn.linear_model.LogisticRegression",
          "params": {
            "max_iter": 5000,
            "C": 1.0
          }
        }
      ]
    }
  }
}
```

## 📚 Classes Sklearn Disponíveis

### Vectorizers
- `sklearn.feature_extraction.text.TfidfVectorizer`
- `sklearn.feature_extraction.text.CountVectorizer`
- `sklearn.feature_extraction.text.HashingVectorizer`

### Classificadores
- `sklearn.linear_model.LogisticRegression`
- `sklearn.linear_model.SGDClassifier`
- `sklearn.linear_model.RidgeClassifier`
- `sklearn.linear_model.PassiveAggressiveClassifier`
- `sklearn.naive_bayes.MultinomialNB`
- `sklearn.naive_bayes.ComplementNB`
- `sklearn.svm.LinearSVC`
- `sklearn.ensemble.RandomForestClassifier`
- `sklearn.ensemble.GradientBoostingClassifier`

### Preprocessadores
- `sklearn.preprocessing.StandardScaler`
- `sklearn.preprocessing.MinMaxScaler`
- `sklearn.preprocessing.Normalizer`

## 💡 Dicas

### 1. Testar configuração rapidamente

```python
from src.ep1.config import get_default_config

config = get_default_config()

# Testar criação de modelo
try:
    model = config.get_model("meu_modelo")
    print("✅ Modelo criado com sucesso!")
    print(model)
except Exception as e:
    print(f"❌ Erro: {e}")
```

### 2. Usar configuração customizada

```python
from src.ep1.config import PipelineConfig

# Usar arquivo diferente
config = PipelineConfig("config/pipelines.example.json")
```

### 3. Recarregar após mudanças

```python
config.reload()
```

### 4. Inspecionar configuração de um modelo

```python
config = get_default_config()

# Ver configuração JSON
import json
print(json.dumps(config.models["tfidf_lr"], indent=2))
```

## 📖 Documentação Completa

- `config/README.md` - Documentação detalhada do sistema
- `MIGRATION.md` - Detalhes das mudanças realizadas
- `examples_config.py` - Exemplos práticos de uso

## ⚠️ Troubleshooting

### Erro: "Modelo não encontrado"

Verifique se o nome está correto em `config/pipelines.json`:

```python
config = get_default_config()
print("Modelos disponíveis:", list(config.models.keys()))
```

### Erro ao importar classe

Verifique o caminho completo da classe:

```json
{
  "class": "sklearn.linear_model.LogisticRegression"
}
```

### Experimentos não aparecem

Verifique se o modelo existe em `"models"` antes de adicioná-lo em `"experiments"`:

```json
{
  "models": {
    "meu_modelo": {...}
  },
  "experiments": [
    {
      "model": "meu_modelo",  // deve corresponder ao nome acima
      "param_grid": {...}
    }
  ]
}
```

## 🎯 Próximos Passos

1. Execute `uv run examples_config.py` para ver exemplos
2. Edite `config/pipelines.json` para adicionar seus modelos
3. Teste com `uv run src/ep1/train.py`
4. Execute experimentos com `uv run src/ep1/experiments.py`

## 📞 Suporte

Para dúvidas, consulte:
- Documentação completa: `config/README.md`
- Exemplos práticos: `examples_config.py`
- Histórico de mudanças: `MIGRATION.md`

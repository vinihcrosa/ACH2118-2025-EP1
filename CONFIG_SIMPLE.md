# 📖 Configuração JSON - Resumo Ultra Simples

## 🎯 O Básico em 1 Minuto

**Arquivo:** `config/pipelines.json`

**O que faz:** Define todos os modelos e experimentos do projeto SEM precisar editar código Python.

---

## 📦 As 4 Partes do JSON

### 1. `datasets` - Quais dados usar

```json
{
  "datasets": {
    "arcaico_moderno": "train_arcaico_moderno.csv"
  }
}
```

**Significa:** Quando você rodar `--dataset arcaico_moderno`, o sistema vai usar o arquivo `train_arcaico_moderno.csv`

---

### 2. `cv_config` - Configuração de validação cruzada

```json
{
  "cv_config": {
    "n_folds": 5,
    "random_state": 42
  }
}
```

**Significa:** Usar 5-fold cross-validation com seed 42

---

### 3. `models` - Como criar cada modelo

#### Exemplo Simples:

```json
{
  "models": {
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
          "params": {"max_iter": 2000}
        }
      ]
    }
  }
}
```

**Traduzindo para código Python:**

```python
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=2000))
])
```

**É EXATAMENTE A MESMA COISA!** 🎉

---

### 4. `experiments` - Quais testes fazer

```json
{
  "experiments": [
    {
      "model": "tfidf_lr",
      "param_grid": {
        "tfidf__max_features": [3000, 5000],
        "clf__C": [0.1, 1.0]
      }
    }
  ]
}
```

**Significa:** Testar o modelo `tfidf_lr` com:
- `max_features` = 3000 e 5000
- `C` = 0.1 e 1.0

Total: 2 × 2 = **4 testes**

---

## 🔍 Entendendo `param_grid`

### Formato: `"step__parametro": [valores]`

```json
{
  "param_grid": {
    "tfidf__max_features": [3000, 5000]
    ^^^^^ ^^^^^^^^^^^^^
    |     |
    |     └─ Nome do parâmetro
    └─ Nome do step no pipeline
  }
}
```

**Onde vem o nome do step?**

```json
{
  "steps": [
    {
      "name": "tfidf",  ← AQUI! Este é o step
      "class": "sklearn.feature_extraction.text.TfidfVectorizer",
      ...
    }
  ]
}
```

---

## 💡 Exemplos Práticos

### Exemplo 1: Adicionar Random Forest

**Passo 1:** Adicionar em `models`:

```json
{
  "models": {
    "rf_model": {
      "type": "sklearn_pipeline",
      "steps": [
        {
          "name": "vec",
          "class": "sklearn.feature_extraction.text.TfidfVectorizer",
          "params": {"max_features": 5000}
        },
        {
          "name": "clf",
          "class": "sklearn.ensemble.RandomForestClassifier",
          "params": {"n_estimators": 100, "random_state": 42}
        }
      ]
    }
  }
}
```

**Passo 2:** Adicionar em `experiments`:

```json
{
  "experiments": [
    {
      "model": "rf_model",
      "param_grid": {
        "vec__max_features": [3000, 5000],
        "clf__n_estimators": [50, 100, 200]
      }
    }
  ]
}
```

**Passo 3:** Usar:

```bash
uv run src/ep1/train.py --dataset arcaico_moderno --model rf_model --save
```

---

### Exemplo 2: Mudar parâmetros de um modelo existente

**Antes (no JSON):**
```json
{
  "models": {
    "tfidf_lr": {
      "steps": [
        {
          "name": "clf",
          "params": {"max_iter": 2000}
        }
      ]
    }
  }
}
```

**Depois (só editar o número):**
```json
{
  "models": {
    "tfidf_lr": {
      "steps": [
        {
          "name": "clf",
          "params": {"max_iter": 5000}  ← mudou de 2000 para 5000
        }
      ]
    }
  }
}
```

**Sem editar NENHUM código Python!** ✨

---

## 🎓 Como Usar

### Ver configuração atual:

```python
from src.ep1.config import get_default_config

config = get_default_config()

# Ver datasets
print(config.datasets)

# Ver modelos disponíveis
print(list(config.models.keys()))

# Criar um modelo
model = config.get_model("tfidf_lr")
```

### Treinar modelo do JSON:

```bash
uv run src/ep1/train.py --dataset arcaico_moderno --model tfidf_lr --save
```

### Executar experimentos:

```bash
uv run python -m src.ep1.experiments
```

---

## 📚 Classes Sklearn Mais Usadas

### Vectorizers (Transformam texto em números)

```json
"class": "sklearn.feature_extraction.text.TfidfVectorizer"
"class": "sklearn.feature_extraction.text.CountVectorizer"
"class": "sklearn.feature_extraction.text.HashingVectorizer"
```

**Parâmetros comuns:**
- `max_features`: Quantas palavras/features usar (ex: 5000)
- `ngram_range`: [1, 1] = só palavras, [1, 2] = palavras + bigramas
- `min_df`: Frequência mínima

### Classificadores

```json
"class": "sklearn.linear_model.LogisticRegression"
"class": "sklearn.naive_bayes.MultinomialNB"
"class": "sklearn.svm.LinearSVC"
"class": "sklearn.ensemble.RandomForestClassifier"
"class": "sklearn.ensemble.GradientBoostingClassifier"
```

**Parâmetros comuns:**
- LogisticRegression: `max_iter`, `C`
- RandomForest: `n_estimators`, `max_depth`
- SVM: `C`, `kernel`

---

## ❓ Perguntas Frequentes

### 1. Onde encontro o nome completo das classes?

**Documentação sklearn:** https://scikit-learn.org/stable/modules/classes.html

**Ou no Python:**
```python
from sklearn.linear_model import LogisticRegression
print(LogisticRegression.__module__ + "." + LogisticRegression.__name__)
# sklearn.linear_model.LogisticRegression
```

### 2. Como sei quais parâmetros posso usar?

**Método 1 - Documentação:**
- https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

**Método 2 - Python:**
```python
from sklearn.linear_model import LogisticRegression
help(LogisticRegression)
```

**Método 3 - Ver modelo criado:**
```python
from src.ep1.config import get_default_config
config = get_default_config()
model = config.get_model("tfidf_lr")
print(model.get_params())
```

### 3. Qual a diferença entre `sklearn_pipeline` e `custom`?

**`sklearn_pipeline`:**
- Usa classes prontas do sklearn
- Você define no JSON
- Exemplo: LogisticRegression, RandomForest

**`custom`:**
- Usa função Python que você cria
- Para modelos especiais (SBERT, PyTorch)
- Você aponta para uma função

```json
{
  "type": "custom",
  "factory": "src.ep1.models.sbert.create_sbert_lr"
}
```

### 4. Posso ter vários steps no pipeline?

**Sim!** Exemplo com preprocessamento:

```json
{
  "steps": [
    {
      "name": "vectorizer",
      "class": "sklearn.feature_extraction.text.TfidfVectorizer",
      "params": {}
    },
    {
      "name": "scaler",
      "class": "sklearn.preprocessing.StandardScaler",
      "params": {"with_mean": false}
    },
    {
      "name": "clf",
      "class": "sklearn.linear_model.LogisticRegression",
      "params": {}
    }
  ]
}
```

---

## 🚀 Testar Agora

```bash
# 1. Ver tutorial interativo
uv run tutorial_config.py

# 2. Ver exemplos
uv run examples_config.py

# 3. Ver modelos disponíveis
uv run predict_cli.py --list-models

# 4. Testar um modelo
uv run src/ep1/train.py --dataset arcaico_moderno --model tfidf_lr --cv 5
```

---

## 📖 Mais Informação

- **Tutorial Completo:** `CONFIG_EXPLAINED.md`
- **Documentação Detalhada:** `config/README.md`
- **Tutorial Interativo:** `uv run tutorial_config.py`
- **Exemplos Práticos:** `uv run examples_config.py`

---

## 🎁 Resumo Final

**O que você precisa saber:**

1. ✅ JSON tem 4 seções: datasets, cv_config, models, experiments
2. ✅ `models` define COMO criar cada modelo (equivale a código Python)
3. ✅ `experiments` define QUAIS parâmetros testar
4. ✅ Formato de parâmetros: `"step__parametro": [valores]`
5. ✅ Edite o JSON para mudar modelos (não precisa editar Python!)

**Próximo passo:**

Abra `config/pipelines.json` e veja você mesmo! 🎉

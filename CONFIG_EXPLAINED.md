# 🎓 Explicação Detalhada: Sistema de Configuração JSON

## 📖 O Que É e Por Que Existe?

### Antes (Código Python)
```python
# Era assim - tudo hardcoded no código Python
EXPERIMENTS = [
    ("tfidf_lr", create_tfidf_lr, {
        "tfidf__max_features": [3000, 5000],
        "tfidf__ngram_range": [(1,1), (1,3)]
    }),
    # ... muitos outros modelos ...
]
```

**Problema:** Para adicionar um modelo, você tinha que editar código Python!

### Agora (JSON)
```json
{
  "models": {
    "tfidf_lr": { "configuração aqui" }
  }
}
```

**Vantagem:** Você edita só um arquivo JSON, sem mexer em Python!

---

## 🏗️ Estrutura do `config/pipelines.json`

O arquivo tem **4 seções principais**:

```json
{
  "datasets": { ... },        // 1️⃣ Quais datasets você tem
  "cv_config": { ... },       // 2️⃣ Configuração de cross-validation
  "models": { ... },          // 3️⃣ Definição dos modelos
  "experiments": [ ... ]      // 4️⃣ Quais experimentos rodar
}
```

Vou explicar cada uma em detalhes:

---

## 1️⃣ Seção `datasets`

**O que é:** Lista de datasets disponíveis para treino.

```json
{
  "datasets": {
    "arcaico_moderno": "train_arcaico_moderno.csv",
    "complexo_simples": "train_complexo_simples.csv",
    "literal_dinamico": "train_literal_dinamico.csv"
  }
}
```

**Como funciona:**
- **Chave** (`arcaico_moderno`): Nome que você usa nos comandos
- **Valor** (`train_arcaico_moderno.csv`): Nome do arquivo CSV na pasta `data/`

**Exemplo de uso:**
```bash
uv run src/ep1/train.py --dataset arcaico_moderno --model tfidf_lr
                                  # ↑ usa esta chave
```

**Adicionar novo dataset:**
```json
{
  "datasets": {
    "arcaico_moderno": "train_arcaico_moderno.csv",
    "meu_novo_dataset": "meus_dados.csv"  // ← adicione aqui
  }
}
```

---

## 2️⃣ Seção `cv_config`

**O que é:** Configurações para cross-validation (validação cruzada).

```json
{
  "cv_config": {
    "n_folds": 5,         // Quantas divisões (5-fold CV)
    "random_state": 42    // Seed para reprodutibilidade
  }
}
```

**Como funciona:**
- `n_folds`: Número de "folds" na validação cruzada (comum: 5 ou 10)
- `random_state`: Garante que os resultados sejam reproduzíveis

**Para mudar:**
```json
{
  "cv_config": {
    "n_folds": 10,        // ← mude para 10-fold CV
    "random_state": 123   // ← mude a seed
  }
}
```

---

## 3️⃣ Seção `models` - A MAIS IMPORTANTE

**O que é:** Define COMO cada modelo é construído.

Existem **2 tipos** de modelos:

### Tipo A: `sklearn_pipeline` (Modelos sklearn padrão)

**Estrutura:**
```json
{
  "models": {
    "nome_do_modelo": {
      "type": "sklearn_pipeline",
      "steps": [
        {
          "name": "nome_do_step",
          "class": "caminho.completo.da.Classe",
          "params": { "parametros": "valores" }
        }
      ]
    }
  }
}
```

**Exemplo Real - Regressão Logística:**
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
          "params": {
            "max_iter": 2000,
            "n_jobs": 1
          }
        }
      ]
    }
  }
}
```

**Traduzindo para Python:**
```python
# O JSON acima equivale a este código Python:
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=2000, n_jobs=1))
])
```

### Entendendo cada parte:

```json
{
  "name": "tfidf",  // ← Nome do step no pipeline (você escolhe)
  "class": "sklearn.feature_extraction.text.TfidfVectorizer",  // ← Classe Python
  "params": {}  // ← Parâmetros passados para a classe
}
```

**Mais exemplos:**

#### Random Forest:
```json
{
  "meu_rf": {
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
          "random_state": 42,
          "n_jobs": -1
        }
      }
    ]
  }
}
```

#### SVM:
```json
{
  "tfidf_svm": {
    "type": "sklearn_pipeline",
    "steps": [
      {
        "name": "tfidf",
        "class": "sklearn.feature_extraction.text.TfidfVectorizer",
        "params": {
          "max_features": 10000
        }
      },
      {
        "name": "clf",
        "class": "sklearn.svm.SVC",
        "params": {
          "kernel": "linear",
          "C": 1.0
        }
      }
    ]
  }
}
```

### Tipo B: `custom` (Modelos customizados)

**O que é:** Para modelos que precisam de código Python especial.

```json
{
  "models": {
    "sbert_lr": {
      "type": "custom",
      "factory": "src.ep1.models.sbert.create_sbert_lr",
      "params": {}
    }
  }
}
```

**Como funciona:**
- `factory`: Caminho para uma função Python que cria o modelo
- `params`: Parâmetros passados para essa função

**A função Python:**
```python
# src/ep1/models/sbert.py
def create_sbert_lr():
    # Código especial para criar o modelo SBERT
    return pipeline
```

---

## 4️⃣ Seção `experiments`

**O que é:** Define quais modelos testar e com quais parâmetros.

```json
{
  "experiments": [
    {
      "model": "tfidf_lr",
      "param_grid": {
        "tfidf__max_features": [3000, 5000],
        "tfidf__ngram_range": [[1, 1], [1, 3]]
      }
    }
  ]
}
```

**Como funciona:**

1. **`model`**: Nome do modelo (deve existir em `"models"`)
2. **`param_grid`**: Parâmetros para testar (grid search)

### Entendendo `param_grid`:

**Formato:** `"step__parametro": [valores_para_testar]`

```json
{
  "param_grid": {
    "tfidf__max_features": [3000, 5000],  // ← Testa 3000 E 5000
    "clf__C": [0.1, 1.0, 10.0]            // ← Testa 0.1 E 1.0 E 10.0
  }
}
```

**O sistema testa TODAS as combinações:**
- `max_features=3000` + `C=0.1`
- `max_features=3000` + `C=1.0`
- `max_features=3000` + `C=10.0`
- `max_features=5000` + `C=0.1`
- `max_features=5000` + `C=1.0`
- `max_features=5000` + `C=10.0`

Total: 2 × 3 = **6 experimentos**

---

## 🎯 Exemplo Completo Passo a Passo

Vou criar um modelo novo do zero:

### Passo 1: Adicionar o modelo em `"models"`

```json
{
  "models": {
    "meu_modelo_novo": {
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
          "class": "sklearn.naive_bayes.MultinomialNB",
          "params": {
            "alpha": 1.0
          }
        }
      ]
    }
  }
}
```

### Passo 2: Adicionar experimentos

```json
{
  "experiments": [
    {
      "model": "meu_modelo_novo",
      "param_grid": {
        "vectorizer__max_features": [3000, 5000, 10000],
        "clf__alpha": [0.5, 1.0, 2.0]
      }
    }
  ]
}
```

### Passo 3: Usar o modelo

```bash
# Treinar
uv run src/ep1/train.py --dataset arcaico_moderno --model meu_modelo_novo --save

# Usar para predição
uv run predict_cli.py --model meu_modelo_novo --text "Teste"
```

---

## 🔍 Como o Sistema Lê o JSON

### 1. Carregar configuração:
```python
from src.ep1.config import get_default_config

config = get_default_config()
# Lê automaticamente config/pipelines.json
```

### 2. Ver o que foi carregado:
```python
# Ver datasets
print(config.datasets)
# {'arcaico_moderno': 'train_arcaico_moderno.csv', ...}

# Ver modelos disponíveis
print(list(config.models.keys()))
# ['tfidf_lr', 'tfidf_sgd', ...]

# Ver configuração de CV
print(config.cv_config)
# {'n_folds': 5, 'random_state': 42}
```

### 3. Criar um modelo:
```python
# O sistema lê o JSON e cria o modelo automaticamente
model = config.get_model("tfidf_lr")
print(model)
# Pipeline(steps=[('tfidf', TfidfVectorizer()), ('clf', LogisticRegression(...))])
```

### 4. Pegar experimentos:
```python
experiments = config.get_experiments()
for model_name, model_factory, param_grid in experiments:
    print(f"Modelo: {model_name}")
    print(f"Parâmetros: {param_grid}")
```

---

## 💡 Casos de Uso Práticos

### Caso 1: Mudar parâmetros de um modelo

**Antes (sem JSON):**
```python
# Tinha que editar código Python
def create_tfidf_lr():
    return Pipeline([
        ("tfidf", TfidfVectorizer()),  # ← editar aqui
        ("clf", LogisticRegression(max_iter=2000))  # ← e aqui
    ])
```

**Agora (com JSON):**
```json
{
  "models": {
    "tfidf_lr": {
      "steps": [
        {
          "name": "tfidf",
          "params": {
            "max_features": 10000  // ← só muda aqui!
          }
        }
      ]
    }
  }
}
```

### Caso 2: Adicionar novo algoritmo

```json
{
  "models": {
    "gradient_boosting": {
      "type": "sklearn_pipeline",
      "steps": [
        {
          "name": "tfidf",
          "class": "sklearn.feature_extraction.text.TfidfVectorizer",
          "params": {}
        },
        {
          "name": "clf",
          "class": "sklearn.ensemble.GradientBoostingClassifier",
          "params": {
            "n_estimators": 100,
            "learning_rate": 0.1,
            "max_depth": 3
          }
        }
      ]
    }
  },
  "experiments": [
    {
      "model": "gradient_boosting",
      "param_grid": {
        "clf__n_estimators": [50, 100, 200],
        "clf__learning_rate": [0.01, 0.1, 0.5]
      }
    }
  ]
}
```

### Caso 3: Testar diferentes vetorizadores

```json
{
  "models": {
    "countvec_lr": {
      "type": "sklearn_pipeline",
      "steps": [
        {
          "name": "vec",
          "class": "sklearn.feature_extraction.text.CountVectorizer",
          "params": {}
        },
        {
          "name": "clf",
          "class": "sklearn.linear_model.LogisticRegression",
          "params": {"max_iter": 2000}
        }
      ]
    },
    "hashvec_lr": {
      "type": "sklearn_pipeline",
      "steps": [
        {
          "name": "vec",
          "class": "sklearn.feature_extraction.text.HashingVectorizer",
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

---

## 🎨 Diagrama Visual

```
config/pipelines.json
│
├─ datasets          ──→  Quais arquivos CSV usar
│  └─ "arcaico_moderno": "train_arcaico_moderno.csv"
│
├─ cv_config         ──→  Configuração de validação cruzada
│  ├─ n_folds: 5
│  └─ random_state: 42
│
├─ models            ──→  COMO criar cada modelo
│  ├─ "tfidf_lr"
│  │  └─ steps:
│  │     ├─ TfidfVectorizer
│  │     └─ LogisticRegression
│  │
│  └─ "sbert_lr"
│     └─ factory: create_sbert_lr()
│
└─ experiments       ──→  QUAIS modelos testar e COM QUAIS parâmetros
   └─ model: "tfidf_lr"
      └─ param_grid:
         ├─ max_features: [3000, 5000]
         └─ ngram_range: [[1,1], [1,3]]
```

---

## 🧪 Testar Sua Configuração

```python
# Criar arquivo: test_config.py
from src.ep1.config import get_default_config

config = get_default_config()

# 1. Ver datasets
print("📁 Datasets:", config.datasets)

# 2. Ver modelos
print("\n🤖 Modelos:", list(config.models.keys()))

# 3. Testar criação de modelo
try:
    model = config.get_model("tfidf_lr")
    print("\n✅ Modelo criado com sucesso!")
    print(model)
except Exception as e:
    print(f"\n❌ Erro: {e}")

# 4. Ver experimentos
experiments = config.get_experiments()
print(f"\n🧪 Total de experimentos: {len(experiments)}")
for name, factory, params in experiments[:3]:  # Primeiros 3
    print(f"  - {name}: {list(params.keys())}")
```

```bash
# Executar teste
uv run python test_config.py
```

---

## ❓ Perguntas Frequentes

### 1. O que significa `tfidf__max_features`?

- `tfidf`: Nome do step no pipeline
- `__`: Separador
- `max_features`: Parâmetro da classe

```json
{
  "steps": [
    {"name": "tfidf", ...},  // ← Este nome
    {"name": "clf", ...}
  ]
}

// Para acessar parâmetros:
// "tfidf__parametro" → parâmetros do vectorizer
// "clf__parametro" → parâmetros do classificador
```

### 2. Como sei quais parâmetros posso usar?

Veja a documentação do sklearn:
- [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- etc.

### 3. Posso usar qualquer classe do sklearn?

Sim! Basta colocar o caminho completo:
```json
{
  "class": "sklearn.ensemble.RandomForestClassifier"
}
```

### 4. E se eu quiser usar bibliotecas externas?

Use o tipo `"custom"` e crie uma função Python que retorna o modelo.

---

## 🎓 Exercício Prático

Tente criar este modelo no JSON:

**Objetivo:** Pipeline com HashingVectorizer + SVM

**Solução:**
```json
{
  "models": {
    "hash_svm": {
      "type": "sklearn_pipeline",
      "steps": [
        {
          "name": "hasher",
          "class": "sklearn.feature_extraction.text.HashingVectorizer",
          "params": {
            "n_features": 2048,
            "ngram_range": [1, 2]
          }
        },
        {
          "name": "clf",
          "class": "sklearn.svm.LinearSVC",
          "params": {
            "C": 1.0,
            "max_iter": 1000
          }
        }
      ]
    }
  },
  "experiments": [
    {
      "model": "hash_svm",
      "param_grid": {
        "hasher__n_features": [1024, 2048, 4096],
        "clf__C": [0.1, 1.0, 10.0]
      }
    }
  ]
}
```

---

## 📚 Próximos Passos

1. ✅ Abra `config/pipelines.json`
2. ✅ Veja os modelos existentes
3. ✅ Tente modificar um parâmetro
4. ✅ Execute: `uv run examples_config.py`
5. ✅ Crie seu próprio modelo!

---

**Ainda com dúvidas?** Execute:
```bash
uv run examples_config.py
```

Isso mostra exemplos práticos de como usar o sistema!

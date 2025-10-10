# Modelos Word2Vec - Guia Completo

## 📋 Resumo

Foram adicionados **2 novos modelos** ao sistema de pipelines configuráveis via JSON:
- **`word2vec_lr`**: Word2Vec + Logistic Regression
- **`word2vec_svc`**: Word2Vec + Linear SVC

## 🎯 O que é Word2Vec?

Word2Vec é uma técnica de **embeddings de palavras** que representa cada palavra como um vetor numérico denso. Diferente do TF-IDF que cria vetores esparsos baseados em frequências, Word2Vec aprende representações semânticas das palavras.

### Vantagens sobre TF-IDF:
- ✅ Captura **relações semânticas** (palavras similares têm vetores próximos)
- ✅ Vetores **densos** (menor dimensionalidade que TF-IDF)
- ✅ Funciona melhor com **corpus menores**
- ✅ Pode capturar **contexto** das palavras

### Desvantagens:
- ❌ Mais **lento** para treinar
- ❌ Requer mais **memória**
- ❌ Não é **interpretável** como TF-IDF

## 🔧 Configuração no JSON

Os modelos foram adicionados em `config/pipelines.json`:

```json
{
  "models": {
    "word2vec_lr": {
      "type": "custom",
      "factory": "src.ep1.models.word2vec.create_word2vec_lr",
      "params": {}
    },
    "word2vec_svc": {
      "type": "custom",
      "factory": "src.ep1.models.word2vec.create_word2vec_svc",
      "params": {}
    }
  },
  "experiments": [
    {
      "model": "word2vec_lr",
      "param_grid": {
        "word2vec__vector_size": [50, 100, 200],
        "word2vec__window": [3, 5, 7],
        "word2vec__sg": [0, 1],
        "clf__C": [0.1, 1.0, 10.0]
      }
    },
    {
      "model": "word2vec_svc",
      "param_grid": {
        "word2vec__vector_size": [50, 100, 200],
        "word2vec__window": [3, 5, 7],
        "word2vec__sg": [0, 1],
        "clf__C": [0.1, 1.0, 10.0]
      }
    }
  ]
}
```

## 📊 Parâmetros do Word2Vec

### `word2vec__vector_size`
- **Descrição**: Dimensionalidade dos vetores de palavras
- **Valores**: `[50, 100, 200]`
- **Recomendação**: 
  - 50: datasets pequenos, treinamento rápido
  - 100: balanceado (padrão)
  - 200: datasets grandes, melhor qualidade

### `word2vec__window`
- **Descrição**: Janela de contexto (quantas palavras antes/depois considerar)
- **Valores**: `[3, 5, 7]`
- **Recomendação**:
  - 3: contexto local
  - 5: balanceado (padrão)
  - 7: contexto mais amplo

### `word2vec__sg`
- **Descrição**: Algoritmo de treinamento
- **Valores**: 
  - `0`: CBOW (Continuous Bag of Words) - mais rápido
  - `1`: Skip-gram - melhor para palavras raras
- **Recomendação**: 
  - CBOW (0) para datasets grandes
  - Skip-gram (1) para datasets pequenos

### `clf__C`
- **Descrição**: Parâmetro de regularização do classificador
- **Valores**: `[0.1, 1.0, 10.0]`
- **Recomendação**:
  - 0.1: mais regularização
  - 1.0: balanceado
  - 10.0: menos regularização

## 🚀 Como Usar

### 1. Treinar um modelo específico

```bash
uv run python src/ep1/train.py --dataset arcaico_moderno --model word2vec_lr --save
```

### 2. Rodar experimentos com grid search

```bash
# Apenas Word2Vec LR
uv run python src/ep1/experiments.py --models word2vec_lr

# Apenas Word2Vec SVC
uv run python src/ep1/experiments.py --models word2vec_svc

# Ambos os modelos Word2Vec
uv run python src/ep1/experiments.py --models word2vec_lr word2vec_svc

# Todos os modelos (incluindo Word2Vec)
uv run python src/ep1/experiments.py
```

### 3. Usar modelo treinado para predição

```bash
# Listar modelos disponíveis
uv run python predict_cli.py --list-models

# Fazer predição
uv run python predict_cli.py \
  --model arcaico_moderno__word2vec_lr.joblib \
  --text "Texto para classificar" \
  --proba
```

### 4. Usar no código Python

```python
from src.ep1.config import get_default_config

# Carregar configuração
config = get_default_config()

# Criar modelo
model = config.get_model('word2vec_lr')

# Treinar
X_train = ["texto 1", "texto 2", ...]
y_train = ["classe 1", "classe 2", ...]
model.fit(X_train, y_train)

# Predizer
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)

# Salvar modelo
import joblib
joblib.dump(model, 'models/meu_word2vec.joblib')
```

## 📈 Número de Experimentos

Cada modelo Word2Vec tem um grid de parâmetros com:
- 3 valores de `vector_size`
- 3 valores de `window`
- 2 valores de `sg`
- 3 valores de `C`

**Total**: 3 × 3 × 2 × 3 = **54 combinações por modelo**

Com 3 datasets e 2 modelos Word2Vec:
- **word2vec_lr**: 54 × 3 = 162 experimentos
- **word2vec_svc**: 54 × 3 = 162 experimentos
- **Total**: 324 experimentos

## 🔍 Implementação

O código está em `src/ep1/models/word2vec.py`:

```python
class Word2VecVectorizer(BaseEstimator, TransformerMixin):
    """
    Vetorizador compatível com sklearn que usa Word2Vec.
    
    Para cada documento:
    1. Tokeniza o texto em palavras
    2. Obtém o embedding de cada palavra
    3. Calcula a média dos embeddings
    """
    
    def __init__(self, vector_size=100, window=5, min_count=1, 
                 workers=4, sg=0, epochs=10):
        ...
    
    def fit(self, X, y=None):
        # Treina o modelo Word2Vec
        ...
    
    def transform(self, X):
        # Transforma documentos em vetores (média dos word embeddings)
        ...
```

## 💡 Exemplos Práticos

### Exemplo 1: Teste rápido

```bash
uv run python example_word2vec.py
```

Este script:
- Carrega um dataset
- Treina Word2Vec + LR e Word2Vec + SVC
- Compara predições
- Mostra componentes do pipeline

### Exemplo 2: Grid search completo

```bash
# Rodar todos os experimentos Word2Vec (pode demorar!)
uv run python src/ep1/experiments.py --models word2vec_lr word2vec_svc
```

### Exemplo 3: Comparar com TF-IDF

```bash
# Treinar TF-IDF + LR
uv run python src/ep1/train.py --dataset arcaico_moderno --model tfidf_lr --save

# Treinar Word2Vec + LR
uv run python src/ep1/train.py --dataset arcaico_moderno --model word2vec_lr --save

# Comparar resultados no terminal ou em results.csv
```

## 📦 Dependências

Foi adicionada a biblioteca `gensim` ao projeto:

```bash
uv add gensim
```

O `pyproject.toml` agora inclui:
```toml
dependencies = [
    "gensim>=4.3.3",
    ...
]
```

## 🎓 Quando usar Word2Vec?

**Use Word2Vec quando:**
- ✅ Você tem um **corpus especializado** (termos técnicos, domínio específico)
- ✅ Quer capturar **relações semânticas** entre palavras
- ✅ Tem **dados suficientes** (pelo menos alguns milhares de documentos)
- ✅ Pode aceitar **maior tempo de treinamento**

**Use TF-IDF quando:**
- ✅ Quer um modelo **mais rápido**
- ✅ Precisa de **interpretabilidade** (ver quais palavras são importantes)
- ✅ Tem **pouco tempo para experimentação**
- ✅ Dataset é muito **pequeno** (< 1000 documentos)

## 🔬 Próximos Passos

1. **Experimentar**: Rode `uv run python example_word2vec.py`
2. **Treinar**: Execute experimentos com seus datasets
3. **Comparar**: Veja se Word2Vec performa melhor que TF-IDF
4. **Otimizar**: Ajuste os parâmetros do grid search conforme necessário

## 📚 Referências

- [Gensim Word2Vec Documentation](https://radimrehurek.com/gensim/models/word2vec.html)
- [Word2Vec Paper](https://arxiv.org/abs/1301.3781)
- [CBOW vs Skip-gram](https://towardsdatascience.com/word2vec-skip-gram-and-cbow-4c6f6d5e6f7e)

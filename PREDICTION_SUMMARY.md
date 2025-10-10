# 📝 Resumo - Sistema de Predição com Modelos Treinados

## ✅ O que foi criado

Criei um **sistema completo** para você usar modelos treinados de forma simples e intuitiva.

## 🎯 3 Formas de Usar

### 1️⃣ CLI (Mais Rápido) ⚡

```bash
# Listar modelos
uv run predict_cli.py --list-models

# Classificar texto
uv run predict_cli.py \
  --model arcaico_moderno__tfidf_lr \
  --text "Seu texto aqui" \
  --proba

# Processar CSV
uv run predict_cli.py \
  --model complexo_simples__tfidf_lr \
  --csv dados.csv \
  --output resultados.csv

# Comparar todos os modelos
uv run predict_cli.py \
  --compare "Texto para comparar"
```

### 2️⃣ Python Simples 🐍

```python
import joblib

# Carregar e usar
model = joblib.load("models/arcaico_moderno__tfidf_lr.joblib")
predicao = model.predict(["Seu texto"])
print(predicao[0])
```

### 3️⃣ Módulo Avançado 🔧

```python
from src.ep1.inference import ModelPredictor

# Mais funcionalidades
predictor = ModelPredictor("models/arcaico_moderno__tfidf_lr.joblib")

# DataFrame com probabilidades
df = predictor.predict_with_confidence([
    "Texto 1",
    "Texto 2"
])
```

## 📦 Modelos Disponíveis

Você já tem **3 modelos treinados**:

1. `arcaico_moderno__tfidf_lr.joblib` - Classifica texto como arcaico ou moderno
2. `complexo_simples__tfidf_lr.joblib` - Classifica como complexo ou simples
3. `literal_dinamico__tfidf_lr.joblib` - Classifica como literal ou dinâmico

## 📚 Arquivos Criados

### Código
- **`src/ep1/inference.py`** - Módulo completo de inferência
- **`predict_cli.py`** - CLI interativa
- **`examples_inference.py`** - 7 exemplos práticos

### Documentação
- **`HOW_TO_PREDICT.md`** - 🎯 **COMECE AQUI!** Guia completo
- **`PREDICT_GUIDE.md`** - Guia detalhado com exemplos
- Este arquivo - Resumo rápido

## 🚀 Teste Agora

```bash
# 1. Listar modelos disponíveis
uv run predict_cli.py --list-models

# 2. Testar com um texto
uv run predict_cli.py \
  --model arcaico_moderno__tfidf_lr \
  --text "Este é um texto moderno sobre tecnologia" \
  --proba

# 3. Ver todos os exemplos
uv run examples_inference.py
```

## 📖 Exemplos Práticos

### Classificar vários textos

```python
from src.ep1.inference import ModelPredictor

predictor = ModelPredictor("models/arcaico_moderno__tfidf_lr.joblib")

textos = [
    "Texto moderno sobre inteligência artificial",
    "Outrossim, cumpre-nos manifestar",
    "A tecnologia avança rapidamente"
]

# Obter DataFrame com resultados
df = predictor.predict_with_confidence(textos)
print(df)
```

### Processar CSV grande

```python
from src.ep1.inference import ModelPredictor

predictor = ModelPredictor("models/complexo_simples__tfidf_lr.joblib")

# Uma linha faz tudo
df = predictor.predict_from_csv(
    "meus_dados.csv",
    output_csv="resultados.csv",
    include_probabilities=True
)
```

### Comparar todos os modelos

```python
from src.ep1.inference import predict_with_all_models

df = predict_with_all_models(["Texto para comparar"])
print(df)
# Mostra predição de cada modelo
```

## 🎓 Treinar Novo Modelo

```bash
uv run src/ep1/train.py \
  --dataset arcaico_moderno \
  --model tfidf_lr \
  --cv 10 \
  --save
```

Isso salva em `models/arcaico_moderno__tfidf_lr.joblib`

## ⚡ Comandos Mais Usados

```bash
# Ver modelos
uv run predict_cli.py --list-models

# Predizer com probabilidades
uv run predict_cli.py --model MODELO --text "TEXTO" --proba

# Processar CSV
uv run predict_cli.py --model MODELO --csv dados.csv --output result.csv

# Ver exemplos completos
uv run examples_inference.py

# Treinar novo modelo
uv run src/ep1/train.py --dataset DATASET --model MODELO --save
```

## 💡 Dicas Importantes

1. **Sempre use `--proba`** para ver a confiança da predição
2. **Filtre por confiança** para identificar predições incertas
3. **Compare modelos** antes de escolher qual usar
4. **Use o CLI** para testes rápidos
5. **Use o módulo Python** para automação

## 📄 Formato dos Dados

### Entrada (CSV)
Precisa ter coluna `text`:
```csv
text
"Primeiro texto"
"Segundo texto"
```

### Saída (CSV com --proba)
```csv
text,prediction,confidence,prob_arcaico,prob_moderno
"Primeiro texto",arcaico,0.85,0.85,0.15
"Segundo texto",moderno,0.92,0.08,0.92
```

## 🆘 Problemas Comuns

### Modelo não encontrado
```bash
# Verificar modelos disponíveis
uv run predict_cli.py --list-models
```

### Coluna 'text' não encontrada
```python
# Verificar e renomear
import pandas as pd
df = pd.read_csv("dados.csv")
print(df.columns)  # Ver colunas
df = df.rename(columns={'minha_coluna': 'text'})
```

## 📚 Documentação Completa

- **HOW_TO_PREDICT.md** - Guia completo (LEIA PRIMEIRO!)
- **PREDICT_GUIDE.md** - Guia detalhado com casos de uso
- **examples_inference.py** - Execute para ver exemplos: `uv run examples_inference.py`

## 🎉 Pronto!

Agora você pode:
- ✅ Classificar textos individuais
- ✅ Processar arquivos CSV
- ✅ Comparar múltiplos modelos
- ✅ Ver probabilidades e confiança
- ✅ Treinar novos modelos

**Comece agora:**
```bash
uv run predict_cli.py --list-models
```

🚀 **Boa classificação!**

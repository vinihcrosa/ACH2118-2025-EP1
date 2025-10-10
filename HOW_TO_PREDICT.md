# 🎯 Como Usar Modelos Treinados - Guia Completo

## 📋 Resumo Rápido

Você tem **3 formas** de usar modelos treinados:

1. **CLI Simples** - Linha de comando (mais rápido)
2. **Script Python** - Para automação
3. **Módulo inference.py** - Para controle total

## 🚀 Forma 1: CLI Simples (Recomendado)

### Listar modelos disponíveis

```bash
uv run predict_cli.py --list-models
```

### Classificar um texto

```bash
uv run predict_cli.py \
  --model arcaico_moderno__tfidf_lr \
  --text "Seu texto aqui"
```

### Classificar com probabilidades

```bash
uv run predict_cli.py \
  --model arcaico_moderno__tfidf_lr \
  --text "Seu texto aqui" \
  --proba
```

### Processar arquivo CSV

```bash
uv run predict_cli.py \
  --model complexo_simples__tfidf_lr \
  --csv dados.csv \
  --output resultados.csv \
  --proba
```

### Comparar todos os modelos

```bash
uv run predict_cli.py \
  --compare "Texto para comparar entre modelos"
```

## 💻 Forma 2: Script Python Simples

### Exemplo básico

```python
import joblib

# Carregar modelo
model = joblib.load("models/arcaico_moderno__tfidf_lr.joblib")

# Classificar
texto = "Seu texto aqui"
predicao = model.predict([texto])

print(f"Predição: {predicao[0]}")
```

### Com probabilidades

```python
import joblib

model = joblib.load("models/arcaico_moderno__tfidf_lr.joblib")

texto = "Seu texto aqui"
predicao = model.predict([texto])[0]
probabilidades = model.predict_proba([texto])[0]

print(f"Predição: {predicao}")
print(f"Classes: {model.classes_}")
print(f"Probabilidades:")
for classe, prob in zip(model.classes_, probabilidades):
    print(f"  {classe}: {prob:.2%}")
```

### Processar CSV

```python
import joblib
import pandas as pd

# Carregar modelo
model = joblib.load("models/complexo_simples__tfidf_lr.joblib")

# Ler CSV
df = pd.read_csv("dados.csv")

# Fazer predições
df["predicao"] = model.predict(df["text"])

# Adicionar probabilidades
probs = model.predict_proba(df["text"])
df["confianca"] = probs.max(axis=1)

# Salvar
df.to_csv("resultados.csv", index=False)
```

## 🔧 Forma 3: Módulo inference.py (Controle Total)

### Uso básico

```python
from src.ep1.inference import ModelPredictor

# Carregar modelo
predictor = ModelPredictor("models/arcaico_moderno__tfidf_lr.joblib")

# Classificar
texto = "Seu texto aqui"
predicao = predictor.predict(texto)
print(predicao)
```

### Com DataFrame de resultados

```python
from src.ep1.inference import ModelPredictor

predictor = ModelPredictor("models/arcaico_moderno__tfidf_lr.joblib")

textos = [
    "Primeiro texto",
    "Segundo texto",
    "Terceiro texto"
]

# Retorna DataFrame com texto, predição e probabilidades
df = predictor.predict_with_confidence(textos)
print(df)
```

### Processar CSV completo

```python
from src.ep1.inference import ModelPredictor

predictor = ModelPredictor("models/complexo_simples__tfidf_lr.joblib")

# Processar CSV com uma linha
df = predictor.predict_from_csv(
    "dados.csv",
    output_csv="resultados.csv",
    include_probabilities=True
)
```

### Carregar todos os modelos

```python
from src.ep1.inference import load_all_models

# Carregar todos
modelos = load_all_models("models")

# Usar qualquer modelo
for nome, predictor in modelos.items():
    print(f"{nome}: {predictor.classes}")
```

### Aplicar todos os modelos

```python
from src.ep1.inference import predict_with_all_models

textos = ["Texto 1", "Texto 2"]
df = predict_with_all_models(textos)

# DataFrame com predição de cada modelo
print(df)
```

### Atalho rápido

```python
from src.ep1.inference import quick_predict

resultado = quick_predict(
    'arcaico_moderno__tfidf_lr',
    'Texto para classificar'
)
```

## 📊 Exemplos Práticos

### 1. Filtrar por confiança

```python
from src.ep1.inference import ModelPredictor

predictor = ModelPredictor("models/arcaico_moderno__tfidf_lr.joblib")
df = predictor.predict_from_csv("dados.csv", include_probabilities=True)

# Filtrar apenas predições confiáveis (>80%)
confiavel = df[df['confidence'] > 0.8]
incerto = df[df['confidence'] <= 0.8]

print(f"Confiáveis: {len(confiavel)} ({len(confiavel)/len(df)*100:.1f}%)")
print(f"Incertos: {len(incerto)} ({len(incerto)/len(df)*100:.1f}%)")
```

### 2. Processar arquivo grande em lotes

```python
import joblib
import pandas as pd

model = joblib.load("models/arcaico_moderno__tfidf_lr.joblib")

# Processar em chunks
chunk_size = 1000
chunks = []

for chunk in pd.read_csv("arquivo_grande.csv", chunksize=chunk_size):
    chunk["predicao"] = model.predict(chunk["text"])
    chunks.append(chunk)

resultado = pd.concat(chunks)
resultado.to_csv("resultado.csv", index=False)
```

### 3. Comparar múltiplos modelos

```python
from src.ep1.inference import load_all_models
import pandas as pd

# Carregar todos os modelos
modelos = load_all_models("models")

# Seus dados
df = pd.read_csv("dados.csv")

# Aplicar cada modelo
for nome, predictor in modelos.items():
    nome_curto = nome.split('__')[0]  # ex: arcaico_moderno
    df[f'pred_{nome_curto}'] = predictor.predict(df["text"])

df.to_csv("comparacao_modelos.csv", index=False)
```

### 4. Análise de distribuição

```python
from src.ep1.inference import ModelPredictor

predictor = ModelPredictor("models/complexo_simples__tfidf_lr.joblib")
df = predictor.predict_from_csv("dados.csv")

# Ver distribuição
print(df['prediction'].value_counts())
print(df['prediction'].value_counts(normalize=True))
```

## 🎓 Treinar Novo Modelo

Para treinar e salvar um novo modelo:

```bash
uv run src/ep1/train.py \
  --dataset arcaico_moderno \
  --model tfidf_lr \
  --cv 10 \
  --save
```

Isso vai:
- Treinar com 10-fold cross-validation
- Mostrar acurácia média e desvio
- Salvar resultados em `results.csv`
- Treinar em 100% dos dados
- Salvar modelo em `models/arcaico_moderno__tfidf_lr.joblib`

## 📁 Formato do CSV de Entrada

Seu CSV deve ter uma coluna chamada `text`:

```csv
text
"Primeiro texto para classificar"
"Segundo texto"
"Terceiro texto"
```

Ou com outras colunas:

```csv
id,text,metadata
1,"Primeiro texto","info1"
2,"Segundo texto","info2"
```

## 📈 Formato do CSV de Saída

Sem probabilidades:

```csv
text,prediction
"Primeiro texto","arcaico"
"Segundo texto","moderno"
```

Com probabilidades (`--proba`):

```csv
text,prediction,confidence,prob_arcaico,prob_moderno
"Primeiro texto","arcaico",0.8523,0.8523,0.1477
"Segundo texto","moderno",0.7234,0.2766,0.7234
```

## 🔍 Inspecionar Modelo

```python
import joblib

model = joblib.load("models/arcaico_moderno__tfidf_lr.joblib")

print("Classes:", model.classes_)
print("Pipeline:", model.steps)

# Testar
teste = model.predict(["Texto de teste"])
print("Teste:", teste[0])
```

## 📚 Documentação Completa

- **PREDICT_GUIDE.md** - Guia detalhado de predição
- **examples_inference.py** - 7 exemplos práticos (execute: `uv run examples_inference.py`)
- **predict_cli.py** - CLI interativa

## ⚡ Comandos Rápidos

```bash
# Ver modelos
uv run predict_cli.py --list-models

# Predizer texto
uv run predict_cli.py --model MODELO --text "TEXTO" --proba

# Predizer CSV
uv run predict_cli.py --model MODELO --csv dados.csv --output result.csv

# Comparar modelos
uv run predict_cli.py --compare "TEXTO"

# Treinar modelo
uv run src/ep1/train.py --dataset DATASET --model MODELO --save

# Ver exemplos
uv run examples_inference.py
```

## 🆘 Troubleshooting

### Modelo não encontrado

```bash
# Verificar modelos
ls models/

# Listar com CLI
uv run predict_cli.py --list-models
```

### Coluna 'text' não encontrada

```python
import pandas as pd

# Ver colunas
df = pd.read_csv("dados.csv")
print(df.columns)

# Renomear
df = df.rename(columns={'minha_coluna': 'text'})
```

### Encoding de caracteres

```python
# Tentar diferentes encodings
df = pd.read_csv("dados.csv", encoding='utf-8')
df = pd.read_csv("dados.csv", encoding='ISO-8859-1')
df = pd.read_csv("dados.csv", encoding='latin1')
```

## 💡 Dicas

1. **Sempre verifique a confiança** das predições (`--proba`)
2. **Para arquivos grandes**, processe em chunks
3. **Compare múltiplos modelos** antes de escolher
4. **Filtre por confiança** para identificar casos ambíguos
5. **Use o CLI** para testes rápidos
6. **Use o módulo** para automação e scripts

---

**Pronto para usar!** 🎉

Escolha a forma que preferir e comece a classificar seus textos!

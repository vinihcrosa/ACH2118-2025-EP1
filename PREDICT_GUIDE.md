# 🎯 Guia: Usar Modelos Treinados para Predição

Este guia mostra como usar um modelo já treinado para fazer predições em novos dados.

## 📦 Modelos Disponíveis

Você tem modelos salvos em `/models`:

```bash
models/
├── arcaico_moderno__tfidf_lr.joblib
├── complexo_simples__tfidf_lr.joblib
└── literal_dinamico__tfidf_lr.joblib
```

## 🚀 Método 1: Usar o Script de Predição

### Preparar seus dados

Crie um CSV com uma coluna chamada `text`:

```csv
text
"Este é o primeiro texto para classificar"
"Este é o segundo texto"
"E aqui vai mais um texto"
```

### Executar predição

```bash
uv run src/ep1/predict.py \
  --model-path models/arcaico_moderno__tfidf_lr.joblib \
  --input-csv meus_dados.csv \
  --output-csv resultados.csv
```

### Resultado

O arquivo `resultados.csv` terá:

```csv
text,predicted_style
"Este é o primeiro texto para classificar",moderno
"Este é o segundo texto",arcaico
"E aqui vai mais um texto",moderno
```

## 💻 Método 2: Usar Programaticamente em Python

### Exemplo Básico

```python
import joblib
import pandas as pd

# 1. Carregar o modelo
model = joblib.load("models/arcaico_moderno__tfidf_lr.joblib")

# 2. Preparar dados
textos = [
    "Este é um texto moderno",
    "Aqui vai outro exemplo",
    "Mais um texto para classificar"
]

# 3. Fazer predições
predicoes = model.predict(textos)

print(predicoes)
# ['moderno', 'moderno', 'arcaico']
```

### Exemplo com CSV

```python
import joblib
import pandas as pd

# Carregar modelo
model = joblib.load("models/complexo_simples__tfidf_lr.joblib")

# Ler CSV
df = pd.read_csv("meus_dados.csv")

# Fazer predições
df["predicao"] = model.predict(df["text"])

# Salvar resultado
df.to_csv("resultados_com_predicoes.csv", index=False)
```

### Exemplo com Probabilidades

```python
import joblib
import pandas as pd

model = joblib.load("models/literal_dinamico__tfidf_lr.joblib")

textos = ["Texto de exemplo"]

# Predição com probabilidades
predicoes = model.predict(textos)
probabilidades = model.predict_proba(textos)

# Ver classes
classes = model.classes_
print(f"Classes: {classes}")

# Ver probabilidades
for texto, pred, probs in zip(textos, predicoes, probabilidades):
    print(f"\nTexto: {texto}")
    print(f"Predição: {pred}")
    for classe, prob in zip(classes, probs):
        print(f"  {classe}: {prob:.4f} ({prob*100:.2f}%)")
```

## 🔧 Método 3: Criar Função Utilitária

Vou criar um módulo para facilitar:

```python
# src/ep1/inference.py
import joblib
from pathlib import Path
from typing import List, Union
import pandas as pd
import numpy as np

class ModelPredictor:
    """Classe para facilitar predições com modelos salvos."""
    
    def __init__(self, model_path: str):
        """
        Carrega um modelo salvo.
        
        Args:
            model_path: Caminho para o arquivo .joblib
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
                'confidence': probs.max()
            }
            # Adicionar probabilidade de cada classe
            for classe, prob in zip(self.model.classes_, probs):
                row[f'prob_{classe}'] = prob
            
            results.append(row)
        
        return pd.DataFrame(results)
    
    @property
    def classes(self):
        """Retorna as classes do modelo."""
        return self.model.classes_
    
    def __repr__(self):
        return f"ModelPredictor(model='{self.model_name}', classes={list(self.classes)})"
```

Uso:

```python
from src.ep1.inference import ModelPredictor

# Carregar modelo
predictor = ModelPredictor("models/arcaico_moderno__tfidf_lr.joblib")

# Predição simples
texto = "Este é um texto de exemplo"
resultado = predictor.predict(texto)
print(resultado)  # ['moderno']

# Predição com confiança
textos = ["Texto 1", "Texto 2", "Texto 3"]
df = predictor.predict_with_confidence(textos)
print(df)
#              text prediction  confidence  prob_arcaico  prob_moderno
# 0        Texto 1     moderno      0.8523        0.1477        0.8523
# 1        Texto 2     arcaico      0.7234        0.7234        0.2766
```

## 📊 Exemplos de Casos de Uso

### 1. Classificar arquivo grande em lotes

```python
import joblib
import pandas as pd

model = joblib.load("models/arcaico_moderno__tfidf_lr.joblib")

# Processar em chunks para arquivos grandes
chunk_size = 1000
chunks = []

for chunk in pd.read_csv("arquivo_grande.csv", chunksize=chunk_size):
    chunk["predicao"] = model.predict(chunk["text"])
    chunks.append(chunk)

resultado = pd.concat(chunks)
resultado.to_csv("resultado_final.csv", index=False)
```

### 2. Aplicar múltiplos modelos

```python
import joblib
import pandas as pd

modelos = {
    'arcaico_moderno': joblib.load("models/arcaico_moderno__tfidf_lr.joblib"),
    'complexo_simples': joblib.load("models/complexo_simples__tfidf_lr.joblib"),
    'literal_dinamico': joblib.load("models/literal_dinamico__tfidf_lr.joblib")
}

df = pd.read_csv("meus_textos.csv")

# Aplicar todos os modelos
for nome, modelo in modelos.items():
    df[f'pred_{nome}'] = modelo.predict(df["text"])

df.to_csv("resultado_multiplos_modelos.csv", index=False)
```

### 3. Filtrar por confiança

```python
import joblib
import pandas as pd

model = joblib.load("models/arcaico_moderno__tfidf_lr.joblib")

df = pd.read_csv("textos.csv")

# Predições com probabilidades
predicoes = model.predict(df["text"])
probabilidades = model.predict_proba(df["text"])

# Adicionar ao DataFrame
df["predicao"] = predicoes
df["confianca"] = probabilidades.max(axis=1)

# Filtrar apenas predições confiáveis (>80%)
df_confiavel = df[df["confianca"] > 0.8]

print(f"Total: {len(df)}")
print(f"Confiáveis: {len(df_confiavel)} ({len(df_confiavel)/len(df)*100:.1f}%)")
```

## 🎓 Treinar e Salvar Novo Modelo

Se você quiser treinar um novo modelo:

```bash
uv run src/ep1/train.py \
  --dataset arcaico_moderno \
  --model tfidf_lr \
  --cv 10 \
  --save
```

Isso vai:
1. Treinar com cross-validation (10 folds)
2. Salvar resultados em `results.csv`
3. Treinar em 100% dos dados
4. Salvar modelo em `models/arcaico_moderno__tfidf_lr.joblib`

## 📋 Resumo dos Comandos

```bash
# Método mais simples - via script
uv run src/ep1/predict.py \
  --model-path models/MODELO.joblib \
  --input-csv dados.csv \
  --output-csv resultado.csv

# Treinar novo modelo
uv run src/ep1/train.py \
  --dataset DATASET \
  --model MODELO \
  --save

# Listar modelos disponíveis
ls -lh models/
```

## 🔍 Verificar Modelo

```python
import joblib

# Carregar e inspecionar
model = joblib.load("models/arcaico_moderno__tfidf_lr.joblib")

print("Pipeline:", model)
print("Classes:", model.classes_)
print("Steps:", model.steps)

# Testar
texto_teste = "Este é um texto de teste"
predicao = model.predict([texto_teste])
print(f"Predição: {predicao[0]}")
```

## ⚠️ Dicas Importantes

1. **Formato dos dados**: O CSV de entrada deve ter coluna `text`
2. **Encoding**: O script de predição usa `ISO-8859-1` por padrão
3. **Texto vazio**: Textos vazios são preenchidos com string vazia
4. **Batch processing**: Para muitos dados, processe em lotes
5. **Confiança**: Use `predict_proba()` para ver a confiança das predições

## 🆘 Troubleshooting

### Erro: "Modelo não encontrado"
```bash
# Verificar modelos disponíveis
ls models/

# Verificar caminho completo
pwd
ls -la models/
```

### Erro: "Coluna 'text' não encontrada"
```python
# Verificar colunas do CSV
import pandas as pd
df = pd.read_csv("meus_dados.csv")
print(df.columns)

# Renomear coluna se necessário
df = df.rename(columns={'minha_coluna': 'text'})
```

### Memória insuficiente para arquivo grande
```python
# Processar em chunks
for chunk in pd.read_csv("arquivo.csv", chunksize=1000):
    predicoes = model.predict(chunk["text"])
    # processar...
```

ACH2118-2025-EP1
=================

Este projeto reúne experimentos de classificação de estilo de texto usados na disciplina ACH2118. Os scripts trabalham com três conjuntos de dados (`train_arcaico_moderno.csv`, `train_complexo_simples.csv`, `train_literal_dinamico.csv`) e avaliam diversos classificadores tradicionais e neurais baseados em TF-IDF, SBERT e MLP.

## 🚀 Início Rápido

### Instalação
```bash
# Instalar dependências
uv sync

# Listar modelos disponíveis
uv run predict_cli.py --list-models

# Classificar um texto
uv run predict_cli.py --model arcaico_moderno__tfidf_lr --text "Seu texto aqui" --proba
```

## 📚 Documentação

- **[HOW_TO_PREDICT.md](HOW_TO_PREDICT.md)** - 🎯 **COMECE AQUI!** Guia completo de como usar modelos treinados
- **[QUICKSTART.md](QUICKSTART.md)** - Guia rápido do sistema de configuração JSON
- **[config/README.md](config/README.md)** - Documentação detalhada das configurações
- **[MIGRATION.md](MIGRATION.md)** - Detalhes da migração para JSON
- **[PREDICT_GUIDE.md](PREDICT_GUIDE.md)** - Guia detalhado de predição

## 💻 Principais Funcionalidades

### 1. Usar Modelos Treinados (Predição)

**CLI Simples:**
```bash
# Classificar texto
uv run predict_cli.py --model arcaico_moderno__tfidf_lr --text "Seu texto"

# Processar CSV
uv run predict_cli.py --model complexo_simples__tfidf_lr --csv dados.csv

# Comparar todos os modelos
uv run predict_cli.py --compare "Texto para comparar"
```

**Python:**
```python
from src.ep1.inference import ModelPredictor

predictor = ModelPredictor("models/arcaico_moderno__tfidf_lr.joblib")
predicao = predictor.predict("Seu texto aqui")
```

Ver exemplos completos: `uv run examples_inference.py`

### 2. Treinar Novos Modelos

```bash
uv run src/ep1/train.py \
  --dataset arcaico_moderno \
  --model tfidf_lr \
  --cv 10 \
  --save
```

### 3. Executar Experimentos

```bash
# Roda todos os experimentos configurados em config/pipelines.json
uv run python -m src.ep1.experiments
```

### 4. Gerar Relatórios

```bash
uv run python -m src.ep1.report \
  --input experiments.csv \
  --output reports/experiments_report.md
```

Requisitos
----------
- Python 3.11+
- [uv](https://docs.astral.sh/uv/) para gerenciar dependências
- GPU opcional (apenas acelera os experimentos com MLP em PyTorch)

Configuração
------------
1. Instale o `uv` seguindo a documentação oficial.
2. Dentro do diretório do projeto, resolva as dependências:
   ```bash
   uv sync
   ```

## ⚙️ Configuração via JSON

Todos os modelos e experimentos agora são configurados através de `config/pipelines.json`. Isso permite:

- ✅ Adicionar novos modelos sem editar código Python
- ✅ Modificar parâmetros facilmente
- ✅ Configurações versionadas e reproduzíveis
- ✅ Suporte para modelos sklearn e customizados

**Exemplo de configuração:**
```json
{
  "models": {
    "tfidf_lr": {
      "type": "sklearn_pipeline",
      "steps": [
        {"name": "tfidf", "class": "sklearn.feature_extraction.text.TfidfVectorizer", "params": {}},
        {"name": "clf", "class": "sklearn.linear_model.LogisticRegression", "params": {"max_iter": 2000}}
      ]
    }
  }
}
```

Ver mais: `config/README.md` ou `uv run examples_config.py`

Como rodar os experimentos
--------------------------
Executa toda a grade de validação cruzada para os modelos definidos em `config/pipelines.json` e grava os resultados em `experiments.csv`.
```bash
uv run python -m src.ep1.experiments
```

O script faz validação estratificada com k-folds (configurável em `config/pipelines.json`). Para alterar modelos ou hiperparâmetros, edite `config/pipelines.json`.

Relatório automático
--------------------
Para gerar um resumo em Markdown com os resultados atuais do CSV:
```bash
uv run python -m src.ep1.report --input experiments.csv --output reports/experiments_report.md
```
O parâmetro `--top` (opcional) permite limitar quantas linhas aparecerão por conjunto (`--top 5`, por exemplo). O arquivo final fica por padrão em `reports/experiments_report.md`.

Modelos implementados
---------------------
- `tfidf_lr`: Regressão logística sobre vetores TF-IDF.
- `tfidf_sgd`: Classificador linear otimizado com SGD (`log_loss`).
- `tfidf_pa`: Passive-Aggressive.
- `tfidf_ridge`: RidgeClassifier.
- `tfidf_cnb`: Complement Naive Bayes.
- `tfidf_nb`: Multinomial Naive Bayes (baseline simples).
- `tfidf_svc`: LinearSVC.
- `sbert_lr`: SBERT com regressão logística.
- `sbert_svc`: SBERT com LinearSVC.
- `torch_mlp`: MLP em PyTorch (via skorch) sobre TF-IDF.

Saída dos experimentos
----------------------
- `experiments.csv`: histórico cumulativo com média, desvio padrão e scores individuais por fold.

Outros scripts úteis
--------------------
- `src/ep1/train.py`: fluxo de treino para um modelo específico (verifique o código para detalhes).
- `src/ep1/predict.py`: gera previsões a partir de um modelo previamente treinado/salvo.

Dicas
-----
- Os caches de embeddings SBERT ficam em `cache/embeddings`. Remova essa pasta para regenerar vetores se alterar os dados ou modelos.
- O número de combinações cresce rapidamente com `ngram_range` estendido até `(1, 10)`; ajuste `max_features` ou reduza a grade se notar uso excessivo de memória/tempo.

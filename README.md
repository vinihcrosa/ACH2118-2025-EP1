ACH2118-2025-EP1
=================

Este projeto reúne experimentos de classificação de estilo de texto usados na disciplina ACH2118. Os scripts trabalham com três conjuntos de dados (`train_arcaico_moderno.csv`, `train_complexo_simples.csv`, `train_literal_dinamico.csv`) e avaliam diversos classificadores tradicionais e neurais baseados em TF-IDF, SBERT e MLP.

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

Como rodar os experimentos
--------------------------
Executa toda a grade de validação cruzada para os modelos definidos em `src/ep1/experiments.py` e grava os resultados em `experiments.csv`.
```bash
uv run python -m src.ep1.experiments
```

O script faz validação estratificada com k-folds (valor padrão `N_FOLDS = 5`). Para alterar quantidade de folds ou os hiperparâmetros considerados, edite `src/ep1/experiments.py` antes de rodar o comando.

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

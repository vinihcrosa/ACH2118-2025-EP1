# GitHub Actions Workflows

Este projeto possui 3 workflows automatizados do GitHub Actions para facilitar o treinamento e experimentação de modelos.

## 📋 Workflows Disponíveis

### 1. 🧪 CI - Tests and Linting (`ci.yml`)

**Quando roda:**
- Push para branches `main` ou `develop`
- Pull requests para `main` ou `develop`

**O que faz:**
- ✅ Verifica formatação do código Python
- ✅ Testa imports de todos os módulos
- ✅ Valida configuração JSON (`pipelines.json`)
- ✅ Testa criação de todos os 12 modelos
- ✅ Executa treinamento rápido de teste

**Duração:** ~2-3 minutos

---

### 2. 🤖 Run ML Experiments (`run-experiments.yml`)

**Quando roda:**
- Push para branch `main`
- Pull requests para `main`
- Manualmente via GitHub UI
- Todo domingo às 00:00 UTC (agendado)

**O que faz:**
1. Instala dependências com `uv`
2. Restaura cache de embeddings
3. **Roda todos os experimentos** (`python src/ep1/experiments.py`)
4. Gera relatório completo (`python src/ep1/report.py`)
5. Faz upload dos resultados:
   - `results.csv`
   - `experiments.csv`
   - `reports/experiments_report.md`
   - Modelos treinados (`models/*.joblib`)
6. Comenta resultados em Pull Requests

**Duração:** ~30 minutos a 2 horas (dependendo dos experimentos)

**Timeout:** 2 horas

**Artifacts:**
- `experiment-results` (90 dias)
- `trained-models` (30 dias)

---

### 3. 🎯 Train Specific Models (`train-models.yml`)

**Quando roda:**
- Manualmente via GitHub UI (workflow_dispatch)

**Parâmetros configuráveis:**

| Parâmetro | Descrição | Padrão | Exemplo |
|-----------|-----------|--------|---------|
| `datasets` | Datasets para usar (separados por vírgula) | `arcaico_moderno,complexo_simples,literal_dinamico` | `arcaico_moderno` |
| `models` | Modelos para treinar (separados por vírgula) | `all` | `word2vec_lr,tfidf_lr` |
| `save_models` | Salvar modelos treinados | `true` | `false` |

**O que faz:**
1. Treina modelos específicos nos datasets escolhidos
2. Gera relatório
3. Faz upload dos resultados e modelos (se `save_models=true`)
4. Cria resumo no GitHub

**Duração:** Variável (depende dos modelos escolhidos)

**Timeout:** 3 horas

---

## 🚀 Como Usar

### Executar CI (Automático)

Simplesmente faça push ou abra um PR:

```bash
git add .
git commit -m "feat: add new feature"
git push origin main
```

O workflow CI rodará automaticamente.

---

### Executar Experimentos Completos (Manual)

1. Vá para **Actions** no GitHub
2. Selecione **"Run ML Experiments"**
3. Clique em **"Run workflow"**
4. Escolha a branch (geralmente `main`)
5. Clique em **"Run workflow"**

![Run Workflow](https://docs.github.com/assets/cb-33887/mw-1440/images/help/actions/workflow-dispatch.webp)

---

### Treinar Modelos Específicos (Manual)

1. Vá para **Actions** no GitHub
2. Selecione **"Train Specific Models"**
3. Clique em **"Run workflow"**
4. Configure os parâmetros:
   - **Branch**: `main`
   - **Datasets**: `arcaico_moderno,complexo_simples` (ou outros)
   - **Models**: `word2vec_lr,word2vec_svc` (ou `all`)
   - **Save models**: ✅ (marque para salvar)
5. Clique em **"Run workflow"**

**Exemplos de uso:**

#### Exemplo 1: Treinar apenas Word2Vec em um dataset
```
Datasets: arcaico_moderno
Models: word2vec_lr,word2vec_svc
Save models: ✅
```

#### Exemplo 2: Comparar TF-IDF vs Word2Vec
```
Datasets: arcaico_moderno
Models: tfidf_lr,word2vec_lr
Save models: ✅
```

#### Exemplo 3: Treinar todos os modelos
```
Datasets: arcaico_moderno,complexo_simples,literal_dinamico
Models: all
Save models: ✅
```

---

## 📦 Baixar Resultados

Após a execução de qualquer workflow:

1. Vá para a página do workflow executado
2. Role até **"Artifacts"**
3. Baixe os arquivos:
   - **experiment-results**: CSVs e relatório
   - **trained-models**: Modelos `.joblib`

---

## 🔧 Configuração de Cache

Os workflows usam cache para:
- ✅ **Embeddings SBERT** (`cache/embeddings`)
- ✅ **Modelos PyTorch** (`~/.cache/torch`)

Isso acelera execuções subsequentes evitando re-download de modelos grandes.

---

## 📊 Visualizar Resultados

### No GitHub Actions

Após a execução, veja o **Summary** do workflow:
- Configuração usada
- Relatório de resultados
- Links para artifacts

### Localmente

Baixe os artifacts e visualize:

```bash
# Descompactar artifact
unzip experiment-results.zip

# Ver resultados
cat reports/experiments_report.md

# Carregar CSV
python -c "import pandas as pd; print(pd.read_csv('results.csv'))"
```

---

## 🛠️ Manutenção

### Ajustar Timeout

Se os experimentos demorarem muito, edite o timeout em `.github/workflows/run-experiments.yml`:

```yaml
- name: Run all experiments
  run: |
    uv run python src/ep1/experiments.py
  timeout-minutes: 240  # Aumentar para 4 horas
```

### Desabilitar Schedule

Para não rodar automaticamente todo domingo, comente a seção `schedule` em `run-experiments.yml`:

```yaml
# schedule:
#   - cron: '0 0 * * 0'
```

### Mudar Retenção de Artifacts

Ajuste `retention-days` conforme necessário:

```yaml
- name: Upload results
  uses: actions/upload-artifact@v4
  with:
    name: experiment-results
    retention-days: 180  # Manter por 6 meses
```

---

## 🔐 Secrets e Variáveis

Este projeto não requer secrets especiais. Todos os workflows usam apenas:
- `GITHUB_TOKEN` (fornecido automaticamente)

Se precisar adicionar secrets (ex: para deploy), vá em:
**Settings → Secrets and variables → Actions**

---

## 📝 Logs e Debugging

Para ver logs detalhados:

1. Vá para **Actions**
2. Clique no workflow executado
3. Clique em um job (ex: `run-experiments`)
4. Expanda os steps para ver output

Para debugging local antes de commitar:

```bash
# Testar se o workflow funcionaria
uv sync
uv run python src/ep1/experiments.py
uv run python src/ep1/report.py
```

---

## 🎯 Próximos Passos

1. **Primeira execução**: Rode o workflow CI para validar tudo
2. **Experimentos**: Execute "Train Specific Models" com poucos modelos
3. **Full run**: Execute "Run ML Experiments" para treinar tudo
4. **Análise**: Baixe os artifacts e analise os resultados

---

## 📚 Recursos

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Manual Workflows](https://docs.github.com/en/actions/using-workflows/manually-running-a-workflow)

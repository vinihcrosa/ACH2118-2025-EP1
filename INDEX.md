# 📚 Índice de Documentação - ACH2118-2025-EP1

## 🎯 Começar Aqui

| Documento | Descrição | Quando Usar |
|-----------|-----------|-------------|
| **[PREDICTION_SUMMARY.md](PREDICTION_SUMMARY.md)** | ⭐ Resumo rápido de predição | Primeira vez usando modelos |
| **[HOW_TO_PREDICT.md](HOW_TO_PREDICT.md)** | Guia completo de predição | Referência detalhada |
| **[README.md](README.md)** | Visão geral do projeto | Entender o projeto |

## 📖 Documentação por Tópico

### 🔮 Usar Modelos Treinados (Predição)

1. **[PREDICTION_SUMMARY.md](PREDICTION_SUMMARY.md)** - Resumo rápido com exemplos
2. **[HOW_TO_PREDICT.md](HOW_TO_PREDICT.md)** - Guia completo com 3 formas de usar
3. **[PREDICT_GUIDE.md](PREDICT_GUIDE.md)** - Guia detalhado com casos de uso avançados

**Scripts:**
- `predict_cli.py` - CLI interativa para predição
- `examples_inference.py` - 7 exemplos práticos executáveis
- `src/ep1/inference.py` - Módulo Python completo

**Comandos rápidos:**
```bash
# Ver modelos
uv run predict_cli.py --list-models

# Classificar texto
uv run predict_cli.py --model arcaico_moderno__tfidf_lr --text "Seu texto" --proba

# Ver exemplos
uv run examples_inference.py
```

### ⚙️ Configuração de Pipelines (JSON)

**👉 COMECE AQUI se quer entender as configurações!**

1. **[CONFIG_SIMPLE.md](CONFIG_SIMPLE.md)** - ⭐ Resumo ultra simples (LEIA PRIMEIRO!)
2. **[CONFIG_EXPLAINED.md](CONFIG_EXPLAINED.md)** - Explicação detalhada com exemplos
3. **[QUICKSTART.md](QUICKSTART.md)** - Guia rápido de uso
4. **[config/README.md](config/README.md)** - Documentação completa do sistema JSON
5. **[MIGRATION.md](MIGRATION.md)** - Detalhes da migração para JSON

**Arquivos:**
- `config/pipelines.json` - Configuração principal
- `config/pipelines.example.json` - Exemplo de configuração customizada
- `src/ep1/config.py` - Módulo de gerenciamento de configuração

**Scripts interativos:**
- `tutorial_config.py` - Tutorial interativo passo a passo
- `examples_config.py` - Exemplos de uso

**Comandos rápidos:**
```bash
# Tutorial interativo (RECOMENDADO!)
uv run tutorial_config.py

# Ver exemplos de configuração
uv run examples_config.py

# Treinar modelo do JSON
uv run src/ep1/train.py --dataset arcaico_moderno --model tfidf_lr --save
```

### 🧪 Experimentos e Treinamento

**Scripts principais:**
- `src/ep1/train.py` - Treinar modelo individual
- `src/ep1/experiments.py` - Executar grid de experimentos
- `src/ep1/report.py` - Gerar relatórios

**Comandos:**
```bash
# Treinar modelo
uv run src/ep1/train.py --dataset DATASET --model MODELO --cv 10 --save

# Executar experimentos
uv run python -m src.ep1.experiments

# Gerar relatório
uv run python -m src.ep1.report --input experiments.csv
```

## 📁 Estrutura de Arquivos

```
ACH2118-2025-EP1/
├── 📚 Documentação
│   ├── README.md                    # Visão geral
│   ├── PREDICTION_SUMMARY.md        # ⭐ Resumo de predição
│   ├── HOW_TO_PREDICT.md           # 🎯 Guia completo de predição
│   ├── PREDICT_GUIDE.md            # Guia detalhado
│   ├── QUICKSTART.md               # Início rápido JSON
│   ├── MIGRATION.md                # Migração para JSON
│   └── config/README.md            # Docs de configuração
│
├── ⚙️ Configuração
│   └── config/
│       ├── pipelines.json          # Configuração principal
│       └── pipelines.example.json  # Exemplo
│
├── 🔧 Scripts Executáveis
│   ├── predict_cli.py              # CLI de predição
│   ├── examples_inference.py       # Exemplos de predição
│   └── examples_config.py          # Exemplos de configuração
│
├── 📦 Código Fonte
│   └── src/ep1/
│       ├── config.py               # Gerenciamento de config
│       ├── inference.py            # Módulo de predição
│       ├── train.py                # Treinar modelos
│       ├── experiments.py          # Grid de experimentos
│       ├── predict.py              # Script de predição legado
│       └── models/                 # Definições de modelos
│
├── 💾 Dados e Modelos
│   ├── data/                       # Datasets de treino
│   │   ├── train_arcaico_moderno.csv
│   │   ├── train_complexo_simples.csv
│   │   └── train_literal_dinamico.csv
│   │
│   └── models/                     # Modelos treinados (.joblib)
│       ├── arcaico_moderno__tfidf_lr.joblib
│       ├── complexo_simples__tfidf_lr.joblib
│       └── literal_dinamico__tfidf_lr.joblib
│
└── 📊 Resultados
    ├── experiments.csv             # Resultados de experimentos
    ├── results.csv                 # Resultados de treino
    └── reports/                    # Relatórios gerados
```

## 🚀 Fluxos de Trabalho Comuns

### 1. Usar Modelo Existente

```bash
# Passo 1: Ver modelos disponíveis
uv run predict_cli.py --list-models

# Passo 2: Classificar texto
uv run predict_cli.py --model arcaico_moderno__tfidf_lr --text "Seu texto" --proba

# Passo 3: Processar CSV (opcional)
uv run predict_cli.py --model arcaico_moderno__tfidf_lr --csv dados.csv
```

**Documentação:** [PREDICTION_SUMMARY.md](PREDICTION_SUMMARY.md)

### 2. Treinar Novo Modelo

```bash
# Passo 1: Editar configuração (opcional)
# Edite config/pipelines.json

# Passo 2: Treinar
uv run src/ep1/train.py --dataset arcaico_moderno --model tfidf_lr --cv 10 --save

# Passo 3: Usar modelo treinado
uv run predict_cli.py --model arcaico_moderno__tfidf_lr --text "Teste"
```

**Documentação:** [QUICKSTART.md](QUICKSTART.md)

### 3. Executar Experimentos

```bash
# Passo 1: Configurar experimentos
# Edite config/pipelines.json

# Passo 2: Executar
uv run python -m src.ep1.experiments

# Passo 3: Gerar relatório
uv run python -m src.ep1.report --input experiments.csv
```

**Documentação:** [config/README.md](config/README.md)

### 4. Adicionar Novo Modelo

```bash
# Passo 1: Editar config/pipelines.json
# Adicionar modelo e experimentos

# Passo 2: Testar configuração
uv run examples_config.py

# Passo 3: Treinar
uv run src/ep1/train.py --dataset DATASET --model NOVO_MODELO --save
```

**Documentação:** [config/README.md](config/README.md)

## 🎓 Tutoriais e Exemplos

| Script | Descrição | Comando |
|--------|-----------|---------|
| `examples_inference.py` | 7 exemplos de predição | `uv run examples_inference.py` |
| `examples_config.py` | Exemplos de configuração | `uv run examples_config.py` |
| `predict_cli.py --help` | Ajuda do CLI | `uv run predict_cli.py --help` |

## 🔍 Busca Rápida

**Quero...**

- **Classificar um texto** → [PREDICTION_SUMMARY.md](PREDICTION_SUMMARY.md) ou `uv run predict_cli.py --help`
- **Processar CSV** → [HOW_TO_PREDICT.md](HOW_TO_PREDICT.md) seção "Processar CSV"
- **Treinar modelo** → [QUICKSTART.md](QUICKSTART.md) seção "Treinar Novo Modelo"
- **Adicionar modelo** → [config/README.md](config/README.md) seção "Adicionar Novo Modelo"
- **Ver probabilidades** → [PREDICT_GUIDE.md](PREDICT_GUIDE.md) seção "Predição com Probabilidades"
- **Comparar modelos** → `uv run predict_cli.py --compare "Texto"`
- **Executar experimentos** → [README.md](README.md) seção "Como rodar os experimentos"

## 💡 Dicas

1. **Primeira vez?** Comece com [PREDICTION_SUMMARY.md](PREDICTION_SUMMARY.md)
2. **Quer exemplos?** Execute `uv run examples_inference.py`
3. **Não sabe o comando?** Use `uv run predict_cli.py --help`
4. **Quer entender tudo?** Leia [config/README.md](config/README.md)

## 📞 Suporte

- 🐛 Problemas? Ver seção "Troubleshooting" em cada guia
- 📖 Mais detalhes? Cada documento tem seção "Ver mais"
- 💻 Exemplos de código? Todos os arquivos `examples_*.py`

---

**Última atualização:** 10 de outubro de 2025

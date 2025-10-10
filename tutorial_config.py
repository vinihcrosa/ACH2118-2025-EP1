"""
Tutorial Interativo: Entendendo a Configuração JSON

Execute este arquivo e siga as instruções para entender como funciona
o sistema de configuração.
"""

import json
from pathlib import Path
from src.ep1.config import get_default_config, create_model_from_config


def separador(titulo):
    """Imprime um separador visual."""
    print("\n" + "="*70)
    print(f"  {titulo}")
    print("="*70 + "\n")


def exemplo_1_ler_json():
    """Mostra como o JSON está estruturado."""
    separador("EXEMPLO 1: Estrutura do JSON")
    
    config_path = Path("config/pipelines.json")
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config_data = json.load(f)
    
    print("📄 O arquivo JSON tem estas seções:\n")
    for secao in config_data.keys():
        print(f"  ✓ {secao}")
    
    print("\n" + "-"*70)
    print("DATASETS (quais datasets existem):")
    print("-"*70)
    for nome, arquivo in config_data['datasets'].items():
        print(f"  {nome:20s} → {arquivo}")
    
    print("\n" + "-"*70)
    print("CV_CONFIG (configuração de cross-validation):")
    print("-"*70)
    for chave, valor in config_data['cv_config'].items():
        print(f"  {chave:20s} = {valor}")
    
    print("\n" + "-"*70)
    print("MODELS (modelos disponíveis):")
    print("-"*70)
    for nome in config_data['models'].keys():
        print(f"  ✓ {nome}")
    
    print("\n" + "-"*70)
    print("EXPERIMENTS (quantos experimentos configurados):")
    print("-"*70)
    print(f"  Total: {len(config_data['experiments'])} experimentos")


def exemplo_2_anatomia_modelo():
    """Mostra em detalhes como um modelo é definido."""
    separador("EXEMPLO 2: Anatomia de um Modelo")
    
    config_path = Path("config/pipelines.json")
    with open(config_path, 'r', encoding='utf-8') as f:
        config_data = json.load(f)
    
    # Pegar o modelo tfidf_lr como exemplo
    modelo = config_data['models']['tfidf_lr']
    
    print("🔍 Vamos dissecar o modelo 'tfidf_lr':\n")
    print(json.dumps(modelo, indent=2))
    
    print("\n" + "-"*70)
    print("📖 Tradução:")
    print("-"*70)
    
    print(f"\n1. Tipo do modelo: {modelo['type']}")
    print("   → Significa: Pipeline padrão do sklearn\n")
    
    print("2. Steps (etapas) do pipeline:")
    for i, step in enumerate(modelo['steps'], 1):
        print(f"\n   Step {i}: {step['name']}")
        print(f"   ├─ Classe: {step['class']}")
        print(f"   └─ Parâmetros: {step['params']}")
    
    print("\n" + "-"*70)
    print("💻 Equivalente em Python:")
    print("-"*70)
    print("""
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=2000, n_jobs=1))
])
    """)


def exemplo_3_criar_modelo():
    """Mostra como o sistema cria um modelo a partir do JSON."""
    separador("EXEMPLO 3: Criando Modelo a partir do JSON")
    
    print("📦 Carregando configuração...\n")
    config = get_default_config()
    
    print("✅ Configuração carregada!")
    print(f"   Modelos disponíveis: {list(config.models.keys())}\n")
    
    print("-"*70)
    print("🔨 Criando modelo 'tfidf_lr'...")
    print("-"*70)
    
    model = config.get_model("tfidf_lr")
    
    print("\n✅ Modelo criado com sucesso!\n")
    print(f"Tipo: {type(model)}")
    print(f"Pipeline: {model}\n")
    
    print("Steps do pipeline:")
    for step_name, step_obj in model.steps:
        print(f"  {step_name}: {step_obj.__class__.__name__}")
        
        # Mostrar alguns parâmetros
        if hasattr(step_obj, 'get_params'):
            params = step_obj.get_params()
            params_importantes = {k: v for k, v in params.items() 
                                 if k in ['max_iter', 'n_jobs', 'max_features']}
            if params_importantes:
                print(f"      Parâmetros: {params_importantes}")


def exemplo_4_experimentos():
    """Mostra como os experimentos são configurados."""
    separador("EXEMPLO 4: Entendendo Experimentos")
    
    config_path = Path("config/pipelines.json")
    with open(config_path, 'r', encoding='utf-8') as f:
        config_data = json.load(f)
    
    # Pegar primeiro experimento
    exp = config_data['experiments'][0]
    
    print("🧪 Primeiro experimento configurado:\n")
    print(json.dumps(exp, indent=2))
    
    print("\n" + "-"*70)
    print("📖 Explicação:")
    print("-"*70)
    
    print(f"\nModelo testado: {exp['model']}")
    print("\nParâmetros a testar (param_grid):")
    
    for param, valores in exp['param_grid'].items():
        step, param_name = param.split('__')
        print(f"\n  {param}:")
        print(f"    Step: {step}")
        print(f"    Parâmetro: {param_name}")
        print(f"    Valores: {valores}")
    
    # Calcular total de combinações
    import itertools
    total_combos = 1
    for valores in exp['param_grid'].values():
        total_combos *= len(valores)
    
    print(f"\n📊 Total de combinações a testar: {total_combos}")
    
    print("\n" + "-"*70)
    print("Algumas combinações que serão testadas:")
    print("-"*70)
    
    # Mostrar algumas combinações
    keys = list(exp['param_grid'].keys())
    values = list(exp['param_grid'].values())
    
    for i, combo in enumerate(itertools.product(*values)):
        if i >= 3:  # Mostrar só 3
            print("  ...")
            break
        params = dict(zip(keys, combo))
        print(f"\n  Combinação {i+1}:")
        for k, v in params.items():
            print(f"    {k} = {v}")


def exemplo_5_adicionar_modelo():
    """Exemplo de como adicionar um novo modelo."""
    separador("EXEMPLO 5: Como Adicionar Novo Modelo")
    
    print("📝 Para adicionar um novo modelo, você precisa:\n")
    
    print("1️⃣ Adicionar na seção 'models':")
    print("-"*70)
    novo_modelo = {
        "meu_modelo": {
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
    print(json.dumps(novo_modelo, indent=2))
    
    print("\n2️⃣ Adicionar na seção 'experiments' (opcional):")
    print("-"*70)
    novo_exp = {
        "model": "meu_modelo",
        "param_grid": {
            "vectorizer__max_features": [3000, 5000, 10000],
            "clf__alpha": [0.5, 1.0, 2.0]
        }
    }
    print(json.dumps(novo_exp, indent=2))
    
    print("\n3️⃣ Usar o modelo:")
    print("-"*70)
    print("""
# Treinar
uv run src/ep1/train.py --dataset arcaico_moderno --model meu_modelo --save

# Predizer
uv run predict_cli.py --model meu_modelo --text "Teste"
    """)


def exemplo_6_tipos_modelos():
    """Compara os dois tipos de modelos."""
    separador("EXEMPLO 6: Tipos de Modelos")
    
    print("Existem 2 tipos de modelos no sistema:\n")
    
    print("="*70)
    print("TIPO 1: sklearn_pipeline")
    print("="*70)
    print("""
Para: Modelos padrão do scikit-learn
Quando usar: Quando você só precisa de classes do sklearn

Exemplo:
{
  "type": "sklearn_pipeline",
  "steps": [
    {
      "name": "vectorizer",
      "class": "sklearn.feature_extraction.text.TfidfVectorizer",
      "params": {"max_features": 5000}
    },
    {
      "name": "clf",
      "class": "sklearn.linear_model.LogisticRegression",
      "params": {"max_iter": 2000}
    }
  ]
}

Classes disponíveis:
  - sklearn.feature_extraction.text.*
  - sklearn.linear_model.*
  - sklearn.ensemble.*
  - sklearn.svm.*
  - sklearn.naive_bayes.*
  - ... e qualquer outra do sklearn!
    """)
    
    print("\n" + "="*70)
    print("TIPO 2: custom")
    print("="*70)
    print("""
Para: Modelos que precisam de código Python especial
Quando usar: SBERT, PyTorch, TensorFlow, ou lógica customizada

Exemplo:
{
  "type": "custom",
  "factory": "src.ep1.models.sbert.create_sbert_lr",
  "params": {}
}

Você precisa criar a função Python:

# src/ep1/models/sbert.py
def create_sbert_lr():
    # Seu código especial aqui
    return pipeline
    """)


def exemplo_7_parametros():
    """Explica como funcionam os parâmetros."""
    separador("EXEMPLO 7: Entendendo Parâmetros")
    
    print("📋 Formato dos parâmetros no param_grid:\n")
    print("  'step__parametro': [valores]\n")
    
    print("-"*70)
    print("Exemplo 1: Parâmetros do vectorizer")
    print("-"*70)
    print("""
Pipeline:
  steps: [
    {"name": "tfidf", ...},    ← Este é o step
    {"name": "clf", ...}
  ]

Para acessar parâmetros do TfidfVectorizer:
  "tfidf__max_features": [3000, 5000]
   ^^^^^ ^^^^^^^^^^^^
   step   parâmetro

Outros exemplos:
  "tfidf__ngram_range": [[1,1], [1,3]]
  "tfidf__min_df": [1, 2, 5]
    """)
    
    print("\n" + "-"*70)
    print("Exemplo 2: Parâmetros do classificador")
    print("-"*70)
    print("""
Pipeline:
  steps: [
    {"name": "tfidf", ...},
    {"name": "clf", ...}       ← Este é o step
  ]

Para acessar parâmetros do LogisticRegression:
  "clf__C": [0.1, 1.0, 10.0]
   ^^^  ^
   step parâmetro

Outros exemplos:
  "clf__max_iter": [1000, 2000]
  "clf__penalty": ["l1", "l2"]
    """)
    
    print("\n" + "-"*70)
    print("💡 Dica: Como saber quais parâmetros existem?")
    print("-"*70)
    print("""
1. Documentação do sklearn:
   https://scikit-learn.org/stable/modules/classes.html

2. Python:
   from sklearn.linear_model import LogisticRegression
   help(LogisticRegression)

3. Ver modelo criado:
   model = config.get_model("tfidf_lr")
   print(model.get_params())
    """)


def menu_interativo():
    """Menu principal do tutorial."""
    print("\n" + "🎓" + " TUTORIAL INTERATIVO: CONFIGURAÇÃO JSON ".center(68, "="))
    print("\nEste tutorial explica como funciona o sistema de configuração JSON.")
    print("Execute os exemplos na ordem ou escolha um específico.\n")
    
    exemplos = [
        ("Estrutura do JSON", exemplo_1_ler_json),
        ("Anatomia de um Modelo", exemplo_2_anatomia_modelo),
        ("Criar Modelo do JSON", exemplo_3_criar_modelo),
        ("Entender Experimentos", exemplo_4_experimentos),
        ("Adicionar Novo Modelo", exemplo_5_adicionar_modelo),
        ("Tipos de Modelos", exemplo_6_tipos_modelos),
        ("Entender Parâmetros", exemplo_7_parametros),
    ]
    
    print("📚 Exemplos disponíveis:\n")
    for i, (titulo, _) in enumerate(exemplos, 1):
        print(f"  {i}. {titulo}")
    
    print("\n" + "="*70)
    
    # Executar todos
    for titulo, funcao in exemplos:
        try:
            funcao()
            input("\n⏸️  Pressione ENTER para continuar...")
        except Exception as e:
            print(f"\n❌ Erro no exemplo: {e}")
            import traceback
            traceback.print_exc()
    
    separador("✅ TUTORIAL CONCLUÍDO")
    
    print("""
🎉 Parabéns! Você completou o tutorial.

📝 Resumo do que aprendeu:
  1. O JSON tem 4 seções: datasets, cv_config, models, experiments
  2. Modelos tipo "sklearn_pipeline" usam classes do sklearn
  3. Modelos tipo "custom" usam funções Python
  4. param_grid define quais parâmetros testar
  5. Formato: "step__parametro": [valores]

🚀 Próximos passos:
  1. Abra config/pipelines.json
  2. Tente modificar um parâmetro
  3. Adicione um novo modelo
  4. Execute: uv run src/ep1/train.py --help

💡 Dúvidas? Consulte:
  - CONFIG_EXPLAINED.md (explicação detalhada)
  - config/README.md (documentação completa)
  - examples_config.py (mais exemplos)

    """)


if __name__ == "__main__":
    menu_interativo()

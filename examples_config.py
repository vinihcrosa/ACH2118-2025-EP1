"""
Exemplo de uso da configuração JSON para pipelines.

Este script demonstra como usar o novo sistema de configuração baseado em JSON.
"""

from src.ep1.config import get_default_config, PipelineConfig
from src.ep1.data import load_dataset
from sklearn.model_selection import cross_val_score, StratifiedKFold


def exemplo_basico():
    """Exemplo básico de uso da configuração."""
    print("=== Exemplo Básico ===\n")
    
    # Carregar configuração padrão
    config = get_default_config()
    
    # Ver datasets disponíveis
    print("Datasets disponíveis:")
    for name, file in config.datasets.items():
        print(f"  - {name}: {file}")
    
    # Ver modelos disponíveis
    print("\nModelos disponíveis:")
    for model_name in config.models.keys():
        print(f"  - {model_name}")
    
    # Criar um modelo
    print("\nCriando modelo tfidf_lr...")
    model = config.get_model("tfidf_lr")
    print(f"Modelo criado: {model}")


def exemplo_treinamento():
    """Exemplo de treinamento usando a configuração."""
    print("\n\n=== Exemplo de Treinamento ===\n")
    
    config = get_default_config()
    
    # Carregar dados
    dataset_name = "arcaico_moderno"
    dataset_file = config.datasets[dataset_name]
    print(f"Carregando dataset: {dataset_name}")
    X, y = load_dataset(dataset_file)
    print(f"Dataset carregado: {len(X)} exemplos")
    
    # Criar modelo
    model_name = "tfidf_lr"
    print(f"\nCriando modelo: {model_name}")
    model = config.get_model(model_name)
    
    # Cross-validation
    cv_config = config.cv_config
    cv = StratifiedKFold(
        n_splits=cv_config["n_folds"],
        shuffle=True,
        random_state=cv_config["random_state"]
    )
    
    print(f"Executando {cv_config['n_folds']}-fold cross-validation...")
    scores = cross_val_score(model, X, y, cv=cv, scoring="accuracy")
    
    print(f"\nResultados:")
    print(f"  Acurácia média: {scores.mean():.4f}")
    print(f"  Desvio padrão: {scores.std():.4f}")
    print(f"  Scores: {scores}")


def exemplo_configuracao_customizada():
    """Exemplo usando um arquivo de configuração customizado."""
    print("\n\n=== Exemplo com Configuração Customizada ===\n")
    
    # Você pode criar sua própria configuração
    # config = PipelineConfig("caminho/para/meu_config.json")
    
    # Ou usar a padrão
    config = get_default_config()
    
    # Modificar configurações em memória (não salva no arquivo)
    print("Configurações de CV atuais:")
    print(f"  N folds: {config.cv_config['n_folds']}")
    print(f"  Random state: {config.cv_config['random_state']}")


def exemplo_experimentos():
    """Exemplo de acesso aos experimentos configurados."""
    print("\n\n=== Exemplo de Experimentos ===\n")
    
    config = get_default_config()
    
    # Obter lista de experimentos
    experiments = config.get_experiments()
    
    print(f"Total de experimentos configurados: {len(experiments)}")
    print("\nPrimeiros 3 experimentos:")
    
    for i, (model_name, model_factory, param_grid) in enumerate(experiments[:3]):
        print(f"\n{i+1}. Modelo: {model_name}")
        print(f"   Parâmetros a testar:")
        for param, values in param_grid.items():
            print(f"     - {param}: {values}")


def exemplo_adicionar_modelo_runtime():
    """Exemplo de como você poderia modificar a configuração em runtime."""
    print("\n\n=== Exemplo: Informações sobre Modelos ===\n")
    
    config = get_default_config()
    
    # Inspecionar um modelo específico
    model_name = "tfidf_lr"
    model_config = config.models[model_name]
    
    print(f"Configuração do modelo '{model_name}':")
    print(f"  Tipo: {model_config['type']}")
    
    if model_config['type'] == 'sklearn_pipeline':
        print(f"  Steps:")
        for step in model_config['steps']:
            print(f"    - {step['name']}: {step['class']}")
            if step['params']:
                print(f"      Params: {step['params']}")
    
    # Criar e inspecionar o modelo
    model = config.get_model(model_name)
    print(f"\n  Pipeline criado: {model}")
    print(f"  Steps do pipeline:")
    for name, estimator in model.steps:
        print(f"    - {name}: {estimator.__class__.__name__}")


if __name__ == "__main__":
    # Executar todos os exemplos
    exemplo_basico()
    exemplo_treinamento()
    exemplo_configuracao_customizada()
    exemplo_experimentos()
    exemplo_adicionar_modelo_runtime()
    
    print("\n\n" + "="*60)
    print("✅ Exemplos concluídos com sucesso!")
    print("="*60)

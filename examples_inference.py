"""
Exemplos práticos de uso da inferência com modelos treinados.

Execute este arquivo para ver diferentes formas de usar modelos salvos.
"""

from pathlib import Path
import pandas as pd
from src.ep1.inference import (
    ModelPredictor,
    load_all_models,
    predict_with_all_models,
    quick_predict
)


def exemplo_1_basico():
    """Exemplo básico: carregar modelo e fazer predição."""
    print("\n" + "="*70)
    print("EXEMPLO 1: Predição Básica")
    print("="*70)
    
    # Verificar se existem modelos
    models_dir = Path("models")
    model_files = list(models_dir.glob("*.joblib"))
    
    if not model_files:
        print("⚠️  Nenhum modelo encontrado em /models")
        print("   Execute: uv run src/ep1/train.py --dataset arcaico_moderno --model tfidf_lr --save")
        return
    
    # Usar o primeiro modelo disponível
    model_path = model_files[0]
    print(f"\n📦 Carregando modelo: {model_path.name}")
    
    predictor = ModelPredictor(model_path)
    print(f"   Classes: {list(predictor.classes)}")
    
    # Fazer predições
    textos = [
        "Este é um exemplo de texto moderno e contemporâneo",
        "Outrossim, cumpre-nos manifestar nosso intento",
        "A inteligência artificial está revolucionando tudo"
    ]
    
    print("\n🔮 Fazendo predições:")
    predicoes = predictor.predict(textos)
    
    for texto, pred in zip(textos, predicoes):
        print(f"   '{texto[:50]}...' → {pred}")


def exemplo_2_com_probabilidades():
    """Exemplo com probabilidades e confiança."""
    print("\n" + "="*70)
    print("EXEMPLO 2: Predições com Probabilidades")
    print("="*70)
    
    models_dir = Path("models")
    model_files = list(models_dir.glob("*.joblib"))
    
    if not model_files:
        print("⚠️  Nenhum modelo encontrado")
        return
    
    predictor = ModelPredictor(model_files[0])
    
    textos = [
        "Texto com características muito claras",
        "Texto ambíguo que pode ser classificado de várias formas"
    ]
    
    print(f"\n📊 Predições com confiança:")
    df = predictor.predict_with_confidence(textos)
    
    # Mostrar resultado formatado
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 50)
    
    print(df.to_string(index=False))
    
    # Analisar confiança
    print(f"\n📈 Análise de confiança:")
    print(f"   Confiança média: {df['confidence'].mean():.2%}")
    print(f"   Confiança mínima: {df['confidence'].min():.2%}")
    print(f"   Confiança máxima: {df['confidence'].max():.2%}")


def exemplo_3_csv():
    """Exemplo: processar arquivo CSV."""
    print("\n" + "="*70)
    print("EXEMPLO 3: Processar CSV")
    print("="*70)
    
    models_dir = Path("models")
    model_files = list(models_dir.glob("*.joblib"))
    
    if not model_files:
        print("⚠️  Nenhum modelo encontrado")
        return
    
    # Criar CSV de exemplo
    csv_exemplo = "exemplo_textos.csv"
    df_exemplo = pd.DataFrame({
        'text': [
            "Primeiro texto para classificar",
            "Segundo texto com características diferentes",
            "Terceiro texto de exemplo",
            "Quarto e último texto"
        ],
        'id': [1, 2, 3, 4]
    })
    
    print(f"\n📝 Criando CSV de exemplo: {csv_exemplo}")
    df_exemplo.to_csv(csv_exemplo, sep=';', index=False, encoding='ISO-8859-1')
    print(f"   {len(df_exemplo)} linhas criadas")
    
    # Processar CSV
    predictor = ModelPredictor(model_files[0])
    
    print(f"\n🔄 Processando CSV com modelo: {model_files[0].name}")
    resultado = predictor.predict_from_csv(
        csv_exemplo,
        output_csv="exemplo_resultado.csv",
        include_probabilities=True,
        sep=';',
        encoding='ISO-8859-1'
    )
    
    print(f"\n✅ Resultado:")
    print(resultado[['id', 'text', 'prediction', 'confidence']].to_string(index=False))
    
    # Limpar arquivos de exemplo
    Path(csv_exemplo).unlink(missing_ok=True)
    Path("exemplo_resultado.csv").unlink(missing_ok=True)
    print("\n🗑️  Arquivos de exemplo removidos")


def exemplo_4_multiplos_modelos():
    """Exemplo: aplicar múltiplos modelos."""
    print("\n" + "="*70)
    print("EXEMPLO 4: Múltiplos Modelos")
    print("="*70)
    
    models_dir = Path("models")
    
    print("\n📦 Carregando todos os modelos disponíveis...")
    modelos = load_all_models(models_dir)
    
    if not modelos:
        print("⚠️  Nenhum modelo encontrado")
        return
    
    print(f"\n✅ {len(modelos)} modelo(s) carregado(s)")
    
    # Aplicar todos os modelos
    textos = [
        "Este é um texto moderno e contemporâneo",
        "Outrossim, manifesto meu intento"
    ]
    
    print(f"\n🔮 Aplicando todos os modelos:")
    df = predict_with_all_models(textos, models_dir)
    
    print(df.to_string(index=False))


def exemplo_5_filtragem_confianca():
    """Exemplo: filtrar por confiança."""
    print("\n" + "="*70)
    print("EXEMPLO 5: Filtrar por Confiança")
    print("="*70)
    
    models_dir = Path("models")
    model_files = list(models_dir.glob("*.joblib"))
    
    if not model_files:
        print("⚠️  Nenhum modelo encontrado")
        return
    
    predictor = ModelPredictor(model_files[0])
    
    # Criar dados de teste
    textos = [
        f"Texto de exemplo número {i} com características variadas"
        for i in range(10)
    ]
    
    print(f"\n🔮 Fazendo predições para {len(textos)} textos...")
    df = predictor.predict_with_confidence(textos)
    
    # Filtrar por confiança
    limiar = 0.7
    df_confiavel = df[df['confidence'] >= limiar]
    df_incerto = df[df['confidence'] < limiar]
    
    print(f"\n📊 Análise de confiança (limiar = {limiar:.0%}):")
    print(f"   Total: {len(df)}")
    print(f"   Confiável (≥{limiar:.0%}): {len(df_confiavel)} ({len(df_confiavel)/len(df)*100:.1f}%)")
    print(f"   Incerto (<{limiar:.0%}): {len(df_incerto)} ({len(df_incerto)/len(df)*100:.1f}%)")
    
    if len(df_incerto) > 0:
        print(f"\n⚠️  Textos com baixa confiança:")
        for idx, row in df_incerto.iterrows():
            print(f"   '{row['text'][:40]}...' → {row['prediction']} ({row['confidence']:.2%})")


def exemplo_6_quick_predict():
    """Exemplo: uso rápido com quick_predict."""
    print("\n" + "="*70)
    print("EXEMPLO 6: Predição Rápida (quick_predict)")
    print("="*70)
    
    models_dir = Path("models")
    model_files = list(models_dir.glob("*.joblib"))
    
    if not model_files:
        print("⚠️  Nenhum modelo encontrado")
        return
    
    # Pegar nome do modelo (sem extensão)
    model_name = model_files[0].stem
    
    print(f"\n⚡ Usando quick_predict com: {model_name}")
    
    texto = "Este é um texto para classificação rápida"
    resultado = quick_predict(model_name, texto)
    
    print(f"\n   Texto: '{texto}'")
    print(f"   Predição: {resultado[0]}")


def exemplo_7_info_modelo():
    """Exemplo: inspecionar informações do modelo."""
    print("\n" + "="*70)
    print("EXEMPLO 7: Informações do Modelo")
    print("="*70)
    
    models_dir = Path("models")
    model_files = list(models_dir.glob("*.joblib"))
    
    if not model_files:
        print("⚠️  Nenhum modelo encontrado")
        return
    
    for model_file in model_files:
        predictor = ModelPredictor(model_file)
        
        print(f"\n📋 {model_file.name}")
        print(f"   Classes: {list(predictor.classes)}")
        print(f"   Número de classes: {len(predictor.classes)}")
        
        if hasattr(predictor.model, 'steps'):
            print(f"   Pipeline steps:")
            for step_name, step_obj in predictor.model.steps:
                print(f"      - {step_name}: {step_obj.__class__.__name__}")


def main():
    """Executa todos os exemplos."""
    print("\n" + "🎯" + " EXEMPLOS DE INFERÊNCIA COM MODELOS TREINADOS ".center(68, "="))
    
    exemplos = [
        exemplo_1_basico,
        exemplo_2_com_probabilidades,
        exemplo_3_csv,
        exemplo_4_multiplos_modelos,
        exemplo_5_filtragem_confianca,
        exemplo_6_quick_predict,
        exemplo_7_info_modelo
    ]
    
    for exemplo in exemplos:
        try:
            exemplo()
        except Exception as e:
            print(f"\n❌ Erro no {exemplo.__name__}: {e}")
    
    print("\n" + "="*70)
    print("✅ Exemplos concluídos!")
    print("="*70)
    print("\n💡 Dicas:")
    print("   - Use ModelPredictor para controle completo")
    print("   - Use quick_predict para predições rápidas")
    print("   - Use predict_with_all_models para comparar modelos")
    print("   - Sempre verifique a confiança das predições")
    print("\n📚 Mais informações: PREDICT_GUIDE.md")
    print()


if __name__ == "__main__":
    main()

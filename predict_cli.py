#!/usr/bin/env python
"""
Script CLI para fazer predições com modelos treinados de forma simples.

Uso:
    uv run predict_cli.py --model arcaico_moderno__tfidf_lr --text "Seu texto aqui"
    uv run predict_cli.py --model arcaico_moderno__tfidf_lr --csv dados.csv
    uv run predict_cli.py --list-models
"""

import argparse
import sys
from pathlib import Path
from src.ep1.inference import ModelPredictor, load_all_models


def list_models():
    """Lista todos os modelos disponíveis."""
    models_dir = Path("models")
    
    if not models_dir.exists():
        print("❌ Diretório 'models' não encontrado")
        return
    
    model_files = list(models_dir.glob("*.joblib"))
    
    if not model_files:
        print("⚠️  Nenhum modelo encontrado em /models")
        print("\n💡 Dica: Treine um modelo primeiro:")
        print("   uv run src/ep1/train.py --dataset arcaico_moderno --model tfidf_lr --save")
        return
    
    print(f"\n📦 Modelos disponíveis ({len(model_files)}):\n")
    
    for model_file in sorted(model_files):
        try:
            predictor = ModelPredictor(model_file)
            print(f"  ✓ {model_file.stem}")
            print(f"    Classes: {', '.join(predictor.classes)}")
        except Exception as e:
            print(f"  ✗ {model_file.stem} (erro ao carregar: {e})")
    
    print()


def predict_text(model_name: str, text: str, show_proba: bool = False):
    """Faz predição para um texto."""
    model_path = Path("models") / f"{model_name}.joblib"
    
    if not model_path.exists():
        print(f"❌ Modelo não encontrado: {model_path}")
        print("\n💡 Use --list-models para ver modelos disponíveis")
        return
    
    try:
        predictor = ModelPredictor(model_path)
        
        prediction = predictor.predict([text])[0]
        
        print(f"\n📝 Texto: {text}")
        print(f"🎯 Predição: {prediction}")
        
        if show_proba:
            proba = predictor.predict_proba([text])[0]
            print(f"\n📊 Probabilidades:")
            for classe, prob in zip(predictor.classes, proba):
                bar = "█" * int(prob * 50)
                print(f"   {classe:15s} {prob:.2%} {bar}")
        
        print()
        
    except Exception as e:
        print(f"❌ Erro: {e}")


def predict_csv(model_name: str, csv_path: str, output_path: str = None, show_proba: bool = False):
    """Faz predições para um arquivo CSV."""
    model_path = Path("models") / f"{model_name}.joblib"
    csv_file = Path(csv_path)
    
    if not model_path.exists():
        print(f"❌ Modelo não encontrado: {model_path}")
        return
    
    if not csv_file.exists():
        print(f"❌ Arquivo CSV não encontrado: {csv_path}")
        return
    
    try:
        predictor = ModelPredictor(model_path)
        
        # Definir output
        if output_path is None:
            output_path = csv_file.stem + "_predictions.csv"
        
        print(f"\n🔄 Processando {csv_path}...")
        print(f"   Modelo: {model_name}")
        print(f"   Classes: {', '.join(predictor.classes)}")
        
        df = predictor.predict_from_csv(
            csv_path,
            output_csv=output_path,
            include_probabilities=show_proba
        )
        
        print(f"\n✅ {len(df)} predições realizadas")
        print(f"📁 Resultado salvo em: {output_path}")
        
        # Mostrar resumo
        print(f"\n📊 Distribuição das predições:")
        counts = df['prediction'].value_counts()
        for classe, count in counts.items():
            pct = count / len(df) * 100
            bar = "█" * int(pct / 2)
            print(f"   {classe:15s} {count:4d} ({pct:5.1f}%) {bar}")
        
        print()
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()


def compare_models(text: str):
    """Compara predições de todos os modelos."""
    print(f"\n📝 Texto: {text}\n")
    print(f"{'Modelo':<30} {'Predição':<15} {'Confiança'}")
    print("-" * 60)
    
    models = load_all_models("models")
    
    for model_name, predictor in sorted(models.items()):
        prediction = predictor.predict([text])[0]
        proba = predictor.predict_proba([text])[0]
        confidence = proba.max()
        
        bar = "█" * int(confidence * 20)
        print(f"{model_name:<30} {prediction:<15} {confidence:.2%} {bar}")
    
    print()


def main():
    parser = argparse.ArgumentParser(
        description="CLI para fazer predições com modelos treinados",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:

  # Listar modelos disponíveis
  uv run predict_cli.py --list-models

  # Predizer um texto
  uv run predict_cli.py \\
    --model arcaico_moderno__tfidf_lr \\
    --text "Este é um texto moderno"

  # Predizer com probabilidades
  uv run predict_cli.py \\
    --model arcaico_moderno__tfidf_lr \\
    --text "Texto de exemplo" \\
    --proba

  # Processar CSV
  uv run predict_cli.py \\
    --model complexo_simples__tfidf_lr \\
    --csv dados.csv \\
    --output resultados.csv

  # Comparar todos os modelos
  uv run predict_cli.py \\
    --compare "Texto para comparar"

        """
    )
    
    parser.add_argument(
        "--list-models",
        action="store_true",
        help="Lista todos os modelos disponíveis"
    )
    
    parser.add_argument(
        "--model",
        type=str,
        help="Nome do modelo (sem .joblib)"
    )
    
    parser.add_argument(
        "--text",
        type=str,
        help="Texto para classificar"
    )
    
    parser.add_argument(
        "--csv",
        type=str,
        help="Arquivo CSV com textos para classificar"
    )
    
    parser.add_argument(
        "--output",
        type=str,
        help="Arquivo de saída para resultados CSV"
    )
    
    parser.add_argument(
        "--proba",
        action="store_true",
        help="Mostrar probabilidades das predições"
    )
    
    parser.add_argument(
        "--compare",
        type=str,
        help="Comparar predição de todos os modelos para um texto"
    )
    
    args = parser.parse_args()
    
    # Executar ação apropriada
    if args.list_models:
        list_models()
    
    elif args.compare:
        compare_models(args.compare)
    
    elif args.text and args.model:
        predict_text(args.model, args.text, args.proba)
    
    elif args.csv and args.model:
        predict_csv(args.model, args.csv, args.output, args.proba)
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

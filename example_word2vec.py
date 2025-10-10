"""
Exemplo de uso dos modelos Word2Vec
"""
from src.ep1.config import get_default_config
import pandas as pd

# Carregar configuração
config = get_default_config()

# Datasets disponíveis (do JSON)
datasets = config._config['datasets']
print("Datasets disponíveis:")
for name, path in datasets.items():
    print(f"  - {name}: {path}")

# Carregar o primeiro dataset
dataset_name = 'arcaico_moderno'
dataset_path = f"data/{datasets[dataset_name]}"
print(f"\nCarregando dataset: {dataset_name}")
df = pd.read_csv(dataset_path, sep=';', encoding='ISO-8859-1')
print(f"  Shape: {df.shape}")
print(f"  Colunas: {df.columns.tolist()}")

# Pegar uma amostra balanceada para teste
sample_size = 50  # 50 de cada classe
# Usar o primeiro nome de coluna (que pode ter BOM)
text_col = df.columns[0]
label_col = df.columns[1]

# Pegar amostras de cada classe
classes = df[label_col].unique()
print(f"\nClasses disponíveis: {classes}")

samples = []
for cls in classes[:2]:  # Pegar apenas as 2 primeiras classes
    cls_data = df[df[label_col] == cls].head(sample_size)
    samples.append(cls_data)

df_sample = pd.concat(samples)
X_sample = df_sample[text_col].values
y_sample = df_sample[label_col].values

print(f"\nUsando amostra balanceada:")
print(f"  Total de exemplos: {len(X_sample)}")
print(f"  Distribuição: {pd.Series(y_sample).value_counts().to_dict()}")
print(f"  Coluna de texto: '{text_col}'")
print(f"  Coluna de label: '{label_col}'")

# Criar e treinar modelo Word2Vec + LR
print("\n" + "="*70)
print("Treinando Word2Vec + Logistic Regression")
print("="*70)
model = config.get_model('word2vec_lr')
print(f"Modelo: {model}")
print("\nTreinando...")
model.fit(X_sample, y_sample)
print("✓ Treinamento concluído!")

# Testar predição
print("\nTestando predições em 5 exemplos:")
X_test = X_sample[:5]
y_test = y_sample[:5]
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)

for i in range(5):
    print(f"\n  Exemplo {i+1}:")
    print(f"    Texto: {X_test[i][:80]}...")
    print(f"    Label real: {y_test[i]}")
    print(f"    Predição: {y_pred[i]}")
    print(f"    Probabilidades: {y_proba[i]}")

# Verificar componentes do pipeline
print("\n" + "="*70)
print("Componentes do pipeline:")
print("="*70)
print(f"  1. Vetorizador: {model.named_steps['word2vec']}")
print(f"     - vector_size: {model.named_steps['word2vec'].vector_size}")
print(f"     - window: {model.named_steps['word2vec'].window}")
print(f"     - sg (0=CBOW, 1=skip-gram): {model.named_steps['word2vec'].sg}")
print(f"  2. Classificador: {model.named_steps['clf']}")

# Testar Word2Vec + SVC
print("\n" + "="*70)
print("Treinando Word2Vec + SVC")
print("="*70)
model_svc = config.get_model('word2vec_svc')
print(f"Modelo: {model_svc}")
print("\nTreinando...")
model_svc.fit(X_sample, y_sample)
print("✓ Treinamento concluído!")

# Comparar predições
print("\nComparando predições (primeiros 5 exemplos):")
y_pred_svc = model_svc.predict(X_test)
for i in range(5):
    print(f"  Exemplo {i+1}: Real={y_test[i]}, LR={y_pred[i]}, SVC={y_pred_svc[i]}")

print("\n" + "="*70)
print("✓ Teste completo!")
print("="*70)

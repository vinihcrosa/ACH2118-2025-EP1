# Migração para Configuração JSON

## Resumo das Mudanças

Este documento descreve as mudanças realizadas para migrar o sistema de configuração de pipelines de código Python hardcoded para um sistema baseado em JSON.

## Arquivos Criados

### 1. `config/pipelines.json`
- **Propósito**: Arquivo central de configuração para todas as pipelines
- **Conteúdo**: 
  - Definição de datasets
  - Configurações de cross-validation
  - Definição de modelos (sklearn e customizados)
  - Grid de parâmetros para experimentos

### 2. `src/ep1/config.py`
- **Propósito**: Módulo para carregar e gerenciar configurações do JSON
- **Classes principais**:
  - `PipelineConfig`: Classe principal para gerenciar configurações
  - Funções utilitárias: `get_class_from_string()`, `get_function_from_string()`, `create_model_from_config()`
- **Funcionalidades**:
  - Importação dinâmica de classes sklearn
  - Criação de pipelines a partir de configuração
  - Suporte para modelos customizados via factory functions
  - Singleton global via `get_default_config()`

### 3. `config/README.md`
- **Propósito**: Documentação completa do sistema de configuração JSON
- **Conteúdo**:
  - Estrutura do arquivo JSON
  - Exemplos de uso
  - Como adicionar novos modelos
  - Vantagens do sistema

### 4. `examples_config.py`
- **Propósito**: Demonstrações práticas de uso do sistema
- **Exemplos incluídos**:
  - Uso básico da configuração
  - Treinamento de modelos
  - Acesso a experimentos
  - Inspeção de configurações

## Arquivos Modificados

### 1. `src/ep1/experiments.py`
**Antes**: Grid de experimentos hardcoded com imports de todas as factory functions

**Depois**:
```python
from src.ep1.config import get_default_config

config = get_default_config()
DATASETS = config.datasets
EXPERIMENTS = config.get_experiments()
```

**Impacto**: 
- Redução de ~80 linhas de código
- Eliminação de dependências hardcoded
- Configurações centralizadas no JSON

### 2. `src/ep1/train.py`
**Antes**: 
```python
from src.ep1.models import get_model
DATASETS = {...}  # hardcoded
```

**Depois**:
```python
from src.ep1.config import get_default_config
config = get_default_config()
DATASETS = config.datasets
model = config.get_model(args.model)
```

**Impacto**:
- Lista de modelos disponíveis agora vem do JSON
- Datasets centralizados

### 3. `src/ep1/models/models.py`
**Antes**: Função `get_model()` com registry hardcoded

**Depois**: 
```python
def get_model(name: str):
    """DEPRECATED: Use src.ep1.config.PipelineConfig.get_model()"""
    from src.ep1.config import get_default_config
    config = get_default_config()
    return config.get_model(name)
```

**Impacto**:
- Mantida para compatibilidade retroativa
- Delega para o sistema de configuração JSON

## Vantagens da Nova Abordagem

### 1. **Centralização**
- Todas as configurações em um único arquivo JSON
- Fácil visualização de todos os modelos e parâmetros

### 2. **Facilidade de Modificação**
- Adicionar novos modelos sem editar Python
- Modificar parâmetros sem recompilar
- Não requer conhecimento profundo de Python

### 3. **Reprodutibilidade**
- Configurações versionadas junto com código
- Fácil compartilhar configurações exatas
- Histórico de mudanças via git

### 4. **Flexibilidade**
- Suporte para pipelines sklearn padrão
- Suporte para modelos customizados via factory functions
- Importação dinâmica de qualquer classe sklearn

### 5. **Manutenibilidade**
- Separação clara entre configuração e lógica
- Código mais limpo e modular
- Redução de código boilerplate

## Compatibilidade

O sistema mantém **compatibilidade total** com código existente:

- ✅ A função `get_model()` antiga ainda funciona
- ✅ Scripts existentes continuam funcionando
- ✅ Modelos customizados (sbert, mlp) mantidos

## Como Usar

### Básico
```python
from src.ep1.config import get_default_config

config = get_default_config()
model = config.get_model("tfidf_lr")
```

### Experimentos
```python
config = get_default_config()
experiments = config.get_experiments()

for model_name, model_factory, param_grid in experiments:
    model = model_factory()
    # usar modelo...
```

### Adicionar Novo Modelo
Edite `config/pipelines.json`:

```json
{
  "models": {
    "novo_modelo": {
      "type": "sklearn_pipeline",
      "steps": [
        {
          "name": "vectorizer",
          "class": "sklearn.feature_extraction.text.CountVectorizer",
          "params": {"max_features": 5000}
        },
        {
          "name": "clf",
          "class": "sklearn.ensemble.RandomForestClassifier",
          "params": {"n_estimators": 100}
        }
      ]
    }
  },
  "experiments": [
    {
      "model": "novo_modelo",
      "param_grid": {
        "clf__n_estimators": [50, 100, 200]
      }
    }
  ]
}
```

## Testes

Execute os exemplos:
```bash
uv run examples_config.py
```

Execute os scripts existentes:
```bash
uv run src/ep1/train.py --dataset arcaico_moderno --model tfidf_lr --cv 5
uv run src/ep1/experiments.py
```

## Próximos Passos Sugeridos

1. **Validação de Schema**: Adicionar validação JSON Schema para o arquivo de configuração
2. **CLI para Configuração**: Criar comandos para listar/adicionar modelos via CLI
3. **Hot Reload**: Suporte para recarregar configuração sem reiniciar
4. **Configurações Múltiplas**: Suporte para múltiplos arquivos de configuração (dev, prod, etc)
5. **Export de Resultados**: Adicionar configuração para formatos de output no JSON

## Conclusão

A migração para JSON torna o sistema mais:
- 📝 **Documentado**: Configurações auto-documentadas
- 🔧 **Configurável**: Mudanças rápidas sem código
- 🚀 **Escalável**: Fácil adicionar novos modelos
- 🎯 **Focado**: Código Python focado em lógica, não configuração

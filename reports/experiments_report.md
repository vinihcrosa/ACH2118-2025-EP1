# Relatório de Resultados

Gerado automaticamente em 2025-09-25 03:45.

## Melhores resultados por conjunto

- **arcaico_moderno**: `tfidf_lr` com 83.56% ± 0.37% (tfidf__max_features=8000.0)
- **complexo_simples**: `tfidf_lr` com 82.51% ± 0.39% (tfidf__max_features=8000.0)
- **literal_dinamico**: `tfidf_lr` com 83.51% ± 0.19% (tfidf__max_features=8000.0)

## arcaico_moderno
| Rank | Modelo | Acurácia (média ± desvio) | Parâmetros | Scores |
| --- | --- | --- | --- | --- |
| 1 | `tfidf_lr` | 83.56% ± 0.37% | tfidf__max_features=8000.0 | 0.8330, 0.8425, 0.8364, 0.8337, 0.8327 |
| 2 | `tfidf_lr` | 82.77% ± 0.40% | tfidf__max_features=5000.0 | 0.8236, 0.8335, 0.8308, 0.8273, 0.8231 |
| 3 | `torch_mlp` | 82.10% ± 0.35% | mlp__epochs=5.0, mlp__hidden=128.0 | 0.8182, 0.8254, 0.8250, 0.8174, 0.8189 |
| 4 | `torch_mlp` | 81.88% ± 0.39% | mlp__epochs=5.0, mlp__hidden=256.0 | 0.8154, 0.8249, 0.8212, 0.8181, 0.8144 |
| 5 | `tfidf_lr` | 81.77% ± 0.51% | tfidf__max_features=3000.0 | 0.8127, 0.8253, 0.8198, 0.8194, 0.8114 |
| 6 | `torch_mlp` | 81.37% ± 0.24% | mlp__epochs=10.0, mlp__hidden=128.0 | 0.8120, 0.8177, 0.8152, 0.8113, 0.8121 |
| 7 | `torch_mlp` | 81.18% ± 0.34% | mlp__epochs=10.0, mlp__hidden=256.0 | 0.8113, 0.8148, 0.8155, 0.8059, 0.8113 |
| 8 | `sbert_lr` | 75.80% ± 0.66% | sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.7557, 0.7500, 0.7637, 0.7529, 0.7675 |
| 9 | `sbert_lr` | 71.78% ± 0.62% | sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.7171, 0.7088, 0.7184, 0.7163, 0.7282 |

## complexo_simples
| Rank | Modelo | Acurácia (média ± desvio) | Parâmetros | Scores |
| --- | --- | --- | --- | --- |
| 1 | `tfidf_lr` | 82.51% ± 0.39% | tfidf__max_features=8000.0 | 0.8185, 0.8260, 0.8265, 0.8306, 0.8241 |
| 2 | `tfidf_lr` | 81.94% ± 0.28% | tfidf__max_features=5000.0 | 0.8144, 0.8193, 0.8217, 0.8224, 0.8194 |
| 3 | `torch_mlp` | 81.13% ± 0.19% | mlp__epochs=5.0, mlp__hidden=128.0 | 0.8093, 0.8145, 0.8113, 0.8118, 0.8094 |
| 4 | `torch_mlp` | 80.87% ± 0.21% | mlp__epochs=5.0, mlp__hidden=256.0 | 0.8078, 0.8094, 0.8051, 0.8106, 0.8109 |
| 5 | `tfidf_lr` | 80.78% ± 0.47% | tfidf__max_features=3000.0 | 0.7987, 0.8100, 0.8115, 0.8109, 0.8080 |
| 6 | `torch_mlp` | 80.45% ± 0.34% | mlp__epochs=10.0, mlp__hidden=128.0 | 0.8063, 0.8043, 0.8001, 0.8098, 0.8021 |
| 7 | `torch_mlp` | 80.18% ± 0.36% | mlp__epochs=10.0, mlp__hidden=256.0 | 0.8000, 0.8007, 0.7991, 0.8089, 0.8001 |
| 8 | `sbert_lr` | 69.24% ± 0.57% | sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.6898, 0.6961, 0.6854, 0.7014, 0.6893 |
| 9 | `sbert_lr` | 68.43% ± 0.37% | sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.6790, 0.6875, 0.6863, 0.6882, 0.6807 |

## literal_dinamico
| Rank | Modelo | Acurácia (média ± desvio) | Parâmetros | Scores |
| --- | --- | --- | --- | --- |
| 1 | `tfidf_lr` | 83.51% ± 0.19% | tfidf__max_features=8000.0 | 0.8313, 0.8369, 0.8354, 0.8362, 0.8356 |
| 2 | `tfidf_lr` | 82.91% ± 0.37% | tfidf__max_features=5000.0 | 0.8223, 0.8298, 0.8301, 0.8296, 0.8335 |
| 3 | `torch_mlp` | 81.85% ± 0.22% | mlp__epochs=5.0, mlp__hidden=128.0 | 0.8177, 0.8206, 0.8201, 0.8147, 0.8194 |
| 4 | `tfidf_lr` | 81.77% ± 0.34% | tfidf__max_features=3000.0 | 0.8110, 0.8192, 0.8198, 0.8205, 0.8180 |
| 5 | `torch_mlp` | 81.64% ± 0.26% | mlp__epochs=5.0, mlp__hidden=256.0 | 0.8189, 0.8171, 0.8159, 0.8117, 0.8186 |
| 6 | `torch_mlp` | 80.99% ± 0.17% | mlp__epochs=10.0, mlp__hidden=128.0 | 0.8125, 0.8090, 0.8081, 0.8087, 0.8113 |
| 7 | `torch_mlp` | 80.99% ± 0.13% | mlp__epochs=10.0, mlp__hidden=256.0 | 0.8091, 0.8117, 0.8100, 0.8078, 0.8107 |
| 8 | `sbert_lr` | 75.44% ± 0.56% | sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.7571, 0.7457, 0.7500, 0.7591, 0.7603 |
| 9 | `sbert_lr` | 70.81% ± 0.27% | sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.7112, 0.7074, 0.7055, 0.7050, 0.7114 |


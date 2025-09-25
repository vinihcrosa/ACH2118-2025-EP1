# Relatório de Resultados

Gerado automaticamente em 2025-09-25 11:08.

## Melhores resultados por conjunto

- **arcaico_moderno**: `tfidf_lr` com 83.56% ± 0.37% (tfidf__max_features=8000.0)
- **complexo_simples**: `tfidf_lr` com 82.51% ± 0.39% (tfidf__max_features=8000.0)
- **literal_dinamico**: `tfidf_lr` com 83.51% ± 0.19% (tfidf__max_features=8000.0)

## arcaico_moderno
| Rank | Modelo | Acurácia (média ± desvio) | Parâmetros | Scores |
| --- | --- | --- | --- | --- |
| 1 | `tfidf_lr` | 83.56% ± 0.37% | tfidf__max_features=8000.0 | 0.8330, 0.8425, 0.8364, 0.8337, 0.8327 |
| 2 | `tfidf_sgd` | 82.80% ± 0.44% | clf__alpha=1e-05, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8235, 0.8335, 0.8330, 0.8235, 0.8265 |
| 3 | `tfidf_sgd` | 82.80% ± 0.43% | clf__alpha=1e-05, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8232, 0.8342, 0.8320, 0.8245, 0.8259 |
| 4 | `tfidf_lr` | 82.77% ± 0.40% | tfidf__max_features=5000.0 | 0.8236, 0.8335, 0.8308, 0.8273, 0.8231 |
| 5 | `tfidf_sgd` | 82.76% ± 0.40% | clf__alpha=1e-05, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8221, 0.8327, 0.8314, 0.8243, 0.8274 |
| 6 | `tfidf_lr` | 82.74% ± 0.40% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8235, 0.8339, 0.8301, 0.8254, 0.8240 |
| 7 | `tfidf_lr` | 82.72% ± 0.39% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8239, 0.8337, 0.8297, 0.8253, 0.8233 |
| 8 | `tfidf_lr` | 82.69% ± 0.39% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8231, 0.8334, 0.8293, 0.8250, 0.8238 |
| 9 | `tfidf_svc` | 82.59% ± 0.36% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8242, 0.8314, 0.8288, 0.8220, 0.8231 |
| 10 | `tfidf_sgd` | 82.56% ± 0.22% | clf__alpha=1e-05, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8246, 0.8292, 0.8234, 0.8240, 0.8270 |
| 11 | `tfidf_svc` | 82.53% ± 0.37% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8227, 0.8319, 0.8266, 0.8217, 0.8238 |
| 12 | `tfidf_svc` | 82.50% ± 0.29% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8230, 0.8301, 0.8262, 0.8223, 0.8235 |
| 13 | `tfidf_ridge` | 82.36% ± 0.24% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8207, 0.8274, 0.8243, 0.8215, 0.8243 |
| 14 | `tfidf_svc` | 82.36% ± 0.11% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8234, 0.8243, 0.8253, 0.8219, 0.8232 |
| 15 | `tfidf_ridge` | 82.36% ± 0.31% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8190, 0.8280, 0.8251, 0.8216, 0.8242 |
| 16 | `tfidf_ridge` | 82.33% ± 0.33% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8190, 0.8281, 0.8239, 0.8201, 0.8251 |
| 17 | `tfidf_lr` | 82.17% ± 0.15% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8208, 0.8242, 0.8224, 0.8198, 0.8214 |
| 18 | `tfidf_cnb` | 82.15% ± 0.19% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8246, 0.8230, 0.8194, 0.8203, 0.8204 |
| 19 | `tfidf_cnb` | 82.14% ± 0.22% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8246, 0.8226, 0.8178, 0.8209, 0.8213 |
| 20 | `tfidf_cnb` | 82.13% ± 0.17% | clf__alpha=1.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8243, 0.8221, 0.8196, 0.8203, 0.8204 |
| 21 | `tfidf_nb` | 82.13% ± 0.20% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8239, 0.8224, 0.8178, 0.8211, 0.8213 |
| 22 | `torch_mlp` | 82.10% ± 0.35% | mlp__epochs=5.0, mlp__hidden=128.0 | 0.8182, 0.8254, 0.8250, 0.8174, 0.8189 |
| 23 | `tfidf_ridge` | 82.07% ± 0.26% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8193, 0.8250, 0.8226, 0.8178, 0.8190 |
| 24 | `tfidf_ridge` | 82.05% ± 0.16% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8192, 0.8209, 0.8208, 0.8184, 0.8231 |
| 25 | `tfidf_ridge` | 82.04% ± 0.25% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8194, 0.8250, 0.8207, 0.8173, 0.8198 |
| 26 | `torch_mlp` | 82.02% ± 0.36% | mlp__epochs=5.0, mlp__hidden=128.0 | 0.8185, 0.8251, 0.8236, 0.8152, 0.8187 |
| 27 | `tfidf_ridge` | 82.01% ± 0.23% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8174, 0.8235, 0.8216, 0.8178, 0.8204 |
| 28 | `torch_mlp` | 81.88% ± 0.39% | mlp__epochs=5.0, mlp__hidden=256.0 | 0.8154, 0.8249, 0.8212, 0.8181, 0.8144 |
| 29 | `torch_mlp` | 81.86% ± 0.50% | mlp__epochs=5.0, mlp__hidden=256.0 | 0.8128, 0.8242, 0.8243, 0.8135, 0.8183 |
| 30 | `tfidf_sgd` | 81.79% ± 0.44% | clf__alpha=0.0001, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8118, 0.8245, 0.8207, 0.8178, 0.8148 |
| 31 | `tfidf_sgd` | 81.79% ± 0.46% | clf__alpha=0.0001, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8114, 0.8242, 0.8212, 0.8184, 0.8141 |
| 32 | `tfidf_sgd` | 81.78% ± 0.42% | clf__alpha=0.0001, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8121, 0.8239, 0.8209, 0.8170, 0.8149 |
| 33 | `tfidf_ridge` | 81.77% ± 0.10% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8179, 0.8174, 0.8188, 0.8160, 0.8185 |
| 34 | `tfidf_lr` | 81.77% ± 0.51% | tfidf__max_features=3000.0 | 0.8127, 0.8253, 0.8198, 0.8194, 0.8114 |
| 35 | `tfidf_sgd` | 81.73% ± 0.17% | clf__alpha=1e-05, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8162, 0.8188, 0.8198, 0.8163, 0.8155 |
| 36 | `tfidf_sgd` | 81.72% ± 0.22% | clf__alpha=1e-05, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8154, 0.8190, 0.8207, 0.8160, 0.8151 |
| 37 | `tfidf_sgd` | 81.72% ± 0.24% | clf__alpha=1e-05, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8143, 0.8193, 0.8207, 0.8163, 0.8152 |
| 38 | `tfidf_lr` | 81.63% ± 0.43% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8129, 0.8235, 0.8166, 0.8173, 0.8110 |
| 39 | `tfidf_lr` | 81.59% ± 0.49% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8109, 0.8239, 0.8177, 0.8165, 0.8105 |
| 40 | `tfidf_cnb` | 81.58% ± 0.15% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8160, 0.8178, 0.8146, 0.8169, 0.8139 |
| 41 | `tfidf_lr` | 81.57% ± 0.52% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8118, 0.8240, 0.8169, 0.8171, 0.8088 |
| 42 | `tfidf_cnb` | 81.57% ± 0.13% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8156, 0.8173, 0.8139, 0.8171, 0.8147 |
| 43 | `tfidf_cnb` | 81.57% ± 0.21% | clf__alpha=1.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8165, 0.8178, 0.8125, 0.8175, 0.8140 |
| 44 | `tfidf_svc` | 81.56% ± 0.26% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8116, 0.8165, 0.8196, 0.8147, 0.8158 |
| 45 | `tfidf_cnb` | 81.56% ± 0.21% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8173, 0.8173, 0.8135, 0.8173, 0.8126 |
| 46 | `tfidf_cnb` | 81.56% ± 0.19% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8169, 0.8175, 0.8131, 0.8169, 0.8134 |
| 47 | `tfidf_cnb` | 81.55% ± 0.15% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8147, 0.8181, 0.8146, 0.8162, 0.8141 |
| 48 | `tfidf_sgd` | 81.55% ± 0.11% | clf__alpha=1e-05, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8162, 0.8150, 0.8142, 0.8150, 0.8172 |
| 49 | `tfidf_nb` | 81.54% ± 0.18% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8165, 0.8174, 0.8131, 0.8169, 0.8134 |
| 50 | `tfidf_cnb` | 81.54% ± 0.16% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8162, 0.8175, 0.8140, 0.8163, 0.8132 |
| 51 | `tfidf_nb` | 81.54% ± 0.20% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8167, 0.8171, 0.8135, 0.8173, 0.8126 |
| 52 | `tfidf_cnb` | 81.54% ± 0.20% | clf__alpha=1.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8165, 0.8171, 0.8136, 0.8174, 0.8124 |
| 53 | `tfidf_nb` | 81.53% ± 0.15% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8158, 0.8174, 0.8140, 0.8163, 0.8132 |
| 54 | `tfidf_cnb` | 81.52% ± 0.20% | clf__alpha=1.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8160, 0.8178, 0.8135, 0.8163, 0.8124 |
| 55 | `tfidf_svc` | 81.52% ± 0.24% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8116, 0.8156, 0.8190, 0.8151, 0.8145 |
| 56 | `tfidf_svc` | 81.50% ± 0.22% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8118, 0.8160, 0.8184, 0.8137, 0.8148 |
| 57 | `tfidf_ridge` | 81.44% ± 0.22% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8118, 0.8165, 0.8173, 0.8147, 0.8120 |
| 58 | `tfidf_ridge` | 81.40% ± 0.19% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8129, 0.8159, 0.8163, 0.8139, 0.8111 |
| 59 | `tfidf_ridge` | 81.40% ± 0.20% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8125, 0.8162, 0.8163, 0.8135, 0.8113 |
| 60 | `torch_mlp` | 81.37% ± 0.24% | mlp__epochs=10.0, mlp__hidden=128.0 | 0.8120, 0.8177, 0.8152, 0.8113, 0.8121 |
| 61 | `torch_mlp` | 81.36% ± 0.25% | mlp__epochs=10.0, mlp__hidden=128.0 | 0.8125, 0.8175, 0.8150, 0.8104, 0.8125 |
| 62 | `tfidf_lr` | 81.31% ± 0.14% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8116, 0.8144, 0.8113, 0.8148, 0.8136 |
| 63 | `tfidf_ridge` | 81.29% ± 0.19% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8114, 0.8146, 0.8151, 0.8135, 0.8099 |
| 64 | `tfidf_ridge` | 81.27% ± 0.18% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8125, 0.8135, 0.8151, 0.8127, 0.8097 |
| 65 | `tfidf_ridge` | 81.24% ± 0.17% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8123, 0.8133, 0.8146, 0.8123, 0.8094 |
| 66 | `tfidf_svc` | 81.22% ± 0.20% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8095, 0.8128, 0.8128, 0.8108, 0.8153 |
| 67 | `torch_mlp` | 81.18% ± 0.34% | mlp__epochs=10.0, mlp__hidden=256.0 | 0.8113, 0.8148, 0.8155, 0.8059, 0.8113 |
| 68 | `torch_mlp` | 81.17% ± 0.37% | mlp__epochs=10.0, mlp__hidden=256.0 | 0.8086, 0.8171, 0.8143, 0.8071, 0.8116 |
| 69 | `tfidf_pa` | 81.16% ± 0.30% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8086, 0.8169, 0.8121, 0.8089, 0.8117 |
| 70 | `tfidf_cnb` | 81.14% ± 0.25% | clf__alpha=1.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8162, 0.8098, 0.8091, 0.8110, 0.8109 |
| 71 | `tfidf_sgd` | 81.13% ± 0.27% | clf__alpha=0.0001, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8072, 0.8123, 0.8097, 0.8120, 0.8153 |
| 72 | `tfidf_pa` | 81.13% ± 0.21% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8093, 0.8143, 0.8133, 0.8091, 0.8105 |
| 73 | `tfidf_cnb` | 81.11% ± 0.20% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8150, 0.8099, 0.8098, 0.8113, 0.8097 |
| 74 | `tfidf_cnb` | 81.11% ± 0.21% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8150, 0.8102, 0.8086, 0.8108, 0.8110 |
| 75 | `tfidf_nb` | 81.10% ± 0.20% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8146, 0.8101, 0.8086, 0.8108, 0.8110 |
| 76 | `tfidf_pa` | 81.06% ± 0.26% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8068, 0.8135, 0.8131, 0.8086, 0.8109 |
| 77 | `tfidf_ridge` | 81.01% ± 0.33% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8047, 0.8117, 0.8094, 0.8098, 0.8147 |
| 78 | `tfidf_pa` | 80.88% ± 0.49% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8078, 0.8109, 0.8155, 0.8006, 0.8091 |
| 79 | `tfidf_sgd` | 80.86% ± 0.49% | clf__alpha=0.0001, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8034, 0.8152, 0.8127, 0.8087, 0.8030 |
| 80 | `tfidf_sgd` | 80.85% ± 0.51% | clf__alpha=0.0001, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8021, 0.8155, 0.8125, 0.8087, 0.8036 |
| 81 | `tfidf_sgd` | 80.85% ± 0.49% | clf__alpha=0.0001, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8030, 0.8150, 0.8131, 0.8078, 0.8034 |
| 82 | `tfidf_ridge` | 80.77% ± 0.27% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8030, 0.8079, 0.8078, 0.8082, 0.8116 |
| 83 | `tfidf_pa` | 80.73% ± 0.33% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8036, 0.8125, 0.8093, 0.8043, 0.8069 |
| 84 | `tfidf_pa` | 80.72% ± 0.13% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8057, 0.8082, 0.8090, 0.8057, 0.8073 |
| 85 | `tfidf_pa` | 80.70% ± 0.20% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8072, 0.8090, 0.8090, 0.8059, 0.8037 |
| 86 | `tfidf_sgd` | 80.66% ± 0.22% | clf__alpha=0.0001, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8062, 0.8063, 0.8032, 0.8099, 0.8076 |
| 87 | `tfidf_pa` | 80.66% ± 0.16% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8070, 0.8067, 0.8079, 0.8079, 0.8037 |
| 88 | `tfidf_pa` | 80.66% ± 0.23% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8068, 0.8093, 0.8085, 0.8059, 0.8026 |
| 89 | `tfidf_pa` | 80.63% ± 0.27% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8026, 0.8097, 0.8082, 0.8036, 0.8072 |
| 90 | `tfidf_pa` | 80.60% ± 0.28% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8028, 0.8038, 0.8109, 0.8060, 0.8065 |
| 91 | `tfidf_pa` | 80.55% ± 0.33% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8033, 0.8113, 0.8071, 0.8028, 0.8029 |
| 92 | `tfidf_pa` | 80.51% ± 0.28% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8007, 0.8037, 0.8093, 0.8063, 0.8055 |
| 93 | `tfidf_pa` | 80.51% ± 0.39% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8052, 0.8037, 0.8102, 0.7987, 0.8075 |
| 94 | `tfidf_pa` | 80.28% ± 0.31% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7973, 0.8040, 0.8059, 0.8013, 0.8053 |
| 95 | `tfidf_cnb` | 80.24% ± 0.15% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8044, 0.8032, 0.8026, 0.8022, 0.7998 |
| 96 | `tfidf_cnb` | 80.24% ± 0.17% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8052, 0.8026, 0.8025, 0.8021, 0.7998 |
| 97 | `tfidf_pa` | 80.23% ± 0.36% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.7982, 0.8078, 0.8037, 0.7987, 0.8033 |
| 98 | `tfidf_cnb` | 80.23% ± 0.23% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8052, 0.8030, 0.8033, 0.8015, 0.7984 |
| 99 | `tfidf_pa` | 80.22% ± 0.29% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.7992, 0.8056, 0.8036, 0.7983, 0.8045 |
| 100 | `tfidf_pa` | 80.21% ± 0.26% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8007, 0.8062, 0.8030, 0.7983, 0.8022 |
| 101 | `tfidf_cnb` | 80.20% ± 0.26% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8055, 0.8038, 0.8018, 0.8011, 0.7979 |
| 102 | `tfidf_cnb` | 80.20% ± 0.23% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8049, 0.8038, 0.8014, 0.8014, 0.7983 |
| 103 | `tfidf_cnb` | 80.20% ± 0.25% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8051, 0.8038, 0.8018, 0.8014, 0.7977 |
| 104 | `tfidf_nb` | 80.19% ± 0.25% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8051, 0.8037, 0.8018, 0.8011, 0.7979 |
| 105 | `tfidf_nb` | 80.19% ± 0.24% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8047, 0.8037, 0.8018, 0.8014, 0.7977 |
| 106 | `tfidf_nb` | 80.18% ± 0.21% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8044, 0.8036, 0.8014, 0.8014, 0.7983 |
| 107 | `tfidf_cnb` | 80.18% ± 0.27% | clf__alpha=1.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8057, 0.8037, 0.8010, 0.8005, 0.7980 |
| 108 | `tfidf_cnb` | 80.16% ± 0.28% | clf__alpha=1.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8059, 0.8030, 0.8014, 0.8003, 0.7976 |
| 109 | `tfidf_cnb` | 80.16% ± 0.28% | clf__alpha=1.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8060, 0.8034, 0.8003, 0.8003, 0.7979 |
| 110 | `tfidf_pa` | 80.15% ± 0.24% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8043, 0.8011, 0.8024, 0.7971, 0.8026 |
| 111 | `tfidf_pa` | 80.05% ± 0.17% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8015, 0.8014, 0.7986, 0.7984, 0.8025 |
| 112 | `tfidf_pa` | 80.02% ± 0.31% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7956, 0.8028, 0.8025, 0.7975, 0.8029 |
| 113 | `tfidf_pa` | 80.00% ± 0.36% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8025, 0.8018, 0.7980, 0.7940, 0.8040 |
| 114 | `tfidf_pa` | 79.91% ± 0.35% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7940, 0.8030, 0.7976, 0.7977, 0.8031 |
| 115 | `tfidf_pa` | 79.67% ± 0.21% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7971, 0.8005, 0.7963, 0.7940, 0.7958 |
| 116 | `tfidf_pa` | 79.64% ± 0.29% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7961, 0.8021, 0.7949, 0.7941, 0.7947 |
| 117 | `tfidf_pa` | 79.60% ± 0.27% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7964, 0.8010, 0.7952, 0.7934, 0.7942 |
| 118 | `tfidf_pa` | 79.56% ± 0.26% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7926, 0.7945, 0.7971, 0.7938, 0.7999 |
| 119 | `tfidf_pa` | 79.09% ± 0.63% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7903, 0.8015, 0.7915, 0.7818, 0.7896 |
| 120 | `tfidf_pa` | 78.98% ± 0.30% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7912, 0.7950, 0.7866, 0.7888, 0.7874 |
| 121 | `tfidf_pa` | 78.90% ± 0.27% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7904, 0.7935, 0.7873, 0.7872, 0.7863 |
| 122 | `tfidf_pa` | 78.87% ± 0.26% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7902, 0.7929, 0.7876, 0.7876, 0.7852 |
| 123 | `tfidf_pa` | 78.28% ± 0.77% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7858, 0.7949, 0.7827, 0.7719, 0.7786 |
| 124 | `sbert_svc` | 76.75% ± 0.63% | clf__C=2.0, sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.7637, 0.7580, 0.7700, 0.7691, 0.7768 |
| 125 | `sbert_svc` | 76.75% ± 0.66% | clf__C=1.0, sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.7637, 0.7574, 0.7705, 0.7687, 0.7771 |
| 126 | `sbert_svc` | 76.69% ± 0.71% | clf__C=0.5, sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.7632, 0.7568, 0.7705, 0.7660, 0.7779 |
| 127 | `sbert_lr` | 75.80% ± 0.66% | sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.7557, 0.7500, 0.7637, 0.7529, 0.7675 |
| 128 | `sbert_lr` | 75.80% ± 0.66% | sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.7557, 0.7500, 0.7637, 0.7529, 0.7675 |
| 129 | `sbert_svc` | 73.44% ± 0.75% | clf__C=2.0, sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.7305, 0.7240, 0.7362, 0.7346, 0.7469 |
| 130 | `sbert_svc` | 73.25% ± 0.74% | clf__C=1.0, sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.7281, 0.7236, 0.7358, 0.7298, 0.7450 |
| 131 | `sbert_svc` | 73.04% ± 0.68% | clf__C=0.5, sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.7297, 0.7203, 0.7335, 0.7277, 0.7409 |
| 132 | `sbert_lr` | 71.78% ± 0.62% | sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.7171, 0.7088, 0.7184, 0.7163, 0.7282 |
| 133 | `sbert_lr` | 71.78% ± 0.62% | sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.7171, 0.7088, 0.7184, 0.7163, 0.7282 |

## complexo_simples
| Rank | Modelo | Acurácia (média ± desvio) | Parâmetros | Scores |
| --- | --- | --- | --- | --- |
| 1 | `tfidf_lr` | 82.51% ± 0.39% | tfidf__max_features=8000.0 | 0.8185, 0.8260, 0.8265, 0.8306, 0.8241 |
| 2 | `tfidf_sgd` | 82.31% ± 0.12% | clf__alpha=1e-05, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8221, 0.8251, 0.8230, 0.8235, 0.8218 |
| 3 | `tfidf_sgd` | 82.30% ± 0.09% | clf__alpha=1e-05, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8218, 0.8244, 0.8224, 0.8232, 0.8233 |
| 4 | `tfidf_sgd` | 82.29% ± 0.17% | clf__alpha=1e-05, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8212, 0.8245, 0.8206, 0.8245, 0.8236 |
| 5 | `tfidf_svc` | 82.08% ± 0.21% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8172, 0.8215, 0.8203, 0.8236, 0.8212 |
| 6 | `tfidf_ridge` | 82.07% ± 0.33% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8166, 0.8199, 0.8224, 0.8262, 0.8184 |
| 7 | `tfidf_svc` | 82.06% ± 0.25% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8166, 0.8221, 0.8188, 0.8236, 0.8220 |
| 8 | `tfidf_ridge` | 82.06% ± 0.38% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8172, 0.8190, 0.8220, 0.8273, 0.8176 |
| 9 | `tfidf_svc` | 82.05% ± 0.22% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8169, 0.8215, 0.8193, 0.8233, 0.8217 |
| 10 | `tfidf_ridge` | 82.04% ± 0.39% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8159, 0.8200, 0.8224, 0.8266, 0.8169 |
| 11 | `tfidf_lr` | 81.94% ± 0.28% | tfidf__max_features=5000.0 | 0.8144, 0.8193, 0.8217, 0.8224, 0.8194 |
| 12 | `tfidf_lr` | 81.93% ± 0.25% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8147, 0.8209, 0.8206, 0.8215, 0.8188 |
| 13 | `tfidf_lr` | 81.92% ± 0.26% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8144, 0.8218, 0.8205, 0.8203, 0.8190 |
| 14 | `tfidf_lr` | 81.91% ± 0.25% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8147, 0.8220, 0.8206, 0.8193, 0.8188 |
| 15 | `tfidf_ridge` | 81.75% ± 0.39% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8118, 0.8190, 0.8191, 0.8232, 0.8146 |
| 16 | `tfidf_ridge` | 81.74% ± 0.34% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8138, 0.8181, 0.8194, 0.8223, 0.8134 |
| 17 | `tfidf_ridge` | 81.69% ± 0.37% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8130, 0.8173, 0.8187, 0.8227, 0.8128 |
| 18 | `torch_mlp` | 81.15% ± 0.31% | mlp__epochs=5.0, mlp__hidden=128.0 | 0.8060, 0.8116, 0.8155, 0.8121, 0.8122 |
| 19 | `tfidf_sgd` | 81.13% ± 0.37% | clf__alpha=1e-05, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8049, 0.8145, 0.8094, 0.8130, 0.8145 |
| 20 | `torch_mlp` | 81.13% ± 0.19% | mlp__epochs=5.0, mlp__hidden=128.0 | 0.8093, 0.8145, 0.8113, 0.8118, 0.8094 |
| 21 | `tfidf_sgd` | 81.12% ± 0.38% | clf__alpha=1e-05, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8043, 0.8143, 0.8103, 0.8125, 0.8146 |
| 22 | `tfidf_sgd` | 81.07% ± 0.38% | clf__alpha=1e-05, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8036, 0.8128, 0.8104, 0.8127, 0.8142 |
| 23 | `tfidf_svc` | 81.03% ± 0.39% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8028, 0.8134, 0.8100, 0.8124, 0.8128 |
| 24 | `torch_mlp` | 81.03% ± 0.12% | mlp__epochs=5.0, mlp__hidden=256.0 | 0.8088, 0.8092, 0.8101, 0.8118, 0.8115 |
| 25 | `tfidf_svc` | 81.02% ± 0.36% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8046, 0.8136, 0.8076, 0.8115, 0.8137 |
| 26 | `tfidf_svc` | 80.98% ± 0.35% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8036, 0.8125, 0.8082, 0.8122, 0.8125 |
| 27 | `torch_mlp` | 80.87% ± 0.21% | mlp__epochs=5.0, mlp__hidden=256.0 | 0.8078, 0.8094, 0.8051, 0.8106, 0.8109 |
| 28 | `tfidf_sgd` | 80.85% ± 0.32% | clf__alpha=0.0001, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8034, 0.8080, 0.8075, 0.8128, 0.8106 |
| 29 | `tfidf_sgd` | 80.84% ± 0.30% | clf__alpha=0.0001, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8036, 0.8082, 0.8073, 0.8124, 0.8106 |
| 30 | `tfidf_sgd` | 80.83% ± 0.32% | clf__alpha=0.0001, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8028, 0.8077, 0.8079, 0.8125, 0.8103 |
| 31 | `tfidf_ridge` | 80.79% ± 0.39% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8003, 0.8113, 0.8085, 0.8092, 0.8100 |
| 32 | `tfidf_lr` | 80.78% ± 0.47% | tfidf__max_features=3000.0 | 0.7987, 0.8100, 0.8115, 0.8109, 0.8080 |
| 33 | `tfidf_ridge` | 80.78% ± 0.46% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7993, 0.8130, 0.8085, 0.8083, 0.8100 |
| 34 | `tfidf_lr` | 80.77% ± 0.44% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7990, 0.8110, 0.8097, 0.8100, 0.8088 |
| 35 | `tfidf_lr` | 80.77% ± 0.43% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7993, 0.8106, 0.8101, 0.8101, 0.8082 |
| 36 | `tfidf_ridge` | 80.75% ± 0.45% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7994, 0.8127, 0.8069, 0.8083, 0.8104 |
| 37 | `tfidf_lr` | 80.72% ± 0.47% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7981, 0.8107, 0.8095, 0.8104, 0.8073 |
| 38 | `tfidf_sgd` | 80.69% ± 0.49% | clf__alpha=1e-05, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8006, 0.8046, 0.8097, 0.8148, 0.8048 |
| 39 | `tfidf_ridge` | 80.58% ± 0.44% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7984, 0.8121, 0.8060, 0.8076, 0.8052 |
| 40 | `torch_mlp` | 80.57% ± 0.26% | mlp__epochs=10.0, mlp__hidden=128.0 | 0.8018, 0.8088, 0.8048, 0.8049, 0.8083 |
| 41 | `tfidf_ridge` | 80.56% ± 0.44% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7981, 0.8118, 0.8064, 0.8060, 0.8060 |
| 42 | `tfidf_ridge` | 80.55% ± 0.51% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7966, 0.8121, 0.8048, 0.8070, 0.8069 |
| 43 | `tfidf_svc` | 80.48% ± 0.36% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8018, 0.8019, 0.8077, 0.8104, 0.8019 |
| 44 | `tfidf_pa` | 80.47% ± 0.36% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8018, 0.8040, 0.8003, 0.8080, 0.8095 |
| 45 | `torch_mlp` | 80.45% ± 0.34% | mlp__epochs=10.0, mlp__hidden=128.0 | 0.8063, 0.8043, 0.8001, 0.8098, 0.8021 |
| 46 | `tfidf_pa` | 80.36% ± 0.37% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8024, 0.8031, 0.7976, 0.8067, 0.8082 |
| 47 | `torch_mlp` | 80.34% ± 0.27% | mlp__epochs=10.0, mlp__hidden=256.0 | 0.7984, 0.8066, 0.8037, 0.8034, 0.8048 |
| 48 | `tfidf_pa` | 80.30% ± 0.40% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8030, 0.8051, 0.7952, 0.8052, 0.8064 |
| 49 | `tfidf_ridge` | 80.28% ± 0.53% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.7993, 0.8012, 0.8088, 0.8091, 0.7956 |
| 50 | `tfidf_lr` | 80.26% ± 0.46% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.7946, 0.8049, 0.8019, 0.8088, 0.8030 |
| 51 | `torch_mlp` | 80.18% ± 0.36% | mlp__epochs=10.0, mlp__hidden=256.0 | 0.8000, 0.8007, 0.7991, 0.8089, 0.8001 |
| 52 | `tfidf_pa` | 80.11% ± 0.51% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.7924, 0.8043, 0.7982, 0.8042, 0.8063 |
| 53 | `tfidf_pa` | 80.11% ± 0.41% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.7966, 0.8037, 0.7956, 0.8045, 0.8049 |
| 54 | `tfidf_pa` | 80.08% ± 0.39% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.7963, 0.8046, 0.7961, 0.8022, 0.8049 |
| 55 | `tfidf_sgd` | 80.03% ± 0.43% | clf__alpha=0.0001, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7918, 0.8036, 0.8015, 0.8021, 0.8025 |
| 56 | `tfidf_ridge` | 80.02% ± 0.45% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.7990, 0.7979, 0.8049, 0.8057, 0.7937 |
| 57 | `tfidf_sgd` | 80.00% ± 0.46% | clf__alpha=0.0001, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7910, 0.8039, 0.8010, 0.8019, 0.8022 |
| 58 | `tfidf_sgd` | 79.98% ± 0.45% | clf__alpha=0.0001, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7909, 0.8030, 0.8009, 0.8019, 0.8022 |
| 59 | `tfidf_pa` | 79.90% ± 0.37% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.7960, 0.8015, 0.7935, 0.8004, 0.8036 |
| 60 | `tfidf_pa` | 79.86% ± 0.34% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.7952, 0.8016, 0.7941, 0.7994, 0.8028 |
| 61 | `tfidf_pa` | 79.85% ± 0.26% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.7978, 0.7991, 0.7943, 0.7991, 0.8022 |
| 62 | `tfidf_pa` | 79.83% ± 0.33% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.7940, 0.8010, 0.7946, 0.8006, 0.8015 |
| 63 | `tfidf_cnb` | 79.81% ± 0.26% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.7955, 0.7988, 0.8015, 0.8001, 0.7947 |
| 64 | `tfidf_cnb` | 79.80% ± 0.28% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.7951, 0.7980, 0.8021, 0.8000, 0.7950 |
| 65 | `tfidf_pa` | 79.78% ± 0.42% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7949, 0.7995, 0.7916, 0.8037, 0.7992 |
| 66 | `tfidf_cnb` | 79.78% ± 0.26% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.7954, 0.7977, 0.8009, 0.8006, 0.7944 |
| 67 | `tfidf_cnb` | 79.71% ± 0.27% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.7943, 0.7983, 0.8001, 0.7992, 0.7935 |
| 68 | `tfidf_nb` | 79.70% ± 0.27% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.7943, 0.7982, 0.8001, 0.7992, 0.7934 |
| 69 | `tfidf_pa` | 79.70% ± 0.47% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7912, 0.8019, 0.7914, 0.8009, 0.7997 |
| 70 | `tfidf_pa` | 79.70% ± 0.51% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.7891, 0.8009, 0.7926, 0.8004, 0.8018 |
| 71 | `tfidf_cnb` | 79.69% ± 0.30% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.7931, 0.7974, 0.8010, 0.7989, 0.7938 |
| 72 | `tfidf_cnb` | 79.69% ± 0.26% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.7936, 0.7976, 0.7994, 0.7998, 0.7940 |
| 73 | `tfidf_nb` | 79.69% ± 0.26% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.7936, 0.7976, 0.7994, 0.7998, 0.7940 |
| 74 | `tfidf_nb` | 79.68% ± 0.30% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.7931, 0.7973, 0.8010, 0.7989, 0.7938 |
| 75 | `tfidf_pa` | 79.67% ± 0.45% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7915, 0.7988, 0.7920, 0.8036, 0.7979 |
| 76 | `tfidf_cnb` | 79.67% ± 0.27% | clf__alpha=1.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.7936, 0.7988, 0.7995, 0.7986, 0.7932 |
| 77 | `tfidf_cnb` | 79.67% ± 0.31% | clf__alpha=1.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.7927, 0.7983, 0.8007, 0.7985, 0.7934 |
| 78 | `tfidf_cnb` | 79.65% ± 0.30% | clf__alpha=1.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.7930, 0.7985, 0.7994, 0.7989, 0.7928 |
| 79 | `tfidf_sgd` | 79.65% ± 0.30% | clf__alpha=1e-05, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7942, 0.7964, 0.7952, 0.8022, 0.7946 |
| 80 | `tfidf_pa` | 79.56% ± 0.62% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.7874, 0.8004, 0.7892, 0.7982, 0.8030 |
| 81 | `tfidf_svc` | 79.52% ± 0.30% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7915, 0.7949, 0.7946, 0.8007, 0.7943 |
| 82 | `tfidf_pa` | 79.38% ± 0.36% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7868, 0.7967, 0.7950, 0.7937, 0.7967 |
| 83 | `tfidf_lr` | 79.35% ± 0.26% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7894, 0.7947, 0.7931, 0.7973, 0.7928 |
| 84 | `tfidf_pa` | 79.28% ± 0.30% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7880, 0.7917, 0.7937, 0.7931, 0.7973 |
| 85 | `tfidf_sgd` | 79.19% ± 0.46% | clf__alpha=0.0001, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.7835, 0.7911, 0.7931, 0.7967, 0.7952 |
| 86 | `tfidf_ridge` | 79.17% ± 0.48% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7876, 0.7923, 0.7901, 0.8006, 0.7877 |
| 87 | `tfidf_cnb` | 79.07% ± 0.46% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.7882, 0.7858, 0.7989, 0.7925, 0.7883 |
| 88 | `tfidf_cnb` | 79.06% ± 0.41% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.7873, 0.7876, 0.7982, 0.7919, 0.7882 |
| 89 | `tfidf_nb` | 79.06% ± 0.41% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.7873, 0.7876, 0.7982, 0.7919, 0.7882 |
| 90 | `tfidf_pa` | 79.04% ± 0.53% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7855, 0.7956, 0.7835, 0.7905, 0.7970 |
| 91 | `tfidf_pa` | 78.98% ± 0.33% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7841, 0.7911, 0.7943, 0.7890, 0.7904 |
| 92 | `tfidf_cnb` | 78.97% ± 0.42% | clf__alpha=1.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.7865, 0.7862, 0.7974, 0.7908, 0.7876 |
| 93 | `tfidf_ridge` | 78.96% ± 0.46% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7856, 0.7911, 0.7896, 0.7973, 0.7844 |
| 94 | `tfidf_pa` | 78.92% ± 0.21% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7855, 0.7901, 0.7913, 0.7883, 0.7910 |
| 95 | `tfidf_pa` | 78.88% ± 0.23% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7858, 0.7904, 0.7919, 0.7865, 0.7893 |
| 96 | `tfidf_pa` | 78.68% ± 0.36% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.7913, 0.7811, 0.7871, 0.7898, 0.7849 |
| 97 | `tfidf_sgd` | 78.65% ± 0.38% | clf__alpha=0.0001, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7797, 0.7871, 0.7867, 0.7913, 0.7880 |
| 98 | `tfidf_pa` | 78.61% ± 0.25% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7868, 0.7864, 0.7817, 0.7895, 0.7862 |
| 99 | `tfidf_nb` | 78.46% ± 0.51% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7829, 0.7910, 0.7893, 0.7829, 0.7766 |
| 100 | `tfidf_cnb` | 78.45% ± 0.49% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7829, 0.7905, 0.7887, 0.7837, 0.7766 |
| 101 | `tfidf_nb` | 78.45% ± 0.49% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7829, 0.7905, 0.7887, 0.7837, 0.7766 |
| 102 | `tfidf_cnb` | 78.45% ± 0.51% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7829, 0.7907, 0.7893, 0.7829, 0.7766 |
| 103 | `tfidf_cnb` | 78.45% ± 0.44% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7831, 0.7902, 0.7879, 0.7838, 0.7775 |
| 104 | `tfidf_nb` | 78.45% ± 0.44% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7831, 0.7902, 0.7879, 0.7838, 0.7775 |
| 105 | `tfidf_cnb` | 78.43% ± 0.41% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7834, 0.7892, 0.7879, 0.7837, 0.7775 |
| 106 | `tfidf_cnb` | 78.42% ± 0.43% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7832, 0.7899, 0.7880, 0.7823, 0.7777 |
| 107 | `tfidf_cnb` | 78.41% ± 0.49% | clf__alpha=1.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7828, 0.7901, 0.7883, 0.7835, 0.7760 |
| 108 | `tfidf_cnb` | 78.41% ± 0.42% | clf__alpha=1.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7831, 0.7895, 0.7874, 0.7834, 0.7774 |
| 109 | `tfidf_cnb` | 78.41% ± 0.41% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7825, 0.7895, 0.7876, 0.7832, 0.7777 |
| 110 | `tfidf_cnb` | 78.41% ± 0.47% | clf__alpha=1.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7828, 0.7896, 0.7886, 0.7828, 0.7766 |
| 111 | `tfidf_pa` | 78.28% ± 0.36% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.7867, 0.7763, 0.7841, 0.7853, 0.7816 |
| 112 | `tfidf_pa` | 78.24% ± 0.18% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.7822, 0.7825, 0.7847, 0.7835, 0.7793 |
| 113 | `tfidf_pa` | 78.23% ± 0.28% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7783, 0.7826, 0.7823, 0.7814, 0.7870 |
| 114 | `tfidf_pa` | 78.12% ± 0.37% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7780, 0.7835, 0.7760, 0.7823, 0.7864 |
| 115 | `tfidf_pa` | 78.04% ± 0.42% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7758, 0.7808, 0.7762, 0.7825, 0.7870 |
| 116 | `tfidf_pa` | 77.77% ± 0.21% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.7774, 0.7751, 0.7781, 0.7763, 0.7814 |
| 117 | `tfidf_cnb` | 77.60% ± 0.45% | clf__alpha=1.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7741, 0.7766, 0.7834, 0.7765, 0.7693 |
| 118 | `tfidf_nb` | 77.58% ± 0.42% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7744, 0.7759, 0.7831, 0.7753, 0.7702 |
| 119 | `tfidf_cnb` | 77.57% ± 0.41% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7744, 0.7759, 0.7829, 0.7753, 0.7702 |
| 120 | `tfidf_cnb` | 77.53% ± 0.45% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7737, 0.7757, 0.7834, 0.7741, 0.7697 |
| 121 | `tfidf_pa` | 77.48% ± 0.33% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7732, 0.7769, 0.7690, 0.7781, 0.7766 |
| 122 | `tfidf_pa` | 77.27% ± 0.38% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7786, 0.7724, 0.7681, 0.7696, 0.7750 |
| 123 | `tfidf_pa` | 76.25% ± 0.60% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7684, 0.7641, 0.7588, 0.7528, 0.7683 |
| 124 | `sbert_svc` | 70.18% ± 0.38% | clf__C=2.0, sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.6992, 0.7054, 0.6979, 0.7074, 0.6991 |
| 125 | `sbert_svc` | 69.99% ± 0.43% | clf__C=1.0, sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.6960, 0.7024, 0.6982, 0.7071, 0.6957 |
| 126 | `sbert_svc` | 69.92% ± 0.43% | clf__C=2.0, sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.6924, 0.6994, 0.7003, 0.7059, 0.6979 |
| 127 | `sbert_svc` | 69.86% ± 0.40% | clf__C=1.0, sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.6923, 0.6997, 0.7018, 0.7033, 0.6960 |
| 128 | `sbert_svc` | 69.77% ± 0.37% | clf__C=0.5, sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.6956, 0.6985, 0.6966, 0.7044, 0.6933 |
| 129 | `sbert_svc` | 69.51% ± 0.47% | clf__C=0.5, sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.6877, 0.6981, 0.6978, 0.7002, 0.6917 |
| 130 | `sbert_lr` | 69.24% ± 0.57% | sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.6898, 0.6961, 0.6854, 0.7014, 0.6893 |
| 131 | `sbert_lr` | 69.24% ± 0.57% | sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.6898, 0.6961, 0.6854, 0.7014, 0.6893 |
| 132 | `sbert_lr` | 68.43% ± 0.37% | sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.6790, 0.6875, 0.6863, 0.6882, 0.6807 |
| 133 | `sbert_lr` | 68.43% ± 0.37% | sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.6790, 0.6875, 0.6863, 0.6882, 0.6807 |

## literal_dinamico
| Rank | Modelo | Acurácia (média ± desvio) | Parâmetros | Scores |
| --- | --- | --- | --- | --- |
| 1 | `tfidf_lr` | 83.51% ± 0.19% | tfidf__max_features=8000.0 | 0.8313, 0.8369, 0.8354, 0.8362, 0.8356 |
| 2 | `tfidf_lr` | 82.91% ± 0.37% | tfidf__max_features=5000.0 | 0.8223, 0.8298, 0.8301, 0.8296, 0.8335 |
| 3 | `tfidf_lr` | 82.88% ± 0.33% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8224, 0.8308, 0.8293, 0.8308, 0.8308 |
| 4 | `tfidf_lr` | 82.87% ± 0.30% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8229, 0.8293, 0.8293, 0.8309, 0.8310 |
| 5 | `tfidf_sgd` | 82.86% ± 0.36% | clf__alpha=1e-05, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8262, 0.8262, 0.8274, 0.8357, 0.8277 |
| 6 | `tfidf_lr` | 82.86% ± 0.27% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8232, 0.8297, 0.8290, 0.8307, 0.8304 |
| 7 | `tfidf_sgd` | 82.83% ± 0.40% | clf__alpha=1e-05, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8251, 0.8266, 0.8254, 0.8358, 0.8289 |
| 8 | `tfidf_sgd` | 82.83% ± 0.34% | clf__alpha=1e-05, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8252, 0.8266, 0.8275, 0.8348, 0.8274 |
| 9 | `tfidf_svc` | 82.54% ± 0.25% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8210, 0.8266, 0.8262, 0.8284, 0.8248 |
| 10 | `tfidf_svc` | 82.50% ± 0.29% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8196, 0.8265, 0.8255, 0.8279, 0.8256 |
| 11 | `tfidf_svc` | 82.48% ± 0.28% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8197, 0.8254, 0.8262, 0.8279, 0.8248 |
| 12 | `tfidf_sgd` | 82.31% ± 0.34% | clf__alpha=1e-05, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8194, 0.8197, 0.8277, 0.8266, 0.8222 |
| 13 | `tfidf_ridge` | 82.24% ± 0.29% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8190, 0.8216, 0.8201, 0.8270, 0.8241 |
| 14 | `tfidf_ridge` | 82.22% ± 0.37% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8173, 0.8231, 0.8198, 0.8282, 0.8228 |
| 15 | `tfidf_ridge` | 82.12% ± 0.37% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8156, 0.8210, 0.8196, 0.8267, 0.8228 |
| 16 | `tfidf_svc` | 82.06% ± 0.47% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8140, 0.8164, 0.8247, 0.8265, 0.8214 |
| 17 | `tfidf_cnb` | 81.98% ± 0.45% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8127, 0.8216, 0.8250, 0.8229, 0.8168 |
| 18 | `tfidf_nb` | 81.95% ± 0.42% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8123, 0.8212, 0.8240, 0.8225, 0.8176 |
| 19 | `tfidf_cnb` | 81.95% ± 0.42% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8123, 0.8212, 0.8246, 0.8219, 0.8176 |
| 20 | `tfidf_lr` | 81.94% ± 0.38% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8129, 0.8220, 0.8240, 0.8181, 0.8199 |
| 21 | `tfidf_cnb` | 81.89% ± 0.47% | clf__alpha=1.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8109, 0.8202, 0.8244, 0.8220, 0.8170 |
| 22 | `torch_mlp` | 81.85% ± 0.22% | mlp__epochs=5.0, mlp__hidden=128.0 | 0.8177, 0.8206, 0.8201, 0.8147, 0.8194 |
| 23 | `tfidf_sgd` | 81.82% ± 0.39% | clf__alpha=0.0001, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8109, 0.8221, 0.8182, 0.8204, 0.8195 |
| 24 | `tfidf_ridge` | 81.82% ± 0.24% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8147, 0.8196, 0.8179, 0.8219, 0.8168 |
| 25 | `tfidf_sgd` | 81.81% ± 0.38% | clf__alpha=0.0001, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8112, 0.8223, 0.8175, 0.8208, 0.8190 |
| 26 | `tfidf_sgd` | 81.80% ± 0.40% | clf__alpha=0.0001, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8104, 0.8216, 0.8178, 0.8202, 0.8202 |
| 27 | `tfidf_ridge` | 81.79% ± 0.31% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8133, 0.8198, 0.8166, 0.8227, 0.8172 |
| 28 | `torch_mlp` | 81.79% ± 0.31% | mlp__epochs=5.0, mlp__hidden=128.0 | 0.8158, 0.8196, 0.8175, 0.8228, 0.8140 |
| 29 | `tfidf_lr` | 81.78% ± 0.35% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8109, 0.8202, 0.8202, 0.8190, 0.8185 |
| 30 | `tfidf_ridge` | 81.78% ± 0.44% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8113, 0.8156, 0.8213, 0.8238, 0.8168 |
| 31 | `tfidf_lr` | 81.77% ± 0.34% | tfidf__max_features=3000.0 | 0.8110, 0.8192, 0.8198, 0.8205, 0.8180 |
| 32 | `tfidf_ridge` | 81.77% ± 0.34% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8117, 0.8185, 0.8187, 0.8223, 0.8171 |
| 33 | `tfidf_lr` | 81.76% ± 0.36% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8109, 0.8206, 0.8205, 0.8192, 0.8166 |
| 34 | `tfidf_sgd` | 81.75% ± 0.32% | clf__alpha=1e-05, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8118, 0.8171, 0.8212, 0.8177, 0.8198 |
| 35 | `tfidf_sgd` | 81.74% ± 0.38% | clf__alpha=1e-05, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8102, 0.8171, 0.8201, 0.8187, 0.8209 |
| 36 | `tfidf_lr` | 81.73% ± 0.35% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8108, 0.8201, 0.8198, 0.8196, 0.8164 |
| 37 | `tfidf_sgd` | 81.68% ± 0.34% | clf__alpha=1e-05, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8104, 0.8171, 0.8201, 0.8186, 0.8180 |
| 38 | `torch_mlp` | 81.64% ± 0.26% | mlp__epochs=5.0, mlp__hidden=256.0 | 0.8189, 0.8171, 0.8159, 0.8117, 0.8186 |
| 39 | `tfidf_svc` | 81.60% ± 0.36% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8091, 0.8178, 0.8164, 0.8175, 0.8193 |
| 40 | `tfidf_svc` | 81.58% ± 0.34% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8091, 0.8181, 0.8174, 0.8181, 0.8166 |
| 41 | `tfidf_cnb` | 81.56% ± 0.55% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8062, 0.8152, 0.8198, 0.8221, 0.8145 |
| 42 | `tfidf_svc` | 81.55% ± 0.42% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8074, 0.8171, 0.8159, 0.8190, 0.8179 |
| 43 | `tfidf_cnb` | 81.54% ± 0.58% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8051, 0.8156, 0.8190, 0.8223, 0.8149 |
| 44 | `tfidf_cnb` | 81.54% ± 0.54% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8063, 0.8146, 0.8192, 0.8224, 0.8144 |
| 45 | `tfidf_cnb` | 81.47% ± 0.53% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8060, 0.8135, 0.8192, 0.8213, 0.8134 |
| 46 | `tfidf_nb` | 81.46% ± 0.53% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8060, 0.8135, 0.8182, 0.8219, 0.8134 |
| 47 | `tfidf_ridge` | 81.46% ± 0.57% | clf__alpha=0.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8054, 0.8133, 0.8189, 0.8220, 0.8133 |
| 48 | `tfidf_cnb` | 81.45% ± 0.52% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8059, 0.8131, 0.8193, 0.8205, 0.8137 |
| 49 | `tfidf_cnb` | 81.44% ± 0.55% | clf__alpha=1.0, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8052, 0.8131, 0.8185, 0.8213, 0.8140 |
| 50 | `tfidf_nb` | 81.44% ± 0.52% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8059, 0.8131, 0.8182, 0.8210, 0.8137 |
| 51 | `tfidf_nb` | 81.43% ± 0.55% | tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8052, 0.8131, 0.8175, 0.8219, 0.8140 |
| 52 | `torch_mlp` | 81.41% ± 0.23% | mlp__epochs=5.0, mlp__hidden=256.0 | 0.8109, 0.8167, 0.8143, 0.8164, 0.8122 |
| 53 | `tfidf_sgd` | 81.40% ± 0.44% | clf__alpha=1e-05, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8090, 0.8087, 0.8155, 0.8190, 0.8179 |
| 54 | `tfidf_cnb` | 81.37% ± 0.54% | clf__alpha=1.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8043, 0.8132, 0.8189, 0.8190, 0.8133 |
| 55 | `tfidf_cnb` | 81.36% ± 0.54% | clf__alpha=1.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8039, 0.8132, 0.8174, 0.8197, 0.8137 |
| 56 | `tfidf_cnb` | 81.35% ± 0.53% | clf__alpha=1.5, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8039, 0.8135, 0.8181, 0.8189, 0.8134 |
| 57 | `tfidf_lr` | 81.32% ± 0.47% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8070, 0.8173, 0.8193, 0.8090, 0.8134 |
| 58 | `tfidf_ridge` | 81.27% ± 0.32% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8070, 0.8158, 0.8113, 0.8148, 0.8144 |
| 59 | `tfidf_ridge` | 81.24% ± 0.35% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8063, 0.8152, 0.8108, 0.8144, 0.8153 |
| 60 | `tfidf_ridge` | 81.24% ± 0.35% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8059, 0.8151, 0.8113, 0.8147, 0.8148 |
| 61 | `tfidf_ridge` | 81.15% ± 0.35% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8054, 0.8156, 0.8102, 0.8124, 0.8137 |
| 62 | `tfidf_ridge` | 81.15% ± 0.30% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8060, 0.8147, 0.8110, 0.8124, 0.8132 |
| 63 | `tfidf_svc` | 81.14% ± 0.29% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8073, 0.8089, 0.8144, 0.8141, 0.8124 |
| 64 | `tfidf_ridge` | 81.14% ± 0.29% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8066, 0.8155, 0.8106, 0.8128, 0.8113 |
| 65 | `tfidf_ridge` | 81.09% ± 0.52% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8012, 0.8102, 0.8150, 0.8156, 0.8124 |
| 66 | `tfidf_sgd` | 81.08% ± 0.39% | clf__alpha=0.0001, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8054, 0.8173, 0.8118, 0.8095, 0.8099 |
| 67 | `torch_mlp` | 81.07% ± 0.33% | mlp__epochs=10.0, mlp__hidden=128.0 | 0.8078, 0.8124, 0.8095, 0.8163, 0.8075 |
| 68 | `tfidf_sgd` | 81.03% ± 0.45% | clf__alpha=0.0001, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.8021, 0.8155, 0.8100, 0.8128, 0.8113 |
| 69 | `tfidf_sgd` | 81.02% ± 0.46% | clf__alpha=0.0001, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.8018, 0.8154, 0.8102, 0.8129, 0.8109 |
| 70 | `tfidf_cnb` | 81.00% ± 0.50% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8020, 0.8121, 0.8156, 0.8137, 0.8065 |
| 71 | `tfidf_pa` | 81.00% ± 0.25% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8085, 0.8059, 0.8128, 0.8120, 0.8106 |
| 72 | `tfidf_pa` | 81.00% ± 0.38% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8090, 0.8039, 0.8147, 0.8131, 0.8091 |
| 73 | `torch_mlp` | 80.99% ± 0.17% | mlp__epochs=10.0, mlp__hidden=128.0 | 0.8125, 0.8090, 0.8081, 0.8087, 0.8113 |
| 74 | `torch_mlp` | 80.99% ± 0.13% | mlp__epochs=10.0, mlp__hidden=256.0 | 0.8091, 0.8117, 0.8100, 0.8078, 0.8107 |
| 75 | `tfidf_sgd` | 80.99% ± 0.48% | clf__alpha=0.0001, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8010, 0.8150, 0.8098, 0.8128, 0.8107 |
| 76 | `tfidf_cnb` | 80.98% ± 0.52% | clf__alpha=1.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8013, 0.8094, 0.8171, 0.8127, 0.8084 |
| 77 | `tfidf_nb` | 80.96% ± 0.51% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8013, 0.8109, 0.8158, 0.8133, 0.8067 |
| 78 | `tfidf_cnb` | 80.96% ± 0.52% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8013, 0.8109, 0.8163, 0.8128, 0.8067 |
| 79 | `torch_mlp` | 80.88% ± 0.28% | mlp__epochs=10.0, mlp__hidden=256.0 | 0.8073, 0.8086, 0.8108, 0.8128, 0.8048 |
| 80 | `tfidf_pa` | 80.87% ± 0.33% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8082, 0.8043, 0.8105, 0.8140, 0.8065 |
| 81 | `tfidf_ridge` | 80.84% ± 0.45% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.8008, 0.8068, 0.8101, 0.8144, 0.8101 |
| 82 | `tfidf_pa` | 80.81% ± 0.41% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8063, 0.8033, 0.8110, 0.8144, 0.8053 |
| 83 | `tfidf_pa` | 80.56% ± 0.37% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8075, 0.8028, 0.8116, 0.8051, 0.8009 |
| 84 | `tfidf_pa` | 80.55% ± 0.28% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.8025, 0.8048, 0.8091, 0.8085, 0.8025 |
| 85 | `tfidf_pa` | 80.48% ± 0.43% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7993, 0.8022, 0.8094, 0.8102, 0.8026 |
| 86 | `tfidf_pa` | 80.42% ± 0.29% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8039, 0.8028, 0.8077, 0.8070, 0.7998 |
| 87 | `tfidf_pa` | 80.41% ± 0.36% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8039, 0.8018, 0.8094, 0.8066, 0.7990 |
| 88 | `tfidf_pa` | 80.41% ± 0.38% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8062, 0.8022, 0.8089, 0.8054, 0.7978 |
| 89 | `tfidf_pa` | 80.40% ± 0.34% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7989, 0.8036, 0.8095, 0.8051, 0.8030 |
| 90 | `tfidf_pa` | 80.40% ± 0.29% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.8056, 0.8025, 0.8082, 0.8040, 0.7996 |
| 91 | `tfidf_sgd` | 80.40% ± 0.47% | clf__alpha=0.0001, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7976, 0.8117, 0.8059, 0.8021, 0.8025 |
| 92 | `tfidf_pa` | 80.38% ± 0.27% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.8056, 0.8040, 0.8078, 0.8004, 0.8013 |
| 93 | `tfidf_pa` | 80.36% ± 0.30% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8047, 0.8004, 0.8050, 0.8081, 0.8002 |
| 94 | `tfidf_cnb` | 80.34% ± 0.39% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7964, 0.8059, 0.8064, 0.8067, 0.8017 |
| 95 | `tfidf_cnb` | 80.34% ± 0.45% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7960, 0.8071, 0.8062, 0.8074, 0.8003 |
| 96 | `tfidf_cnb` | 80.34% ± 0.37% | clf__alpha=0.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7967, 0.8060, 0.8059, 0.8063, 0.8019 |
| 97 | `tfidf_cnb` | 80.33% ± 0.42% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7956, 0.8067, 0.8054, 0.8066, 0.8025 |
| 98 | `tfidf_nb` | 80.33% ± 0.42% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7956, 0.8067, 0.8045, 0.8074, 0.8025 |
| 99 | `tfidf_cnb` | 80.32% ± 0.40% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7956, 0.8066, 0.8047, 0.8062, 0.8030 |
| 100 | `tfidf_cnb` | 80.32% ± 0.45% | clf__alpha=1.0, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7952, 0.8068, 0.8052, 0.8074, 0.8014 |
| 101 | `tfidf_nb` | 80.32% ± 0.46% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7952, 0.8070, 0.8044, 0.8081, 0.8014 |
| 102 | `tfidf_nb` | 80.32% ± 0.41% | tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7956, 0.8066, 0.8039, 0.8068, 0.8030 |
| 103 | `tfidf_cnb` | 80.28% ± 0.44% | clf__alpha=1.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7944, 0.8068, 0.8048, 0.8051, 0.8026 |
| 104 | `tfidf_cnb` | 80.27% ± 0.49% | clf__alpha=1.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7939, 0.8073, 0.8056, 0.8060, 0.8009 |
| 105 | `tfidf_cnb` | 80.26% ± 0.49% | clf__alpha=1.5, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7935, 0.8070, 0.8048, 0.8060, 0.8019 |
| 106 | `tfidf_pa` | 80.15% ± 0.45% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 3) | 0.8024, 0.7982, 0.8051, 0.8071, 0.7948 |
| 107 | `tfidf_pa` | 80.14% ± 0.33% | clf__C=0.5, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7972, 0.7978, 0.8055, 0.8037, 0.8026 |
| 108 | `tfidf_pa` | 80.13% ± 0.37% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 5) | 0.7986, 0.8014, 0.8043, 0.8062, 0.7960 |
| 109 | `tfidf_pa` | 80.06% ± 0.43% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 10) | 0.7985, 0.7995, 0.8056, 0.8051, 0.7942 |
| 110 | `tfidf_pa` | 80.00% ± 0.53% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.8028, 0.7949, 0.8071, 0.8024, 0.7929 |
| 111 | `tfidf_pa` | 79.99% ± 0.40% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7959, 0.8067, 0.7962, 0.8018, 0.7990 |
| 112 | `tfidf_pa` | 79.98% ± 0.37% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7958, 0.8067, 0.7993, 0.7995, 0.7978 |
| 113 | `tfidf_pa` | 79.94% ± 0.48% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7941, 0.8078, 0.7964, 0.8010, 0.7975 |
| 114 | `tfidf_pa` | 79.69% ± 0.44% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=5000.0, tfidf__ngram_range=(1, 1) | 0.7940, 0.7949, 0.8040, 0.7997, 0.7918 |
| 115 | `tfidf_pa` | 79.69% ± 0.55% | clf__C=1.0, clf__loss=hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7956, 0.7952, 0.8020, 0.8035, 0.7881 |
| 116 | `tfidf_pa` | 79.34% ± 0.35% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7893, 0.7918, 0.7945, 0.7995, 0.7917 |
| 117 | `tfidf_pa` | 79.31% ± 0.34% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7887, 0.7906, 0.7949, 0.7985, 0.7927 |
| 118 | `tfidf_pa` | 79.29% ± 0.41% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7887, 0.7890, 0.7948, 0.7997, 0.7922 |
| 119 | `tfidf_pa` | 79.25% ± 0.42% | clf__C=0.5, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7924, 0.7860, 0.7981, 0.7959, 0.7903 |
| 120 | `tfidf_pa` | 78.72% ± 0.42% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 3) | 0.7822, 0.7941, 0.7861, 0.7894, 0.7840 |
| 121 | `tfidf_pa` | 78.68% ± 0.40% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 5) | 0.7809, 0.7932, 0.7871, 0.7879, 0.7850 |
| 122 | `tfidf_pa` | 78.63% ± 0.34% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 10) | 0.7822, 0.7897, 0.7867, 0.7902, 0.7826 |
| 123 | `tfidf_pa` | 78.53% ± 0.73% | clf__C=1.0, clf__loss=squared_hinge, tfidf__max_features=3000.0, tfidf__ngram_range=(1, 1) | 0.7876, 0.7809, 0.7912, 0.7933, 0.7734 |
| 124 | `sbert_svc` | 76.37% ± 0.41% | clf__C=2.0, sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.7672, 0.7561, 0.7627, 0.7653, 0.7672 |
| 125 | `sbert_svc` | 76.22% ± 0.44% | clf__C=1.0, sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.7661, 0.7540, 0.7614, 0.7638, 0.7657 |
| 126 | `sbert_svc` | 76.15% ± 0.51% | clf__C=0.5, sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.7642, 0.7517, 0.7613, 0.7655, 0.7647 |
| 127 | `sbert_lr` | 75.44% ± 0.56% | sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.7571, 0.7457, 0.7500, 0.7591, 0.7603 |
| 128 | `sbert_lr` | 75.44% ± 0.56% | sbert__sbert_model=sentence-transformers/distiluse-base-multilingual-cased-v2 | 0.7571, 0.7457, 0.7500, 0.7591, 0.7603 |
| 129 | `sbert_svc` | 72.55% ± 0.47% | clf__C=2.0, sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.7297, 0.7254, 0.7178, 0.7310, 0.7233 |
| 130 | `sbert_svc` | 72.39% ± 0.41% | clf__C=1.0, sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.7272, 0.7249, 0.7168, 0.7283, 0.7224 |
| 131 | `sbert_svc` | 72.16% ± 0.32% | clf__C=0.5, sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.7241, 0.7227, 0.7154, 0.7237, 0.7220 |
| 132 | `sbert_lr` | 70.81% ± 0.27% | sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.7112, 0.7074, 0.7055, 0.7050, 0.7114 |
| 133 | `sbert_lr` | 70.81% ± 0.27% | sbert__sbert_model=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 | 0.7112, 0.7074, 0.7055, 0.7050, 0.7114 |


from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List

DEFAULT_OUTPUT = Path("reports/experiments_report.md")

EXCLUDED_COLUMNS = {"dataset", "model", "mean_acc", "std_acc", "scores"}


def parse_float(value: str | None) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def clean_param(value: str) -> str:
    if value is None:
        return ""
    value = value.strip()
    if value == "" or value.lower() == "nan":
        return ""
    return value


def format_params(row: Dict[str, str]) -> str:
    params: List[str] = []
    for key, value in sorted(row.items()):
        if key in EXCLUDED_COLUMNS:
            continue
        cleaned = clean_param(value)
        if not cleaned:
            continue
        params.append(f"{key}={cleaned}")
    return ", ".join(params) if params else "—"


def build_section(dataset: str, rows: Iterable[Dict[str, str]], top: int | None) -> List[str]:
    items = sorted(
        rows,
        key=lambda r: (
            -(parse_float(r.get("mean_acc")) or float("-inf")),
            parse_float(r.get("std_acc")) or float("inf"),
        ),
    )
    if top is not None:
        items = items[:top]

    section: List[str] = []
    section.append(f"## {dataset}\n")
    section.append("| Rank | Modelo | Acurácia (média ± desvio) | Parâmetros | Scores |\n")
    section.append("| --- | --- | --- | --- | --- |\n")
    for idx, row in enumerate(items, start=1):
        mean_acc = parse_float(row.get("mean_acc"))
        std_acc = parse_float(row.get("std_acc"))
        if mean_acc is not None:
            acc_text = f"{mean_acc*100:.2f}%"
        else:
            acc_text = "?"
        if std_acc is not None:
            acc_text += f" ± {std_acc*100:.2f}%"
        params_text = format_params(row)
        scores = row.get("scores", "")
        if scores:
            scores = scores.replace(";", ", ")
        else:
            scores = "—"
        section.append(
            f"| {idx} | `{row.get('model', '')}` | {acc_text} | {params_text} | {scores} |\n"
        )
    section.append("\n")
    return section


def collect_best_rows(groups: Dict[str, List[Dict[str, str]]]) -> List[str]:
    summary: List[str] = []
    summary.append("## Melhores resultados por conjunto\n\n")
    for dataset, rows in sorted(groups.items()):
        best = max(
            rows,
            key=lambda r: parse_float(r.get("mean_acc")) or float("-inf"),
        )
        mean_acc = parse_float(best.get("mean_acc"))
        std_acc = parse_float(best.get("std_acc"))
        acc_text = f"{mean_acc*100:.2f}%" if mean_acc is not None else "?"
        if std_acc is not None:
            acc_text += f" ± {std_acc*100:.2f}%"
        params_text = format_params(best)
        summary.append(
            f"- **{dataset}**: `{best.get('model', '')}` com {acc_text} ({params_text})\n"
        )
    summary.append("\n")
    return summary


def generate_report(input_path: Path, output_path: Path, top: int | None) -> None:
    if not input_path.exists():
        raise FileNotFoundError(f"Arquivo de resultados não encontrado: {input_path}")

    groups: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    with input_path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            dataset = row.get("dataset", "desconhecido")
            groups[dataset].append(row)

    if not groups:
        raise ValueError("Nenhum resultado encontrado para gerar relatório.")

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines: List[str] = []
    lines.append("# Relatório de Resultados\n\n")
    lines.append(f"Gerado automaticamente em {now}.\n\n")

    lines.extend(collect_best_rows(groups))

    for dataset, rows in sorted(groups.items()):
        lines.extend(build_section(dataset, rows, top))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(lines), encoding="utf-8")


def main(argv: List[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Gera relatório em Markdown dos experimentos.")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("experiments.csv"),
        help="Caminho para o CSV de resultados (default: experiments.csv)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Arquivo de saída em Markdown (default: reports/experiments_report.md)",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=None,
        help="Número máximo de linhas por conjunto; use 0 para todos.",
    )
    args = parser.parse_args(argv)

    top = args.top if args.top and args.top > 0 else None
    generate_report(args.input, args.output, top)


if __name__ == "__main__":
    main()

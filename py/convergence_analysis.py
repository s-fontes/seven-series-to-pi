from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from compute import run

SERIES_LIST = [
    "leibniz",
    "nilakantha",
    "machin",
    "euler",
    "ramanujan",
    "chudnovsky",
    "bbp",
]
PRECISIONS = ["float", "double"]


def generate_convergence_csv(out_path: Path, eps: float = 1e-5) -> None:
    """Generate a CSV with convergence deltas for all algorithms."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["series", "precision", "k", "pi", "error", "delta_pi", "delta_error"]
        )
        for series in SERIES_LIST:
            for precision in PRECISIONS:
                results = run(series, precision, eps)
                prev_pi: float | None = None
                prev_error: float | None = None
                for row in results:
                    delta_pi = 0.0 if prev_pi is None else row.pi - prev_pi
                    delta_err = 0.0 if prev_error is None else row.error - prev_error
                    writer.writerow(
                        [
                            series,
                            precision,
                            row.k,
                            row.pi,
                            row.error,
                            delta_pi,
                            delta_err,
                        ]
                    )
                    prev_pi = row.pi
                    prev_error = row.error


def calculate_order(errors: list[float]) -> float:
    """Estimate the empirical order of convergence from error history."""
    if len(errors) < 3:
        return 0.0
    orders: list[float] = []
    for i in range(2, len(errors)):
        e_n = abs(errors[i])
        e_nm1 = abs(errors[i - 1])
        e_nm2 = abs(errors[i - 2])
        if e_nm1 == 0 or e_nm2 == 0:
            continue
        num = math.log(e_n / e_nm1)
        den = math.log(e_nm1 / e_nm2)
        if den != 0:
            orders.append(num / den)
    if not orders:
        return 0.0
    return sum(orders) / len(orders)


def generate_convergence_table(out_path: Path, eps: float = 1e-5) -> None:
    """Generate a LaTeX table with convergence order for all algorithms."""
    summary: list[tuple[str, str, float]] = []
    for series in SERIES_LIST:
        for precision in PRECISIONS:
            results = run(series, precision, eps)
            errors = [row.error for row in results]
            order = calculate_order(errors)
            summary.append((series, precision, order))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        f.write("\\begin{tabular}{l l c}\n")
        f.write("\\toprule\n")
        f.write("Series & Precision & Order\\\\\n")
        f.write("\\midrule\n")
        for series, precision, order in summary:
            f.write(f"{series} & {precision} & {order:.2f} \\\\n")
        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")


def main(argv: list[str] | None = None) -> None:
    args = argv or sys.argv[1:]
    eps = 1e-5
    if len(args) > 1:
        print("Usage: python convergence_analysis.py [epsilon]")
        raise SystemExit(1)
    if args:
        try:
            eps = float(args[0])
        except ValueError:
            print("epsilon must be a float")
            raise SystemExit(1)

    base = Path(__file__).resolve().parents[1] / "out" / "analysis"
    csv_path = base / "convergence.csv"
    tex_path = base / "convergence_table.tex"
    generate_convergence_csv(csv_path, eps)
    generate_convergence_table(tex_path, eps)
    print(f"Written {csv_path}")
    print(f"Written {tex_path}")


if __name__ == "__main__":
    main()

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

plt.switch_backend("Agg")


def _plot_file(csv_path: Path, out_dir: Path) -> None:
    """Generate a convergence graph for a single CSV file."""
    ks: list[int] = []
    errors: list[float] = []
    with csv_path.open() as f:
        reader = csv.reader(f)
        next(reader, None)  # header
        for row in reader:
            ks.append(int(row[0]))
            errors.append(float(row[2]))

    plt.figure()
    plt.plot(ks, errors)
    plt.yscale("log")
    plt.xlabel("k")
    plt.ylabel("error")
    plt.title(csv_path.stem)
    out_file = out_dir / f"{csv_path.stem}.png"
    plt.savefig(out_file)
    plt.close()


def generate_graphs(data_dir: Path, graph_dir: Path) -> None:
    """Generate graphs for all CSV files in ``data_dir``.

    Parameters
    ----------
    data_dir:
        Directory containing CSV files with ``k, pi, error`` columns.
    graph_dir:
        Destination directory for the generated PNG graphs.
    """
    graph_dir.mkdir(parents=True, exist_ok=True)

    for csv_path in data_dir.glob("*.csv"):
        _plot_file(csv_path, graph_dir)


def main() -> None:
    base = Path(__file__).resolve().parents[1] / "out"
    data_dir = base / "data"
    graph_dir = base / "graphs"

    generate_graphs(data_dir, graph_dir)



if __name__ == "__main__":
    main()

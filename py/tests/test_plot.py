import csv
from pathlib import Path
import importlib
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
plot = importlib.import_module("plot")


def test_generate_graphs_creates_png(tmp_path):
    data_dir = tmp_path / "data"
    graph_dir = tmp_path / "graphs"
    data_dir.mkdir()

    csv_path = data_dir / "sample.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["k", "pi", "error"])
        writer.writerow([0, 3.14, 0.01])
        writer.writerow([1, 3.141, 0.001])

    plot.generate_graphs(data_dir, graph_dir)

    assert (graph_dir / "sample.png").exists()

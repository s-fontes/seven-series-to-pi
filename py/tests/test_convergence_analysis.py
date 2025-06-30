import csv
import importlib
import sys
from pathlib import Path
import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
analysis = importlib.import_module("convergence_analysis")
compute = importlib.import_module("compute")


def test_generate_convergence_csv(tmp_path):
    out_file = tmp_path / "conv.csv"
    analysis.generate_convergence_csv(out_file, 1e-3)

    assert out_file.exists()
    with out_file.open() as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == [
            "series",
            "precision",
            "k",
            "pi",
            "error",
            "delta_pi",
            "delta_error",
        ]
        rows = list(reader)
        assert rows
        first = rows[0]
        assert float(first[5]) == 0.0
        assert float(first[6]) == 0.0

        series = analysis.SERIES_LIST[0]
        precision = analysis.PRECISIONS[0]
        results = compute.run(series, precision, 1e-3)
        if len(results) > 1:
            expected = results[1].pi - results[0].pi
            row = rows[1]
            assert abs(float(row[5]) - expected) < 1e-12


def test_calculate_order():
    errors = [1e-1, 1e-2, 1e-4, 1e-8]
    order = analysis.calculate_order(errors)
    assert pytest.approx(order, rel=0.1) == 2.0


def test_generate_convergence_table(tmp_path):
    out_file = tmp_path / "table.tex"
    analysis.generate_convergence_table(out_file, 1e-3)
    assert out_file.exists()
    content = out_file.read_text()
    assert "\\begin{tabular}" in content


def test_main_creates_file():
    out_base = Path(__file__).resolve().parents[2] / "out"
    analysis_dir = out_base / "analysis"
    if out_base.exists():
        import shutil
        shutil.rmtree(out_base)

    analysis.main(["1e-3"])

    file_path = analysis_dir / "convergence.csv"
    table_path = analysis_dir / "convergence_table.tex"
    assert file_path.exists()
    assert table_path.exists()
    with file_path.open() as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header[0] == "series"

    import shutil
    shutil.rmtree(out_base)

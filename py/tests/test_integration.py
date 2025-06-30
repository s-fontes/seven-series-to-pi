import csv
import subprocess
import pytest
import importlib
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
main = importlib.import_module("compute").main


class TestIntegration:
    """End-to-end tests invoking the main entry point."""

    def test_main_function_execution(self, tmp_path):
        out_base = Path(__file__).resolve().parents[2] / "out"
        data_dir = out_base / "data"

        if out_base.exists():
            import shutil
            shutil.rmtree(out_base)

        main(["1e-3"])

        expected_files = [
            f"{series}_{precision}.csv"
            for series in [
                "leibniz",
                "nilakantha",
                "machin",
                "euler",
                "ramanujan",
                "chudnovsky",
                "bbp",
            ]
            for precision in ["float", "double"]
        ]

        for fname in expected_files:
            fp = data_dir / fname
            assert fp.exists(), f"Arquivo {fname} não foi criado"
            with fp.open() as f:
                reader = csv.reader(f)
                header = next(reader)
                assert header == ["k", "pi", "error"]
                rows = list(reader)
                assert rows

        # cleanup
        import shutil
        shutil.rmtree(out_base)


    def test_makefile_integration(self):
        try:
            result = subprocess.run(["make", "build"], capture_output=True, text=True)
            assert result.returncode == 0
        except FileNotFoundError:
            pytest.skip("make não disponível")

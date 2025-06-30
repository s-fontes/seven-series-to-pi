import math
import subprocess
import sys
from pathlib import Path
import importlib

sys.path.append(str(Path(__file__).resolve().parents[1]))
compute = importlib.import_module("compute")


def test_leibniz_double_accuracy() -> None:
    results = compute.run("leibniz", "double")
    assert results[0].k == 0
    assert abs(results[-1].pi - math.pi) < 1e-2


def test_cli_validation() -> None:
    script = Path(__file__).resolve().parents[1] / "compute.py"
    proc = subprocess.run(
        [sys.executable, str(script), "not-a-number", "extra"],
        capture_output=True,
    )
    assert proc.returncode != 0


def test_machin_double_wrapper() -> None:
    results = compute.run_machin_double()
    assert abs(results[-1].pi - math.pi) < 1e-5


def test_leibniz_float_wrapper() -> None:
    results = compute.run_leibniz_float(eps=1.0)
    assert results[0].k == 0
    assert len(results) <= 100000


def test_error_field() -> None:
    results = compute.run_leibniz_double(eps=1.0)
    first = results[0]
    assert math.isclose(first.error, (first.pi - math.pi) ** 2, rel_tol=0, abs_tol=1e-12)


def test_euler_double_wrapper() -> None:
    results = compute.run_euler_double()
    assert abs(results[-1].pi - math.pi) < 1e-2


def test_ramanujan_double_wrapper() -> None:
    results = compute.run_ramanujan_double()
    assert abs(results[-1].pi - math.pi) < 1e-5


def test_chudnovsky_double_wrapper() -> None:
    results = compute.run_chudnovsky_double()
    assert abs(results[-1].pi - math.pi) < 1e-5

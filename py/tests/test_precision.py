import math
import importlib
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
compute = importlib.import_module("compute")
run = compute.run


class TestPrecision:
    """Tests around error calculation and precision."""

    def test_error_calculation_accuracy(self):
        for series in ["machin", "ramanujan"]:
            results = run(series, "double", 1e-8)
            final = results[-1]
            real_error = (final.pi - math.pi) ** 2
            calculated_error = final.error
            assert abs(real_error - calculated_error) / real_error < 0.01

    def test_float_vs_double_precision(self):
        epsilon = 1e-6
        for series in ["machin", "nilakantha"]:
            results_float = run(series, "float", epsilon)
            results_double = run(series, "double", epsilon)
            assert results_double[-1].error <= results_float[-1].error * 1.1

    def test_convergence_monotonicity(self):
        results = run("nilakantha", "double", 1e-6)
        decreasing = 0
        for i in range(1, len(results)):
            if results[i].error <= results[i - 1].error:
                decreasing += 1
        ratio = decreasing / (len(results) - 1)
        assert ratio > 0.8

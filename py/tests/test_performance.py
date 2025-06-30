import pytest
import time
import importlib
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
compute = importlib.import_module("compute")
run = compute.run


class TestPerformance:
    """Simple performance checks for algorithm speed."""

    def test_algorithm_speed_ranking(self):
        epsilon = 1e-4
        algorithms = {
            "chudnovsky": "ultra_fast",
            "ramanujan": "ultra_fast",
            "machin": "fast",
            "bbp": "fast",
            "nilakantha": "medium",
            "euler": "slow",
            "leibniz": "slow",
        }

        results = {}
        for algo in algorithms:
            start_time = time.perf_counter()
            result = run(algo, "double", epsilon)
            end_time = time.perf_counter()
            results[algo] = {
                "time": end_time - start_time,
                "iterations": len(result),
            }

        for algo in [k for k, v in algorithms.items() if v == "ultra_fast"]:
            assert results[algo]["iterations"] < 10

        for algo in [k for k, v in algorithms.items() if v == "fast"]:
            assert results[algo]["iterations"] < 50

    def test_float_vs_double_performance(self):
        """Ensure float and double modes perform similarly."""
        epsilon = 1e-5
        for series in ["machin", "nilakantha"]:
            results_float = run(series, "float", epsilon)
            results_double = run(series, "double", epsilon)

            iter_ratio = max(len(results_float), len(results_double)) / min(
                len(results_float), len(results_double)
            )
            assert iter_ratio < 1.5

    @pytest.mark.slow
    def test_large_epsilon_performance(self):
        results = run("ramanujan", "double", 1e-12)
        assert len(results) < 100

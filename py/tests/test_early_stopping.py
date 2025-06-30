import importlib
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
compute = importlib.import_module("compute")
run = compute.run


class TestEarlyStopping:
    """Validate that algorithms stop once the desired precision is reached."""

    def test_early_stopping_large_epsilon(self, all_algorithms, precision_types):
        for series in all_algorithms:
            for precision in precision_types:
                results = run(series, precision, 1e-2)
                assert len(results) < 100000, f"{series}_{precision} excedeu MAX_ITER"
                assert results[-1].error < 1e-2

    def test_early_stopping_medium_epsilon(self):
        fast_algorithms = ["ramanujan", "chudnovsky", "machin", "bbp"]
        for series in fast_algorithms:
            results = run(series, "double", 1e-5)
            assert len(results) < 1000, f"{series} demorou para convergir"
            assert results[-1].error < 1e-5

    def test_slow_algorithms_behavior(self):
        results_euler = run("euler", "double", 1e-4)
        results_leibniz = run("leibniz", "double", 1e-4)

        assert len(results_euler) <= 100000
        assert len(results_leibniz) <= 100000

        if len(results_euler) < 100000:
            assert results_euler[-1].error < 1e-4

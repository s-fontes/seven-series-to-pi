import pytest
import importlib
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
compute = importlib.import_module("compute")
run = compute.run


class TestRobustness:
    """Edge case and invalid input handling."""

    def test_invalid_series_name(self):
        with pytest.raises(ValueError, match="Unknown series"):
            run("invalid_series", "double", 1e-5)

    def test_invalid_precision_type(self):
        with pytest.raises(ValueError, match="Unknown precision"):
            run("leibniz", "invalid_precision", 1e-5)

    def test_extreme_epsilon_values(self):
        results = run("machin", "float", 1.0)
        assert len(results) == 1

        results = run("ramanujan", "double", 1e-15)
        assert 1 <= len(results) <= 100000

    def test_epsilon_zero(self):
        results = run("ramanujan", "double", 0.0)
        assert len(results) >= 1

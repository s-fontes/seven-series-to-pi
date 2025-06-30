import pytest


def pytest_configure(config: pytest.Config) -> None:
    """Register custom markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )


@pytest.fixture(scope="session")
def test_epsilon() -> float:
    """Default epsilon used across tests."""
    return 1e-4


@pytest.fixture
def all_algorithms() -> list[str]:
    """Return all available algorithm names."""
    return [
        "leibniz",
        "nilakantha",
        "machin",
        "euler",
        "ramanujan",
        "chudnovsky",
        "bbp",
    ]


@pytest.fixture
def precision_types() -> list[str]:
    """Return available precision types."""
    return ["float", "double"]

from __future__ import annotations

import ctypes
import csv
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from plot import generate_graphs

LIB_PATH = Path(__file__).resolve().parents[1] / "build" / "libpi_series.so"


def _load_lib() -> ctypes.CDLL:
    lib = ctypes.CDLL(str(LIB_PATH))
    lib.calculate_error_float.argtypes = [ctypes.c_float]
    lib.calculate_error_float.restype = ctypes.c_float
    lib.calculate_error_double.argtypes = [ctypes.c_double]
    lib.calculate_error_double.restype = ctypes.c_double
    return lib


class PiResult(ctypes.Structure):
    _fields_ = [
        ("k", ctypes.c_ulong),
        ("pi", ctypes.c_double),
    ]


@dataclass
class Iteration:
    """Container for a single iteration result."""

    k: int
    pi: float
    error: float


def run(series: str, precision: str, eps: float = 1e-5) -> list[Iteration]:
    lib = _load_lib()
    if precision not in {"float", "double"}:
        raise ValueError(f"Unknown precision: {precision}")
    suffix = "f" if precision == "float" else "d"
    func_name = f"run_{series}_{suffix}"
    try:
        func = getattr(lib, func_name)
    except AttributeError as exc:
        raise ValueError(f"Unknown series: {series}") from exc
    etype = ctypes.c_float if precision == "float" else ctypes.c_double
    func.argtypes = [etype, ctypes.POINTER(ctypes.c_ulong)]
    func.restype = ctypes.POINTER(PiResult)
    lib.free_results.argtypes = [ctypes.POINTER(PiResult)]
    lib.free_results.restype = None

    length = ctypes.c_ulong()
    eps_sq = eps * eps
    ptr = func(etype(eps_sq), ctypes.byref(length))
    if not ptr:
        raise RuntimeError("C function returned NULL")
    results: list[Iteration] = []
    for i in range(length.value):
        row = ptr[i]
        if precision == "float":
            error = lib.calculate_error_float(ctypes.c_float(row.pi))
        else:
            error = lib.calculate_error_double(ctypes.c_double(row.pi))
        results.append(Iteration(k=row.k, pi=row.pi, error=float(error)))
    lib.free_results(ptr)
    return results


def run_leibniz_float(eps: float = 1e-5) -> list[Iteration]:
    return run("leibniz", "float", eps)


def run_leibniz_double(eps: float = 1e-5) -> list[Iteration]:
    return run("leibniz", "double", eps)


def run_nilakantha_float(eps: float = 1e-5) -> list[Iteration]:
    return run("nilakantha", "float", eps)


def run_nilakantha_double(eps: float = 1e-5) -> list[Iteration]:
    return run("nilakantha", "double", eps)


def run_machin_float(eps: float = 1e-5) -> list[Iteration]:
    return run("machin", "float", eps)


def run_machin_double(eps: float = 1e-5) -> list[Iteration]:
    return run("machin", "double", eps)


def run_euler_float(eps: float = 1e-5) -> list[Iteration]:
    return run("euler", "float", eps)


def run_euler_double(eps: float = 1e-5) -> list[Iteration]:
    return run("euler", "double", eps)


def run_ramanujan_float(eps: float = 1e-5) -> list[Iteration]:
    return run("ramanujan", "float", eps)


def run_ramanujan_double(eps: float = 1e-5) -> list[Iteration]:
    return run("ramanujan", "double", eps)


def run_chudnovsky_float(eps: float = 1e-5) -> list[Iteration]:
    return run("chudnovsky", "float", eps)


def run_chudnovsky_double(eps: float = 1e-5) -> list[Iteration]:
    return run("chudnovsky", "double", eps)


def run_bbp_float(eps: float = 1e-5) -> list[Iteration]:
    return run("bbp", "float", eps)


def run_bbp_double(eps: float = 1e-5) -> list[Iteration]:
    return run("bbp", "double", eps)


def main(argv: list[str] | None = None) -> None:
    args = argv or sys.argv[1:]
    eps = 1e-5
    if len(args) > 1:
        print("Usage: python compute.py [epsilon]")
        raise SystemExit(1)
    if args:
        try:
            eps = float(args[0])
        except ValueError:
            print("epsilon must be a float")
            raise SystemExit(1)

    series_list = [
        "leibniz",
        "nilakantha",
        "machin",
        "euler",
        "ramanujan",
        "chudnovsky",
        "bbp",
    ]
    precisions = ["float", "double"]
    base_out = Path(__file__).resolve().parents[1] / "out"
    out_dir = base_out / "data"
    graph_dir = base_out / "graphs"
    out_dir.mkdir(parents=True, exist_ok=True)
    for series in series_list:
        for precision in precisions:
            results = run(series, precision, eps)
            csv_path = out_dir / f"{series}_{precision}.csv"
            with csv_path.open("w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["k", "pi", "error"])
                for row in results:
                    writer.writerow([row.k, row.pi, row.error])
    generate_graphs(out_dir, graph_dir)
    print("Done")


if __name__ == "__main__":
    main()

"""Performance Benchmarking for AI OS Components"""
import time
from dataclasses import dataclass, field
from typing import Any, Callable
from pathlib import Path
from datetime import datetime


@dataclass
class BenchmarkResult:
    """Result of a single benchmark run"""
    name: str
    iterations: int
    total_time_ms: float
    avg_time_ms: float
    min_time_ms: float
    max_time_ms: float
    timestamp: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "iterations": self.iterations,
            "total_time_ms": self.total_time_ms,
            "avg_time_ms": self.avg_time_ms,
            "min_time_ms": self.min_time_ms,
            "max_time_ms": self.max_time_ms,
            "timestamp": self.timestamp.isoformat()
        }


class Benchmark:
    """Performance benchmarking utility"""

    def __init__(self, name: str, iterations: int = 100):
        self.name = name
        self.iterations = iterations
        self.results: list[BenchmarkResult] = []

    def run(self, fn: Callable, *args, **kwargs) -> BenchmarkResult:
        """Run a function multiple times and measure performance"""
        times = []

        for _ in range(self.iterations):
            start = time.perf_counter()
            fn(*args, **kwargs)
            end = time.perf_counter()
            times.append((end - start) * 1000)  # Convert to ms

        result = BenchmarkResult(
            name=self.name,
            iterations=self.iterations,
            total_time_ms=sum(times),
            avg_time_ms=sum(times) / len(times),
            min_time_ms=min(times),
            max_time_ms=max(times)
        )

        self.results.append(result)
        return result


# Benchmark functions for AI OS components
def benchmark_agent_fleet_resolution(repo_root: Path) -> BenchmarkResult:
    """Benchmark agent fleet resolution"""
    from ai_os.agent_fleet import resolve_fleet

    bench = Benchmark("agent_fleet_resolution", iterations=50)
    return bench.run(lambda: resolve_fleet(repo_root))


def benchmark_pm_compiler_import() -> BenchmarkResult:
    """Benchmark PM compiler import time"""
    import importlib

    bench = Benchmark("pm_compiler_import", iterations=50)

    def do_import():
        import ai_os.pm_compiler
        importlib.reload(ai_os.pm_compiler)

    return bench.run(do_import)


def benchmark_memory_operations(repo_root: Path) -> BenchmarkResult:
    """Benchmark memory system operations"""
    from ai_os.memory import add_memory_entry

    bench = Benchmark("memory_add_entry", iterations=100)

    def do_add():
        add_memory_entry(
            repo_root,
            category="benchmark_test",
            content="Benchmark test entry",
            source="benchmark"
        )

    return bench.run(do_add)


def benchmark_local_worker_discovery(repo_root: Path) -> BenchmarkResult:
    """Benchmark task discovery in local worker"""
    from ai_os.local_worker import discover_tasks

    bench = Benchmark("task_discovery", iterations=50)

    def do_discover():
        discover_tasks(repo_root / "ops" / "tasks" / "pending")

    return bench.run(do_discover)


def benchmark_context_hub_operations(repo_root: Path) -> BenchmarkResult:
    """Benchmark context hub operations"""
    from ai_os.context_hub import compile_context

    bench = Benchmark("context_compile", iterations=20)

    test_context = {
        "mission": "Test mission",
        "initiative": "Test initiative",
        "constraints": []
    }

    return bench.run(compile_context, test_context, repo_root)


def benchmark_swarm_orchestrator() -> BenchmarkResult:
    """Benchmark swarm orchestrator operations"""
    from ai_os.swarm_orchestrator import SwarmOrchestrator

    bench = Benchmark("swarm_orchestrator", iterations=100)

    def do_orchestrate():
        orch = SwarmOrchestrator(Path("."))
        orch.create_execution([
            {"task_id": "t1", "agent_role": "architect", "description": "d"},
            {"task_id": "t2", "agent_role": "implementer", "description": "d"}
        ])

    return bench.run(do_orchestrate)


def run_all_benchmarks(repo_root: Path | None = None) -> dict[str, BenchmarkResult]:
    """Run all benchmarks and return results"""
    if repo_root is None:
        repo_root = Path(".")

    results = {}

    # Import benchmarks
    benchmarks = [
        ("swarm_orchestrator", benchmark_swarm_orchestrator),
    ]

    # Only run certain benchmarks that don't require complex setup
    for name, bench_fn in benchmarks:
        try:
            result = bench_fn()
            results[name] = result
            print(f"{name}: avg={result.avg_time_ms:.3f}ms, min={result.min_time_ms:.3f}ms, max={result.max_time_ms:.3f}ms")
        except Exception as e:
            print(f"{name}: ERROR - {e}")

    return results


if __name__ == "__main__":
    print("Running AI OS Benchmarks...")
    print("-" * 50)
    run_all_benchmarks()
    print("-" * 50)
    print("Benchmarks complete!")

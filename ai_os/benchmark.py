"""Performance Benchmarking for AI OS Components"""
import time
import json
from dataclasses import dataclass, field
from typing import Any, Callable
from pathlib import Path
from datetime import datetime
import tempfile
import shutil


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
            title="Benchmark Test Entry",
            content="Benchmark test entry content",
        )

    return bench.run(do_add)


def benchmark_local_worker_discovery(repo_root: Path) -> BenchmarkResult:
    """Benchmark task discovery in local worker"""
    from ai_os.local_worker import _discover_next_task
    from ai_os.contracts import ExecutorType

    bench = Benchmark("task_discovery", iterations=50)

    def do_discover():
        _discover_next_task(repo_root, ExecutorType.claude_code, None)

    return bench.run(do_discover)


def benchmark_context_hub_operations(repo_root: Path) -> BenchmarkResult:
    """Benchmark context hub operations"""
    from ai_os.context_hub import compile_context_bundle
    from ai_os.contracts import ContextBundle

    bench = Benchmark("context_compile", iterations=20)

    test_bundle = ContextBundle(
        bundle_id="benchmark-test",
        context_type="mission",
        content="Test mission content",
        metadata={}
    )

    return bench.run(compile_context_bundle, test_bundle, repo_root)


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

    # Benchmark functions that don't require complex setup
    benchmarks = [
        ("swarm_orchestrator", benchmark_swarm_orchestrator),
        ("slugify", lambda: benchmark_slugify()),
        ("json_serialization", benchmark_json_serialization),
        ("path_operations", benchmark_path_operations),
        ("yaml_cached_load", lambda: benchmark_yaml_cached_load(repo_root)),
    ]

    for name, bench_fn in benchmarks:
        try:
            if callable(bench_fn):
                result = bench_fn()
            else:
                result = bench_fn
            if result:
                results[name] = result
                print(f"{name}: avg={result.avg_time_ms:.3f}ms, min={result.min_time_ms:.3f}ms, max={result.max_time_ms:.3f}ms")
        except Exception as e:
            print(f"{name}: ERROR - {e}")

    # Try to run more complex benchmarks with fallback
    complex_benchmarks = [
        ("agent_fleet_resolution", lambda: benchmark_agent_fleet_resolution(repo_root)),
        ("memory_operations", lambda: benchmark_memory_operations(repo_root)),
    ]

    for name, bench_fn in complex_benchmarks:
        try:
            result = bench_fn()
            results[name] = result
            print(f"{name}: avg={result.avg_time_ms:.3f}ms, min={result.min_time_ms:.3f}ms, max={result.max_time_ms:.3f}ms")
        except Exception as e:
            print(f"{name}: SKIPPED - {e}")

    return results


def benchmark_slugify() -> BenchmarkResult:
    """Benchmark slugify operations"""
    from ai_os.fs_utils import slugify

    bench = Benchmark("slugify", iterations=1000)
    test_strings = [
        "Test Task Name",
        "Hello World",
        "Special!@#Characters",
        "Multiple   Spaces",
        "UPPERCASE",
        "mixedCase123",
    ]

    def do_slugify():
        for s in test_strings:
            slugify(s)

    return bench.run(do_slugify)


def benchmark_json_serialization() -> BenchmarkResult:
    """Benchmark JSON serialization/deserialization"""
    bench = Benchmark("json_serialization", iterations=500)

    test_data = {
        "name": "test_envelope",
        "task_id": "task-001",
        "epic_id": "epic-001",
        "initiative_id": "initiative-001",
        "description": "This is a test task description with some content",
        "metadata": {"key1": "value1", "key2": 123},
        "tags": ["tag1", "tag2", "tag3"],
    }

    def do_serialize():
        json.dumps(test_data)

    def doDeserialize():
        json.loads(json.dumps(test_data))

    # Combined serialize + deserialize
    def do_both():
        json.loads(json.dumps(test_data))

    return bench.run(do_both)


def benchmark_path_operations() -> BenchmarkResult:
    """Benchmark path operations"""
    bench = Benchmark("path_operations", iterations=1000)

    base = Path("/test/repo/root")
    subpath = "ops/tasks/compiled/task.json"

    def do_path_ops():
        p = base / subpath
        p.exists()
        p.parent.exists()
        str(p)
        p.suffix
        p.stem

    return bench.run(do_path_ops)


def benchmark_yaml_cached_load(repo_root: Path) -> BenchmarkResult:
    """Benchmark YAML cached loading"""
    from ai_os.fs_utils import load_yaml, _cached_load_yaml

    # Find a YAML file to benchmark
    yaml_files = list(repo_root.glob("**/*.yaml"))[:5]
    if not yaml_files:
        # Create a temporary test file
        import yaml
        test_yaml = repo_root / "_test_bench.yaml"
        test_yaml.write_text("key1: value1\nkey2: value2\n", encoding="utf-8")
        yaml_files = [test_yaml]

    bench = Benchmark("yaml_cached_load", iterations=200)
    test_file = str(yaml_files[0])

    def do_load():
        # Clear cache to test cold cache
        _cached_load_yaml.cache_clear()
        load_yaml(test_file)

    # Warm up cache
    load_yaml(test_file)

    return bench.run(do_load)


if __name__ == "__main__":
    print("Running AI OS Benchmarks...")
    print("-" * 50)
    run_all_benchmarks()
    print("-" * 50)
    print("Benchmarks complete!")

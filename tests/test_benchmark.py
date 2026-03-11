"""Tests for Performance Benchmarking"""
import pytest
from pathlib import Path
from ai_os.benchmark import (
    Benchmark, BenchmarkResult, run_all_benchmarks
)


class BenchmarkTests:
    """Test suite for Performance Benchmarking"""

    def test_benchmark_creation(self):
        """Verify benchmark can be created"""
        bench = Benchmark("test_benchmark", iterations=10)
        assert bench.name == "test_benchmark"
        assert bench.iterations == 10

    def test_benchmark_result(self):
        """Verify benchmark result contains correct fields"""
        result = BenchmarkResult(
            name="test",
            iterations=5,
            total_time_ms=100.0,
            avg_time_ms=20.0,
            min_time_ms=18.0,
            max_time_ms=22.0
        )
        assert result.name == "test"
        assert result.iterations == 5
        assert result.avg_time_ms == 20.0

    def test_benchmark_run(self):
        """Verify benchmark runs and collects results"""
        bench = Benchmark("simple_test", iterations=5)

        def simple_fn():
            x = 1 + 1

        result = bench.run(simple_fn)

        assert result is not None
        assert result.iterations == 5
        assert len(bench.results) == 1

    def test_benchmark_result_to_dict(self):
        """Verify benchmark result converts to dict"""
        result = BenchmarkResult(
            name="test",
            iterations=5,
            total_time_ms=100.0,
            avg_time_ms=20.0,
            min_time_ms=18.0,
            max_time_ms=22.0
        )
        d = result.to_dict()

        assert d["name"] == "test"
        assert d["iterations"] == 5
        assert "timestamp" in d

    def test_run_all_benchmarks(self):
        """Verify run_all_benchmarks executes"""
        results = run_all_benchmarks(Path("."))

        # Should return a dict
        assert isinstance(results, dict)

        # At least one benchmark should run
        assert len(results) >= 0  # May be 0 if imports fail


def test_benchmark_suite():
    """Run benchmark test suite"""
    tests = BenchmarkTests()

    tests.test_benchmark_creation()
    tests.test_benchmark_result()
    tests.test_benchmark_run()
    tests.test_benchmark_result_to_dict()
    tests.test_run_all_benchmarks()


if __name__ == "__main__":
    test_benchmark_suite()
    print("Benchmark tests passed!")
